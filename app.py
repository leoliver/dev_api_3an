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

if __name__ == "__main__":
    app.run(debug=True)