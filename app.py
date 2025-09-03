from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from controllers.tarefa_controller import TarefaController
from routes.tarefas_routes import tarefas_bp

# Função para criar a aplicação Flask
def create_app():
    app = Flask(__name__)
    # Configurações da aplicação
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Inicializa o banco de dados
    db.init_app(app)

    # Registra as rotas de tarefas
    app.register_blueprint(tarefas_bp)

    # Cria uma instância do controlador de tarefas
    return app

if __name__ == '__main__':
    app = create_app()
    # Cria as tabelas do banco de dados
    with app.app_context():
        db.create_all()  # Só cria as tabelas se não existirem
    app.run(debug=True)