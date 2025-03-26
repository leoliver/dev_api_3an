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
        ],
    "turmas":[
        {"id": 1, 
         "nome": "DevOps", 
         "turno": "Noite",
         "id_professor": 2},
        {"id": 2, 
         "nome": "Desenvolvimento de API", 
         "turno": "Manhã",
         "id_professor": 1},
        ],
}

class AlunoNaoEncontrado(Exception):
    pass

def getNextId(list):
    lastIndex = list[-1]
    nextId = lastIndex["id"] + 1
    return nextId

def lista_alunos():
    return dici["alunos"]

def aluno_por_id(idAluno):
    alunos = lista_alunos()
    for aluno in alunos:
        if(aluno["id"] == idAluno):
            return aluno
    raise AlunoNaoEncontrado

def adiciona_aluno(data):
    alunos = lista_alunos()
    data["id"] = getNextId("alunos")
    alunos.append(data)

def atualiza_aluno(idAluno, data):
    alunos = lista_alunos()
    for aluno in alunos:
        if aluno["id"] == idAluno:
            chaves = data.keys()
            for chave in chaves:
                if not aluno[chave] == data[chave]:
                    aluno[chave] = data[chave]
                    return
    raise AlunoNaoEncontrado

def remove_aluno(idAluno):
    alunos = lista_alunos()
    for aluno in alunos:
        if aluno["id"] == idAluno:
            alunos.remove(aluno)
            return
    raise AlunoNaoEncontrado