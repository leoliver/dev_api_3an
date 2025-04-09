from auxiliar import *

dici = {
    "professores":[
        {"id": 1, 
         "nome":"Caio", 
         "data_nascimento":"04/05/1995",
         "disciplina":"Desenvolvimento de API",
         "salario": 1000},
        {"id": 2, 
         "nome":"Kleber", 
         "data_nascimento":"10/07/1995",
         "disciplina":"DevOps",
         "salario": 2000}
        ]
}

class ProfessoresNaoEncontrados(Exception):
    pass

def getProfessores():
    return dici["professores"]

def getProfessorById(id_professor):
    professores = dici["professores"]
    for professor in professores:
        if professor["id"] == id_professor:
            return professor
    raise ProfessoresNaoEncontrados

def createProfessor(dados):
    lista_professores = getProfessores()
    dados['id'] = getNextId(lista_professores)
    lista_professores.append(dados)
    return dici["professores"]