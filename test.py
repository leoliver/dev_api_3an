from flask import Flask, jsonify, request
import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5000/alunos')
        if r.status_code == 404:
            self.fail("Página /turmas não definida no servidor para o método GET.")

        try:
            retorno = r.json()
        except:
            self.fail("queria um json mas voce retornou outra coisa")

        self.assertEqual(type(retorno),type([]))

    def test_001_alunos_procura_id(self):
        r = requests.get('http://localhost:5000/alunos/1')
            
        if r.status_code == 404:
            self.fail("Página /turmas/id não definida no servidor para o método GET por Id.")

        try:
            resposta = r.json()
        except:
            self.fail("Formato deveria ser JSON.")

        self.assertEqual(type(resposta),type({}))

    def test_002_alunos_criacao(self):
        r = requests.post('http://localhost:5000/alunos', json={"nome": "Hiago", "idade": 35, "data_nascimento": "Tem tempo", "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0, "turma_id": 1})

        if r.status_code == 404:
            self.fail("Página /turmas não definida no servidor para o método POST.")

        resposta = requests.get('http://localhost:5000/alunos')
        achei = False
        lista_alunos = resposta.json()

        for aluno in lista_alunos:
            if aluno['nome'] == 'Hiago':
                achei = True
        
        if not achei:
            self.fail("O aluno não foi encontrado")


    def test_003_alunos_atualiza_dados_id(self):
        r = requests.put('http://localhost:5000/alunos/2', json={"nome": "Welington", "idade": 19, "data_nascimento": "Tem tempo", "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0, "turma_id": 1})
        resposta = requests.get('http://localhost:5000/alunos/2')
        retorno = resposta.json()
    def test_004_alunos_delete_id(self):
        r = requests.delete('http://localhost:5000/alunos/4')
        resposta = requests.get('http://localhost:5000/alunos')
        retorno = resposta.json()

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()