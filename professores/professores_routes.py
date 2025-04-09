from flask import Blueprint, request, jsonify
from .professores_model import ProfessoresNaoEncontrados, deleteProfessor, getProfessorById, getProfessores, updateProfessor, createProfessor

professores_blueprint = Blueprint('professores', __name__)