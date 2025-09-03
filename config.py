import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "geleira@1")
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:SECRET_KEY@127.0.0.1:5433/tarefas_api_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False



"""Adicione a chave de configuração SQLALCHEMY_TRACK_MODIFICATIONS = False ao app flask.
Com isso na hora de instanciar o aplicativo na instancia do FlaskSQLAlchemy não será mostrado."""