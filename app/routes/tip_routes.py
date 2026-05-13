import random

from flask import Blueprint

from flask_jwt_extended import jwt_required

from app.models.tip_model import Tip

tip_bp = Blueprint("tip", __name__)

@tip_bp.route("/v1/dica", methods=["GET"])
@jwt_required()
def get_tip():

    tips = Tip.query.all()

    if not tips:

        return {
            "id": 1,
            "categoria": "Saúde",
            "texto": "Beba água regularmente.",
            "icone": "favorite"
        }, 200

    tip = random.choice(tips)

    return {
        "id": tip.id,
        "categoria": tip.categoria,
        "texto": tip.texto,
        "icone": tip.icone
    }, 200