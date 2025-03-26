from flask import Flask, jsonify, request
import model

app = Flask(__name__)

#ROTAS DE ALUNO

@app.route("/alunos", methods=["GET"])
def getAlunos():
    return model.lista_alunos()

@app.route("/alunos/<int:idAluno>", methods=["GET"])
def getAlunoById(idAluno):
    try:
        return model.aluno_por_id(idAluno)
    except model.AlunoNaoEncontrado:
        return {"erro": "Aluno não encontrado", "codigo": 400}

@app.route("/alunos", methods=["POST"])
def createAluno():
    dados = request.json
    model.adiciona_aluno(dados)
    return model.lista_alunos()

@app.route("/alunos/<int:idAluno>", methods=["PUT"])
def updateAluno(idAluno):
    dados = request.json
    try:
        model.atualiza_aluno(idAluno, dados)
        return model.aluno_por_id(idAluno)
    except model.AlunoNaoEncontrado:
        return {"erro": "Aluno não encontrado", "codigo": 400}

@app.route("/alunos/<int:idAluno>", methods=["DELETE"])
def deleteAluno(idAluno):
    try:
        model.remove_aluno(idAluno)
        return model.lista_alunos() 
    except model.AlunoNaoEncontrado:
        return {"erro": "Aluno não encontrado", "codigo": 400}

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