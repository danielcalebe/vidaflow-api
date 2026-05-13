from app.extensions import db

class Tip(db.Model):
    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True)

    categoria = db.Column(db.String(50))

    texto = db.Column(db.String(255))

    icone = db.Column(db.String(50))