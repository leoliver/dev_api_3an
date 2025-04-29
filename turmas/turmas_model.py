from config import db

class Turma(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    turno = db.Column(db.String(30))
    id_professor = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship('Professor', back_populates = 'turmas')
    alunos = db.relationship('Aluno', back_populates = 'turma')

    def __init__(self, nome, turno, id_professor):
        self.nome = nome
        self.turno = turno
        self.id_professor = id_professor

    def to_dict(self):
        return {
         "id": self.id,
         "nome": self.nome,
         "turno": self.turno,
         "id_professor": self.id_professor
        }


class TurmasNaoEncontradas(Exception):    
    pass

def getTurmas():
    turmas = Turma.query.all()
    lista_turmas = []
    for turma in turmas:
        lista_turmas.append(turma.to_dict())
    return lista_turmas

def getTurmaById(idTurma):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmasNaoEncontradas
    return turma.to_dict()

def createTurma(dados):
    novaTurma = Turma(nome=dados['nome'], turno=dados['turno'], id_professor=dados['id_professor'])
    db.session.add(novaTurma)
    db.session.commit()
    return novaTurma.to_dict()

def updateTurma(idTurma, dados):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmasNaoEncontradas
    for chave, valor in dados.items():
        if hasattr(turma, chave):
            setattr(turma, chave, valor)
    
    db.session.commit()
    return turma.to.dict()

def deleteTurma(idTurma):
    turma = Turma.query.get(idTurma)
    if not turma:
        raise TurmasNaoEncontradas
    db.session.delete(turma)
    db.session.commit()