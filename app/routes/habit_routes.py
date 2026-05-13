from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from app.extensions import db

from app.models.habit_model import Habit

from app.utils.responses import success, error

habit_bp = Blueprint("habit", __name__)

# LISTAR
@habit_bp.route("/v1/habits/<int:user_id>", methods=["GET"])
@jwt_required()
def get_habits(user_id):

    habits = Habit.query.filter_by(user_id=user_id).all()

    if not habits:
        return error("Nenhum hábito encontrado", 404)

    response = []

    for habit in habits:

        response.append({
            "id": habit.id,
            "nome": habit.nome,
            "categoria": habit.categoria,
            "horario_alvo": habit.horario_alvo,
            "frequencia": habit.frequencia,
            "lembrete": habit.lembrete,
            "antecedencia_lembrete": habit.antecedencia_lembrete,
            "meta_diaria": habit.meta_diaria,
            "tags": habit.tags.split(",") if habit.tags else []
        })

    return response, 200

# CRIAR
@habit_bp.route("/v1/habits", methods=["POST"])
@jwt_required()
def create_habit():

    data = request.get_json()

    required_fields = [
        "user_id",
        "nome",
        "categoria",
        "horario_alvo",
        "frequencia"
    ]

    for field in required_fields:

        if field not in data:
            return error(
                "Parâmetros obrigatórios ausentes",
                400
            )

    habit = Habit(
        user_id=data["user_id"],
        nome=data["nome"],
        descricao=data.get("descricao"),
        categoria=data["categoria"],
        horario_alvo=data["horario_alvo"],
        frequencia=data["frequencia"],
        lembrete=data.get("lembrete", False),
        antecedencia_lembrete=data.get(
            "antecedencia_lembrete"
        ),
        meta_diaria=data.get("meta_diaria"),
        tags=",".join(data.get("tags", []))
    )

    db.session.add(habit)
    db.session.commit()

    return success(
        "Hábito criado",
        {
            "id": habit.id
        },
        201
    )

# UPDATE
@habit_bp.route("/v1/habits/<int:id_habit>", methods=["PUT"])
@jwt_required()
def update_habit(id_habit):

    habit = Habit.query.get(id_habit)

    if not habit:
        return error("Hábito não encontrado", 404)

    data = request.get_json()

    for key, value in data.items():

        if key == "tags":
            value = ",".join(value)

        setattr(habit, key, value)

    db.session.commit()

    return success("Hábito atualizado")

# DELETE
@habit_bp.route("/v1/habits/<int:id_habit>", methods=["DELETE"])
@jwt_required()
def delete_habit(id_habit):

    habit = Habit.query.get(id_habit)

    if not habit:
        return error("Hábito não encontrado", 404)

    db.session.delete(habit)
    db.session.commit()

    return success("Hábito excluído")