from flask import Blueprint, request, jsonify
from .turmas_model import TurmasNaoEncontradas, deleteTurma, getTurmaById, getTurmas, updateTurma, createTurma

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = getTurmas()
    return jsonify(turmas)

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['GET'])
def get_turma_by_id(idTurma):
    try:
        turma = getTurmaById(idTurma)
        return jsonify(turma)
    except TurmasNaoEncontradas:
        return jsonify({"erro": "Turma nao encontrada"})

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    dados = request.json
    turma = createTurma(dados)
    return jsonify(turma)