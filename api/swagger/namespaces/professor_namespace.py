from flask_restx import Namespace, Resource, fields
from professores.professores_model import getProfessores, getProfessorById, createProfessor, updateProfessor, deleteProfessor