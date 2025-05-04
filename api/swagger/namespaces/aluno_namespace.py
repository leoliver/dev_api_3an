from flask_restx import Namespace, Resource, fields
from alunos.alunos_model import getAlunos, getAlunoById, updateAluno, createAluno, deleteAluno

alunos_ns = Namespace("Alunos", description="Operações relacionadas aos alunos")

alunos_model = alunos_ns.model ("Aluno",{
    "nome": fields.String(required = True, description="Nome do aluno."),
    "data_nascimento": fields.String(required = True, description="Data de nascimento (DD-MM-AAAA)."),
    "nota_primeiro_semestre": fields.Float(required = True, description="Nota primeiro semestre."),
    "nota_segundo_semestre": fields.Float(required = True, description="Nota segundo semestre."),
    "turma_id": fields.Integer(required = True, description="ID Turma associada."),
})

alunos_output_model = alunos_ns.model("AlunoOutPut", {
    "id": fields.String(required = True, description="ID Aluno."),
    "nome": fields.String(required = True, description="Nome do aluno."),
    "data_nascimento": fields.String(required = True, description="Data de nascimento (DD-MM-AAAA)."),
    "nota_primeiro_semestre": fields.Float(required = True, description="Nota primeiro semestre."),
    "nota_segundo_semestre": fields.Float(required = True, description="Nota segundo semestre."),
    "turma_id": fields.Integer(required = True, description="ID Turma associada."),
    "media_final": fields.Float(required = True, description="Média final do Aluno."),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(alunos_output_model)
    def get(self):
        """Lista todos os alunos"""
        return getAlunos()

    @alunos_ns.expect(alunos_model)
    def post(self):
        """Cria um aluno novo"""
        data = alunos_ns.payload
        response, status_code = createAluno(data)
        return response, status_code
    
@alunos_ns.route("/<int:idAluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(alunos_output_model)
    def get(self, id_aluno):
        """Busca um aluno pelo ID"""
        return getAlunoById(id_aluno)

    @alunos_ns.expect(alunos_model)
    def put(self, id_aluno):
        """Atualiza um aluno"""
        data = alunos_ns.payload
        updateAluno(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        """Deleta um aluno"""
        deleteAluno(id_aluno)
        return {"message": "Aluno excluído com sucesso!"}, 200