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