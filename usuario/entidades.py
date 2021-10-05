from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    senha = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    