from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .. import db
from ..models import User

# Flask Blueprint
admin_bp = Blueprint('admin', __name__)

# POST | Creates athlete if of admin role


@admin_bp.route('/athlete', methods=["POST"])
@jwt_required()
def create_athlete():
    # Is requesting user is Admin
    admin_last_name = get_jwt_identity()
    admin = User.query.filter_by(last_name=admin_last_name, is_admin=True)
    if not admin:
        return jsonify({"message": "Invalid priviliges"})

    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    is_admin = data.get('is_admin')

    # Searches database for User with matching name
    if User.query.filter_by(first_name=first_name, last_name=last_name).first():
        return jsonify({"message": "User already exists"}), 409

    # Creating new User instance with hashed password
    new_user = User(first_name=first_name,
                    last_name=last_name)
    if is_admin:
        new_user.is_admin = True

    new_user.password = data.get('password')
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User successfully created"}), 201

# PUT | Fully edits user if of admin role


@admin_bp.route('/athlete/<int:id>', methods=["PUT"])
@jwt_required()
def edit_user(id):
    # Is requesting user is Admin
    admin_last_name = get_jwt_identity()
    admin = User.query.filter_by(last_name=admin_last_name, is_admin=True)
    if not admin:
        return jsonify({"message": "Invalid priviliges"})

    data = request.get_json()

    user_edited = User.query.filter_by(id=id).first()

    if not user_edited:
        return jsonify({"message": "User not found"}), 404

    new_first_name = data.get('new_first_name')
    new_last_name = data.get('new_last_name')

    if not new_first_name or not new_first_name.strip() or not new_last_name or not new_last_name.strip():
        return jsonify({"message": "Invalid Content"}), 400

    user_edited.first_name = new_first_name.strip()
    user_edited.last_name = new_last_name.strip()

    db.session.commit()

    return jsonify({"message": f"User successfully updated to {new_first_name} {new_last_name}"}), 200


# PATCH | Updates kilo access of user if of admin role
@admin_bp.route('/athlete/<int:id>', methods=["PATCH"])
@jwt_required()
def update_kilo_access(id):
    # Is requesting user is Admin
    admin_last_name = get_jwt_identity()
    admin = User.query.filter_by(last_name=admin_last_name, is_admin=True)
    if not admin:
        return jsonify({"message": "Invalid priviliges"})

    user_edited = User.query.filter_by(id=id).first()

    if not user_edited:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    update = data.get("kilo_access")

    if not update:
        return jsonify({"message": "Invalid update"}), 400

    user_edited.kilo_access = update

    db.session.commit()

    return jsonify({"message": f"Kilo access updated for {user_edited.first_name} {user_edited.last_name}"}), 200


# DELETE | Deletes user if of admin role


@admin_bp.route('/athlete/<int:id>', methods=["DELETE"])
@jwt_required()
def delete_user(id):
    # Is requesting user an Admin
    admin_last_name = get_jwt_identity()
    admin = User.query.filter_by(last_name=admin_last_name, is_admin=True)
    if not admin:
        return jsonify({"message": "Invalid priviliges"})

    current_user = User.query.filter_by(id=id).first()

    if not current_user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(current_user)
    db.session.commit()

    return jsonify({"message": f"User {current_user.first_name} {current_user.last_name} successfully deleted"}), 200
