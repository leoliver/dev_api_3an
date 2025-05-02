from flask_restx import Namespace, Resource, fields
from professores.professores_model import getProfessores, getProfessorById, createProfessor, updateProfessor, deleteProfessor
professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

#Entrada de dados
professores_model = professores_ns.model("Professores", {
    "nome": fields.String(required=True, description="Nome do professor."),
    "idade": fields.Integer(required=True, description="Idade do professor."),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (DD-MM-AAAA)."),
    "disciplina": fields.String(required=True, description="Disciplina que o professor ministra."),
    "salario": fields.Float(required=True, description="Salário do professor.")
})

#Saída de dados
professores_output_model = professores_ns.model("ProfessoresOutput", {
    "id": fields.Integer(description="ID professor."),
    "nome": fields.String(description="Nome do professor."),
    "idade": fields.Integer(description="Idade do professor."),
    "data_nascimento": fields.String(description="Data de nascimento (DD-MM-AAAA)."),
    "disciplina": fields.String(description="Disciplina que o professor ministra."),
    "salario": fields.Float(description="Salário do professor.")    
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self):
        """Lista todos os professores"""
        return getProfessores()
    @professores_ns.expect(professores_model)
    def post(self):
        """Cria um professor novo"""
        data = professores_ns.payload
        response, status_code = createProfessor(data)
        return response, status_code

@professores_ns.route("/<int:idProfessor>")
class ProfessoresResource(Resource):
    @professores_ns.marshal_with(professores_output_model)
    def get(self, idprofessor):
        """Busca um professor pelo ID"""
        return getProfessorById(idprofessor)
    
    @professores_ns.expect(professores_model)
    def put(self, idprofessor):
        """Atualiza um professor"""
        data = professores_ns.payload
        updateProfessor(idprofessor, data)
        return data, 200
    
    def delete(self, idprofessor):
        """Deleta um professor"""
        deleteProfessor(idprofessor)
        return {"message": "Aluno excluído com sucesso!"}, 200
    