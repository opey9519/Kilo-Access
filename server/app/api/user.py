from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token
from .. import db, jwt
from ..models import User, TokenBlocklist
from ..util import generate_qr_code


# Flask Blueprint
user_bp = Blueprint("user", __name__)

# GET | Get all users


@user_bp.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()

    users_returned = []
    for user in users:
        userdict = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "kilo_access": user.kilo_access,
            "is_admin": user.is_admin
        }

        users_returned.append(userdict)

    return jsonify({"message": "Returned all Users",
                    "Users": users_returned}), 200


@user_bp.route('/user/<int:id>', methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)

    # Permanent URL for this user's profile
    qr_url = f"http://localhost:5173/qr/{user.uuid}"

    # Generate QR Code
    # Convert to Base64 string so frontend can render as <img src="data:image/png;base64,...">
    qr_base64 = generate_qr_code(qr_url)

    userdict = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "kilo_access": user.kilo_access,
        "is_admin": user.is_admin,
        "qr_code": f"data:image/png;base64,{qr_base64}"  # frontend-ready
    }

    return jsonify(userdict), 200
