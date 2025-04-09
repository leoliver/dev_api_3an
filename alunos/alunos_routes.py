from flask import Blueprint, request, jsonify
from .alunos_model import AlunosNaoEncontrados, deleteAluno, getAlunoById, getAlunos, updateAluno, createAluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = getAlunos()
    return jsonify(alunos)