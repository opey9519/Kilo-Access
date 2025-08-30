from flask import Blueprint, jsonify
from ..models import User, Officer
from ..util import generate_qr_code


# Flask Blueprint
user_bp = Blueprint("user", __name__)

# GET | Get all users


@user_bp.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    officers = Officer.query.all()

    users_returned = []
    for user in users:
        users_returned.append(user.serialize())

    officers_returned = []
    for officer in officers:
        officers_returned.append(officer.serialize())

    users_returned += officers_returned

    return jsonify({"users": users_returned}), 200


# GET Specific User & return QR code
@user_bp.route('/user/<int:id>', methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)

    # Permanent URL for this user's profile
    qr_url = f"http://localhost:5173/qr/{user.uuid}"

    # Generate QR Code
    # Convert to Base64 string so frontend can render as <img src="data:image/png;base64,...">
    qr_base64 = generate_qr_code(qr_url)

    return jsonify({"qr_code": f"data:image/png;base64,{qr_base64}",
                    "user": user.serialize()}), 200

# Get Specific Officer & return QR code


@user_bp.route('/officer/<int:id>', methods=["GET"])
def get_officer(id):
    officer = Officer.query.get_or_404(id)

    # Permanent URL for this user's profile
    qr_url = f"http://localhost:5173/qr/{officer.uuid}"

    # Generate QR Code
    # Convert to Base64 string so frontend can render as <img src="data:image/png;base64,...">
    qr_base64 = generate_qr_code(qr_url)

    return jsonify({"qr_code": f"data:image/png;base64,{qr_base64}",
                    "officer": officer.serialize()}), 200
