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