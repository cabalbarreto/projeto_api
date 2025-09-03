
from models import Tarefa
from models import db


class TarefaController: 
    
    @staticmethod
    def get_listar_tarefas():
        return Tarefa.query.all()

    @staticmethod
    def get_listar_tarefas_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)
    
    @staticmethod
    def criar_tarefa(id, tarefa, concluida):
        nova_tarefa = Tarefa(id=id, titulo=tarefa['titulo'], concluida=concluida)
        db.session.add(nova_tarefa)
        db.session.commit()
        return nova_tarefa
    
    @staticmethod
    def atualizar_tarefa(self, tarefa_id: int, dados: dict):
        pass
    
    @staticmethod
    def deletar_tarefa(self, tarefa_id: int):
        pass