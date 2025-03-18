from flask import Flask, jsonify, request
import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5000/alunos')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /alunos no seu server")

        try:
            retorno = r.json()
        except:
            self.fail("queria um json mas voce retornou outra coisa")

        self.assertEqual(type(retorno),type([]))
    def test_001_alunos_procura_id(self):
         r = requests.get('http://localhost:5000/alunos/1')
         resposta = r.json()
    def test_002_alunos_criacao(self):
         r = requests.post('http://localhost:5000/alunos', json={"nome": "hiago", "idade": 35, "data_nascimento": "Tem tempo", "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0, "turma_id": 1})
         resposta = requests.get('http://localhost:5000/alunos/5')
         retorno = resposta.json()
    def test_003_alunos_atualiza_dados_id(self):
         r = requests.put('http://localhost:5000/alunos/2', json={"nome": "Welington", "idade": 19, "data_nascimento": "Tem tempo", "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0, "turma_id": 1})
         resposta = requests.get('http://localhost:5000/alunos/2')
         retorno = resposta.json()
    def test_004_alunos_delete_id(self):
         r = requests.delete('http://localhost:5000/alunos/4')
         resposta = requests.get('http://localhost:5000/alunos')
         retorno = resposta.json()

    def test_100_professores_retorna_lista(self):
        r = requests.get('http://localhost:5000/professores')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /professores no seu server")

        try:
            retorno = r.json()
        except:
            self.fail("queria um json mas voce retornou outra coisa")

        self.assertEqual(type(retorno),type([])) 
    def test_101_professores_procura_id(self):
         r = requests.get('http://localhost:5000/professores/1')
         resposta = r.json()
    def test_102_professores_criacao(self):
         r = requests.post('http://localhost:5000/professores', json={'nome': 'Sidinei', 'data_nascimento': '07/08/1994', 'disciplina':'Matematica', 'salario': 3000})
         resposta = requests.get('http://localhost:5000/professores/3')
         retorno = resposta.json()
    def test_103_professores_atualiza_dados_id(self):
         r = requests.put('http://localhost:5000/professores/2', json={'disciplina':'Desenvolvimento de API'})
         resposta = requests.get('http://localhost:5000/professores/2')
         retorno = resposta.json()
    def test_104_professores_delete_id(self):
         r = requests.delete('http://localhost:5000/professores/1')
         resposta = requests.get('http://localhost:5000/professores')
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()