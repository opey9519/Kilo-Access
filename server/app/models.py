from . import db, bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timezone


class User(db.Model):
    def __init__(self, first_name, last_name, kilo_access, is_admin) -> None:
        self.first_name = first_name,
        self.last_name = last_name,
        self.kilo_access = kilo_access,
        self.is_admin = is_admin

    id = db.Column(db.Integer, primary_key=True, index=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True,
                     nullable=False, default=uuid.uuid4)
    first_name = db.Column(db.String(160), nullable=False, index=True)
    last_name = db.Column(db.String(160), nullable=False)
    kilo_access = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "kilo_access": self.kilo_access,
            "is_admin": self.is_admin,
            "_uuid": self.uuid
        }

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

# Officer model | contains athlete data


class Officer(db.Model):
    def __init__(self, first_name, last_name, kilo_access, is_admin) -> None:
        self.first_name = first_name,
        self.last_name = last_name,
        self.kilo_access = kilo_access,
        self.is_admin = is_admin

    id = db.Column(db.Integer, primary_key=True, index=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True,
                     nullable=False, default=uuid.uuid4)
    first_name = db.Column(db.String(160), nullable=False, index=True)
    last_name = db.Column(db.String(160), nullable=False)
    _password_hash = db.Column(db.String(128))
    kilo_access = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Returns dictionary of User information
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "kilo_access": self.kilo_access,
            "is_admin": self.is_admin,
            "_uuid": self.uuid
        }

    # Identifies password attribute as a write-only field
    @property
    def password(self):
        raise AttributeError("Password: write-only field")

    # Sets password through bcrypt hashing algorithm
    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(
            password).decode("utf-8")

    # Checks password argument against password instance using bcrypt
    def check_password(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f"<Officer {self.first_name} {self.last_name}>"


class TokenBlocklist(db.Model):
    def __init__(self, jti, token_type) -> None:
        self.jti = jti,
        self.token_type = token_type

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    token_type = db.Column(db.String(16), nullable=False)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc))
