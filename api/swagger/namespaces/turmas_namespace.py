from flask_restx import Namespace, Resource, fields
from turmas.turmas_model import createTurma, getTurmaById, getTurmas, deleteTurma, updateTurma

turmas_ns = Namespace("Turmas", description="Operações relacionadas às turmas")

turmas_model = turmas_ns.model("Turmas",{
    "nome":fields.String(required = True, description = "Nome da disciplina."),
    "turno":fields.String(required = True, description = "Turno da disciplina."),
    "id_professor":fields.Integer(required = True, description = "ID Professor associado.")
})

turmas_output_model = turmas_ns.model("TurmasOutPut",{
    "id":fields.Integer(required = True, description = "ID turma."),
    "nome":fields.String(required = True, description = "Nome da disciplina."),
    "turno":fields.String(required = True, description = "Turno da disciplina."),
    "id_professor":fields.Integer(required = True, description = "ID Professor associado.")

})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self):
        """Lista todas as turmas"""
        return getTurmas()
    
    @turmas_ns.marshal_list_with(turmas_model)
    def post(self):
        """Cria uma turma nova"""
        data = turmas_ns.payload
        response, status_code = createTurma(data)
        return response, status_code


@turmas_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self, id_turma):
        """Busca uma turma pelo ID"""
        return getTurmaById(id_turma)
    
    @turmas_ns.marshal_list_with(turmas_model)
    def put(self, id_turma):
        """Atualiza uma turma"""
        data = turmas_ns.payload
        updateTurma(id_turma, data)
        return data, 200
    
    def delete(self, id_turma):
        """Deleta uma turma"""
        deleteTurma(id_turma)
        return{"message": "Turma excluída com sucesso!"}, 200