from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token
from .. import db, jwt
from ..models import User, TokenBlocklist

# Flask Blueprint
auth_bp = Blueprint('auth', __name__)

# Callback function to check if a JWT exists in the database blocklist
# From Flask JWT documentation


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None


# POST | Signin


@auth_bp.route('/signin', methods=["POST"])
def sign_in():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not first_name or not last_name or not data.get('password'):
        return jsonify({"message": "Credentials required"}), 400

    current_user = User.query.filter_by(
        first_name=first_name, last_name=last_name).first()
    if not current_user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not current_user.check_password(data.get('password')):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=last_name)
    refresh_token = create_refresh_token(identity=last_name)

    return jsonify({"message": "Successfully Logged In",
                    "is_admin": current_user.is_admin,
                    "access_token": access_token,
                    "refresh_token": refresh_token}), 200

# POST | Signout adds JWT to TokenBlocklist table in database


@auth_bp.route('/signout', methods=["POST"])
@jwt_required()
def sign_out():
    token = get_jwt()
    jti = token.get('jti')
    ttype = token.get('type')

    # Revoking JWT by adding to TokenBlocklist table
    db.session.add(TokenBlocklist(jti=jti, token_type=ttype))
    db.session.commit()

    return jsonify({"message": "Successfully Logged Out"}), 200

#  Refresh Token route - Required valid JWT & Refresh token, upon verification, update access token


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required()
def refreshToken():
    identity = get_jwt_identity()
    refresh_token = request.get_json().get('refresh_token')

    if not refresh_token:
        return jsonify({"message": "Invalid refresh token"}), 400

    new_access_token = create_access_token(identity=identity)

    return jsonify({"access_token": new_access_token}), 200
