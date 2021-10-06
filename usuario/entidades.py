from app import db

class Usuario(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    senha = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), primary_key=True)
    animais = db.relationship('Animal', backref='usuario', lazy=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dono = db.Column(db.String(100), db.ForeignKey('usuario.nome'), nullable=False)