from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token
from .. import db, jwt
from ..models import User, TokenBlocklist

# Flask Blueprint
user_bp = Blueprint('user', __name__)

# Callback function to check if a JWT exists in the database blocklist
# From Flask JWT documentation


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None
