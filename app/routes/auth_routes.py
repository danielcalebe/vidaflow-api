from flask import Blueprint, request

from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models.user_model import User

from app.utils.responses import success, error

auth_bp = Blueprint("auth", __name__)

# REGISTER
@auth_bp.route("/v1/users", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return error("Parâmetros inválidos", 400)

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return error("E-mail já cadastrado", 409)

    user = User(
        name=name,
        email=email
    )

    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return success(
        "Usuário criado",
        {
            "user_id": user.id
        },
        201
    )

# LOGIN
@auth_bp.route("/v1/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return error("E-mail ou senha inválidos", 401)

    if not user.check_password(password):
        return error("E-mail ou senha inválidos", 401)

    token = create_access_token(identity=str(user.id))

    return {
        "token": token,
        "user_id": user.id,
        "name": user.name,
        "expires_in": 1800
    }, 200