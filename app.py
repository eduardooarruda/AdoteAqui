from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(): 

    load_dotenv('.env') 
    
    app = Flask(__name__)
    
    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bcrypt.init_app(app)    
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    with app.app_context():

        from usuario.usuario import bp_usuarios
        app.register_blueprint(bp_usuarios)

        @app.route('/')
        def index():
            return render_template('base.html')
    return app