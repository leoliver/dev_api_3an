from flask import Flask, jsonify, request

app = Flask(__name__)

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
    "turma":[
        {"id": 1, 
         "nome": "DevOps", 
         "turno": "Noite"},
        {"id": 2, 
         "nome": "Desenvolvimento de API", 
         "turno": "Manhã"}
        ]
}

def getNextId(list):
    lastIndex = list[-1]
    nextId = lastIndex["id"] + 1
    return nextId

#ROTAS DE ALUNO

@app.route("/alunos", methods=["GET"])
def getAlunos():
    dados = dici["alunos"]
    return jsonify(dados)

@app.route("/alunos/<int:idAluno>", methods=["GET"])
def getAlunoById(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            return jsonify(aluno)

@app.route("/alunos", methods=["POST"])
def createAluno():
    dados = request.json
    alunos = dici["alunos"]
    dados["id"] = getNextId(alunos)
    alunos.append(dados)
    return dados

@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def updateAluno(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            dados = request.json
            chaves = dados.keys()
            for chave in chaves:
                aluno[chave] = dados[chave]
            return dados

@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deleteAluno(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno["id"] == idAluno:
            alunos.remove(aluno)
            return aluno

#ROTAS DE PROFESSOR

@app.route("/professores", methods = ["GET"])
def getProfessor():
    dados = dici["professores"]
    return jsonify(dados)

@app.route("/professores/<int:idProf>", methods=["GET"])
def getProfessorById(idProf):
    professores = dici["professores"]
    for professor in professores:
        if professor["id"] == idProf:
            return jsonify(professor)
        
@app.route("/professores", methods=["POST"])
def createProfessor():
    dados = request.json
    professores = dici["professores"]
    dados["id"] = getNextId(professores)
    professores.append(dados)
    return dados

@app.route("/professores/<int:idProf>", methods=["PUT"])
def updateProfessor(idProf):
    professores = dici["professores"]
    for professor in professores:
        if professor["id"] == idProf:
            dados = request.json
            chaves = dados.keys()
            for chave in chaves:
                professor[chave] = dados[chave]
            return dados

@app.route("/professores/<int:idProf>", methods=["DELETE"])
def deleteProfessor(idProf):
    professores = dici["professores"]
    for professor in professores:
        if professor["id"] == idProf:
            professores.remove(professor)
            return professor
        
#ROTAS DE TURMA

@app.route("/turmas", methods=["GET"])
def getTurmas():
    dados = dici["turmas"]
    return jsonify(dados)

@app.route("/turmas/<int:idTurma>", methods=["GET"])
def getTurmaById(idTurma):
    turmas = dici["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            return jsonify(turma)

@app.route("/turmas", methods=["POST"])
def createTurma():
    dados = request.json
    turmas = dici["turmas"]
    dados["id"] = getNextId(turmas)
    turmas.append(dados)
    return dados

@app.route("/turmas/<int:idTurma>", methods=["PUT"])
def updateTurma(idTurma):
    turmas = dici["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            dados = request.json
            chaves = dados.keys()
            for chave in chaves:
                turma[chave] = dados[chave]
            return dados

@app.route("/turmas/<int:idTurma>", methods=["DELETE"])
def deleteTurma(idTurma):
    turmas = dici["turmas"]
    for turma in turmas:
        if turma["id"] == idTurma:
            turmas.remove(turma)
            return turma

if __name__ == "__main__":
    app.run(debug=True)