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
        return jsonify({"erro": "Turma nao encontrada","código": 404})

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    dados = request.json
    turma = createTurma(dados)
    return jsonify(turma)

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def update_turma(idTurma):
    dados = request.json
    try:
        turma = updateTurma(idTurma, dados)
        return jsonify(turma)
    except TurmasNaoEncontradas:
        return jsonify({"erro": "Turma nao encontrada","código": 404})
    
@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    try:
        deleteTurma(idTurma)
        return jsonify({"sucesso": "Turma deletada com sucesso"})
    except TurmasNaoEncontradas:
        return jsonify({"erro": "Turma nao encontrada","código": 404})