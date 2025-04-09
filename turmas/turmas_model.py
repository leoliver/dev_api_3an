from auxiliar import *

dici = {
    "turmas":[
        {"id": 1, 
         "nome": "DevOps", 
         "turno": "Noite",
         "id_professor": 2},
        {"id": 2, 
         "nome": "Desenvolvimento de API", 
         "turno": "ManhÃ£",
         "id_professor": 1},
        ]
}

class TurmasNaoEncontradas(Exception):    
    pass

def getTurmas():
    turmas = dici["turmas"]
    return turmas

def getTurmaById(idTurma):
    turmas = dici["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return turma
    raise TurmasNaoEncontradas

def createTurma(dados):
    lista_turmas = getTurmas()
    dados["id"] = getNextId(lista_turmas)
    lista_turmas.append(dados)
    return dici["turmas"]

def updateTurma(idTurma, dados):
    turma = getTurmaById(idTurma)
    turma.update(dados)
    return