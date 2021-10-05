from flask import Flask, render_template

def create_app(): 
    app = Flask(__name__)
    with app.app_context():
        
        from usuario.usuario import bp_usuarios
        app.register_blueprint(bp_usuarios)

        @app.route('/')
        def index():
            return render_template('base.html')
    return app