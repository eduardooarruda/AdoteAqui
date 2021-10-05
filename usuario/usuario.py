from flask import Blueprint, render_template

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates_usuarios')

@bp_usuarios.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')