from app.extensions import db

class Habit(db.Model):
    __tablename__ = "habits"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    nome = db.Column(db.String(60), nullable=False)

    descricao = db.Column(db.String(200))

    categoria = db.Column(db.String(50), nullable=False)

    horario_alvo = db.Column(db.String(10), nullable=False)

    frequencia = db.Column(db.String(50), nullable=False)

    lembrete = db.Column(db.Boolean, default=False)

    antecedencia_lembrete = db.Column(db.String(20))

    meta_diaria = db.Column(db.Integer)

    tags = db.Column(db.String(255))