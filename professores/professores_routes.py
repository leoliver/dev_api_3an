from flask import Blueprint, request, jsonify
from .professores_model import ProfessoresNaoEncontrados, deleteProfessor, getProfessorById, getProfessores, updateProfessor, createProfessor

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = getProfessores()
    return jsonify(professores)

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_professor_by_id(idProfessor):
    try:
        professor = getProfessorById(idProfessor)
        return jsonify(professor)
    except ProfessoresNaoEncontrados:
        return jsonify({"erro": "Professor nao encontrado"})
    
@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    dados = request.json
    professor = createProfessor(dados)
    return jsonify(professor)

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    dados = request.json
    try:
        professor = updateProfessor(idProfessor, dados)
        return jsonify(professor)
    except ProfessoresNaoEncontrados:
        return jsonify({"erro": "Professor nao encontrado"})