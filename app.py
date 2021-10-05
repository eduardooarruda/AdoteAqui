from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        load_dotenv('.env')

        db.init_app(app)

        from usuario.usuario import bp_usuarios
        app.register_blueprint(bp_usuarios)

        @app.route('/')
        def index():
            return render_template('base.html')
    return app