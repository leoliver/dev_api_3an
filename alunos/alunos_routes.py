from flask import Blueprint, request, jsonify
from .alunos_model import AlunosNaoEncontrados, deleteAluno, getAlunoById, getAlunos, updateAluno, createAluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = getAlunos()
    return jsonify(alunos)

@alunos_blueprint.route('/alunos/<int:idAluno>', methods=['GET'])
def getalunobyid(idAluno):
    try:
        aluno = getAlunoById(idAluno)
        return jsonify(aluno)
    except AlunosNaoEncontrados:
        return jsonify({"erro": "Aluno nao encontrado"})
    
@alunos_blueprint.route('/alunos', methods=['POST'])
def createaluno():
    dados = request.json
    aluno = createAluno(dados)
    return jsonify(aluno)

@alunos_blueprint.route('/alunos/<int:idAluno>', methods=['PUT'])
def updatealuno(idAluno):
    dados = request.json
    try:
        aluno = updateAluno(idAluno, dados)
        return jsonify(aluno)
    except AlunosNaoEncontrados:
        return jsonify({"erro": "Aluno nao encontrado"})