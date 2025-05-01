from flask_restx import Namespace, Resource, fields
from turmas.turmas_model import createTurma, getTurmaById, getTurmas, deleteTurma, updateTurma