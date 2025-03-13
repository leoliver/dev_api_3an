from flask import Flask, jsonify, request

app = Flask(__name__)

dici = {
    "alunos":[
        {"id": 1, "nome":"Leonardo", "idade": 23},
        {"id": 2, "nome":"Joana", "idade": 23},
        {"id": 3, "nome":"Renoir", "idade": 19}
        ],
    "professores":[
        {"id": 1, "nome":"Caio", "disciplina":"Desenvolvimento de API"},
        {"id": 2, "nome":"Kleber", "disciplina":"DevOps"}
        ],
    "turma":[
        {"id": 1, "nome": "DevOps", "turno": "Noite"},
        {"id": 2, "nome": "Desenvolvimento de API", "turno": "Manhã"}
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

if __name__ == "__main__":
    app.run(debug=True)