from flask import Blueprint, request, jsonify
from .professores_model import ProfessoresNaoEncontrados, deleteProfessor, getProfessorById, getProfessores, updateProfessor, createProfessor

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = getProfessores()
    return jsonify(professores)