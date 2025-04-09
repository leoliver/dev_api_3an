from auxiliar import *

dici = {
    "alunos":[
        {"id": 1,
         "nome": "Sid",
         "idade": 28,
         "data_nascimento": "ontem",
         "nota_primeiro_semestre": 0,
         "nota_segundo_semestre": 0,
         "media_final": 0,
         "turma_id": 1},
        {"id": 2,
         "nome": "Leonardo",
         "idade": 23,
         "data_nascimento": "anteontem",
         "nota_primeiro_semestre": 0,
         "nota_segundo_semestre": 0,
         "media_final": 0,
         "turma_id": 1},
        {"id": 3,
         "nome": "Joana",
         "idade": 23,
         "data_nascimento": "há um tempo",
         "nota_primeiro_semestre": 0,
         "nota_segundo_semestre": 0,
         "media_final": 0,
         "turma_id": 1},
        {"id": 4,
         "nome": "Renoir",
         "idade": 19,
         "data_nascimento": "Amanhã",
         "nota_primeiro_semestre": 0,
         "nota_segundo_semestre": 0,
         "media_final": 0,
         "turma_id": 1}
        ],
}

class AlunosNaoEncontrados(Exception):
    pass

def getAlunos():
    return dici["alunos"]

def getAlunoById(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            return aluno
    raise AlunosNaoEncontrados

def createAluno(dados):
    lista_alunos = getAlunos()
    dados['id'] = getNextId(lista_alunos)
    lista_alunos.append(dados)
    return dici["alunos"]
