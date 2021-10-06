from flask import Blueprint, render_template, request, flash, redirect
from usuario.entidades import Usuario, Animal
from app import db

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates_usuarios')

@bp_usuarios.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@bp_usuarios.route('/banco')
def banco():
    usuarios = Usuario.query.all()
    return(usuarios)

@bp_usuarios.post('/addcadastro')
def cadastrar():
    usuario = Usuario()
    animal = Animal()
    usuario.nome = request.form['nome']
    usuario.senha = request.form['senha']
    db.session.add(usuario)
    db.session.commit()

    animal.dono = int(request.form['ID'])
    animal.nome = request.form['nomeAnimal']
    db.session.add(animal)
    db.session.commit()
    return redirect('/')