from turmas.turmas_model import TurmasNaoEncontradas, getTurmas
from config import db
from datetime import datetime,date

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'))
    turma = db.relationship('Turma', back_populates = 'alunos')

    def __init__(self, nome, data_nascimento, turma_id, nota_primeiro_semestre=0, nota_segundo_semestre=0, media_final=0):
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
        self.idade = self.calcular_idade(self.data_nascimento)
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media(self.nota_primeiro_semestre, self.nota_segundo_semestre)
        self.turma_id = turma_id

    def calcular_media(self, nota_primeiro_semestre, nota_segundo_semestre):
        media = (nota_primeiro_semestre + nota_segundo_semestre)/2
        return media

    def calcular_idade(self, nascimento):
        hoje = date.today()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def to_dict(self):
        return {"id": self.id,
         "nome": self.nome,
         "idade": self.idade,
         "data_nascimento": self.data_nascimento.strftime("%d-%m-%Y"),
         "nota_primeiro_semestre": self.nota_primeiro_semestre,
         "nota_segundo_semestre": self.nota_segundo_semestre,
         "media_final": self.media_final,
         "turma_id": self.turma_id}

class AlunosNaoEncontrados(Exception):
    pass

def getAlunos():
    alunos = Aluno.query.all()
    lista_alunos = []
    for aluno in alunos:
        lista_alunos.append(aluno.to_dict())
    return lista_alunos

def getAlunoById(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunosNaoEncontrados
    return aluno.to_dict()

def createAluno(dados):
    novoAluno = Aluno(nome=dados['nome'], data_nascimento=dados['data_nascimento'], turma_id=dados['turma_id'], nota_primeiro_semestre=dados['nota_primeiro_semestre'], nota_segundo_semestre=dados['nota_segundo_semestre'], media_final=dados['media_final'])
    db.session.add(novoAluno)
    db.session.commit()
    return novoAluno.to_dict()
    

def updateAluno(idAluno, dados):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunosNaoEncontrados
    
    for chave, valor in dados.items():
        if hasattr(aluno, chave):
            if chave == "data_nascimento" and isinstance(valor, str):
                valor = datetime.strptime(valor, "%d-%m-%Y").date()
                setattr(aluno, chave, valor)
                aluno.idade = aluno.calcular_idade(aluno.data_nascimento)
            else:
                setattr(aluno, chave, valor)

    db.session.commit()
    return aluno.to_dict()

def deleteAluno(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunosNaoEncontrados
    db.session.delete(aluno)
    db.session.commit()