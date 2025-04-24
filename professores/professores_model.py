from config import db
from datetime import datetime,date


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date)
    disciplina = db.Column(db.String(100))
    salario = db.Column(db.Float)

    def __init__(self, nome, data_nascimento, disciplina, salario):
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
        self.idade = self.calcular_idade(self.data_nascimento)
        self.disciplina = disciplina
        self.salario = salario
    
    def calcular_idade(self, nascimento):
        hoje = date.today()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def to_dict(self):
        return {"id": self.id,
         "nome": self.nome,
         "idade": self.idade,
         "data_nascimento": self.data_nascimento.strftime("%d-%m-%Y"),
         "disciplina": self.disciplina,
         "salario": self.salario}

class ProfessoresNaoEncontrados(Exception):
    pass

def getProfessores():
    professores = Professor.query.all()
    lista_professores = []
    for professor in professores:
        lista_professores.append(professor.to_dict())
    return lista_professores

def getProfessorById(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessoresNaoEncontrados
    return professor.to_dict()

def createProfessor(dados):
    novoProfessor = Professor(nome=dados['nome'], data_nascimento=dados['data_nascimento'], disciplina=dados["disciplina"], salario=dados['salario'])
    db.session.add(novoProfessor)
    db.session.commit()
    return novoProfessor.to_dict()

def updateProfessor(idProfessor, dados):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessoresNaoEncontrados
    
    for chave, valor in dados.items():
        if hasattr(professor, chave):
            if chave == "data_nascimento" and isinstance(valor, str):
                valor = datetime.strptime(valor, "%d-%m-%Y").date()
                setattr(professor, chave, valor)
                professor.idade = professor.calcular_idade(professor.data_nascimento)
            else:
                setattr(professor, chave, valor)

    db.session.commit()
    return professor.to_dict()

def deleteProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessoresNaoEncontrados
    db.session.delete(professor)
    db.session.commit()