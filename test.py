from flask import Flask, jsonify, request
import unittest
import requests

class TestStringMethods(unittest.TestCase):

     def test_000_alunos_retorna_lista(self):
          r = requests.get('http://localhost:5000/alunos')
          if r.status_code == 404:
               self.fail("Página /alunos não definida no servidor para o método GET.")

          try:
               lista_alunos = r.json()
          except:
               self.fail("Formato deveria ser JSON.")

          self.assertEqual(type(lista_alunos),type([]))

     def test_001_alunos_procura_id(self):
          r = requests.get('http://localhost:5000/alunos/1')
               
          if r.status_code == 404:
               self.fail("Página /alunos/id não definida no servidor para o método GET por Id.")

          try:
               aluno = r.json()
          except:
               self.fail("Formato deveria ser JSON.")

          self.assertEqual(type(aluno),type({}))

     def test_002_alunos_criacao(self):
          r = requests.post('http://localhost:5000/alunos', json={"nome": "Hiago", "idade": 35, "data_nascimento": "Tem tempo", "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0, "turma_id": 1})

          if r.status_code == 404:
               self.fail("Página /alunos não definida no servidor para o método POST.")

          resposta = requests.get('http://localhost:5000/alunos')
          achei = False
          lista_alunos = resposta.json()

          for aluno in lista_alunos:
               if aluno['nome'] == 'Hiago':
                    achei = True
          
          if not achei:
               self.fail("O aluno não foi encontrado")


     def test_003_alunos_atualiza_dados_id(self):
          r = requests.put('http://localhost:5000/alunos/2', json={"nome": "Welington", "idade": 19})

          if r.status_code == 404:
               self.fail("Página /alunos/id não definida no servidor para o método PUT.")

          resposta = requests.get('http://localhost:5000/alunos/2')
          aluno = resposta.json()
          if not (aluno['nome'] == 'Welington' and aluno['idade'] == 19):
               self.fail("Dados não foram atualizados")

     def test_004_alunos_delete_id(self):
          r = requests.delete('http://localhost:5000/alunos/4')

          if r.status_code == 404:
               self.fail("Página /alunos/id não definida no servidor para o método DELETE.")
          
          resposta = requests.get('http://localhost:5000/alunos')
          lista_alunos = resposta.json()
          deletado = True

          for aluno in lista_alunos:
               if aluno['id'] == 4:
                    deletado = False

          if not deletado:
               self.fail("O aluno não foi deletado corretamente.")

     def test_100_professores_retorna_lista(self):
          r = requests.get('http://localhost:5000/professores')

          if r.status_code == 404:
               self.fail("Página /professores não definida no servidor para o método GET.")

          try:
               retorno = r.json()
          except:
               self.fail("Formato deveria ser JSON")

          self.assertEqual(type(retorno),type([])) 

     def test_101_professores_procura_id(self):
               r = requests.get('http://localhost:5000/professores/1')
               
               if r.status_code == 404:
                    self.fail("Página /professores/id não definida no servidor para o método GET por Id.")

               try:
                    professor = r.json()
               except:
                    self.fail("Formato deveria ser JSON.")

               self.assertEqual(type(professor),type({}))

     def test_102_professores_criacao(self):
               r = requests.post('http://localhost:5000/professores', json={'nome': 'Sidinei', 'data_nascimento': '1994-08-07', 'disciplina':'Matematica', 'salario': 3000})

               if r.status_code == 404:
                    self.fail("Página /professores não definida no servidor para o método POST.")

               resposta = requests.get('http://localhost:5000/professores')
               achei = False
               lista_professores = resposta.json()

               for professor in lista_professores:
                    if professor['nome'] == 'Sidinei':
                         achei = True
               
               if not achei:
                    self.fail("O professor não foi encontrado")

     def test_103_professores_atualiza_dados_id(self):
               r = requests.put('http://localhost:5000/professores/2', json={'disciplina':'Desenvolvimento Mobile'})

               if r.status_code == 404:
                    self.fail("Página /professores/id não definida no servidor para o método PUT.")

               resposta = requests.get('http://localhost:5000/professores/2')
               professor = resposta.json()
               if not professor['disciplina'] == 'Desenvolvimento Mobile':
                    self.fail("Dados não foram atualizados")

     def test_104_professores_delete_id(self):
               r = requests.delete('http://localhost:5000/professores/2')
               
               if r.status_code == 404:
                    self.fail("Página /professores/id não definida no servidor para o método DELETE.")
          
               resposta = requests.get('http://localhost:5000/professores')
               lista_professores = resposta.json()
               deletado = True

               for professor in lista_professores:
                    if professor['id'] == 2:
                         deletado = False

               if not deletado:
                    self.fail("O professor não foi deletado corretamente.")

     #Testes Turmas     
     def test_200_busca_as_turmas(self):

          req_turmas = requests.get('http://127.0.0.1:5000/turmas')
          if req_turmas.status_code == 404:
                    self.fail("Página /turmas não definida no servidor para o método GET.")
               
          try:
               retorno = req_turmas.json()
               
          except:
               self.fail("Seu objeto não foi convertido para Json.")
          
          self.assertEqual(type(retorno), type([]))
     
     def test_201_busca_turma_por_ID(self):
          req_turmas = requests.get('http://127.0.0.1:5000/turmas/1')
          retorno = req_turmas.json()
          if req_turmas.status_code == 404:
                    self.fail("Página /turmas/id não definida no servidor para o método GET.")

          self.assertEqual(retorno['id'],1)


     

          

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()