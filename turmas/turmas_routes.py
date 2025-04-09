from flask import Blueprint, request, jsonify
from .turmas_model import TurmasNaoEncontradas, deleteTurma, getTurmaById, getTurmas, updateTurma, createTurma

turmas_blueprint = Blueprint('turmas', __name__)