from flask import Flask, jsonify, request
import unittest
import requests

class TestStringMethods(unittest.TestCase):

     # def test_000_alunos_retorna_lista(self):
     #      r = requests.get('http://localhost:5000/alunos')
     #      if r.status_code == 404:
     #           self.fail("Página /alunos não definida no servidor para o método GET.")

     #      try:
     #           lista_alunos = r.json()
     #      except:
     #           self.fail("Formato deveria ser JSON.")

     #      self.assertEqual(type(lista_alunos),type([]))

     # def test_001_alunos_procura_id(self):
     #      r = requests.get('http://localhost:5000/alunos/1')
               
     #      if r.status_code == 404:
     #           self.fail("Página /alunos/id não definida no servidor para o método GET por Id.")

     #      try:
     #           aluno = r.json()
     #      except:
     #           self.fail("Formato deveria ser JSON.")

     #      self.assertEqual(type(aluno),type({}))

     # def test_002_alunos_criacao(self):
          
     #      r = requests.post('http://localhost:5000/alunos', json={"nome": "Hiago", "data_nascimento": "02-05-1980", "turma_id": 1, "nota_primeiro_semestre": 0, "nota_segundo_semestre": 0, "media_final": 0})

     #      if r.status_code == 404:
     #           self.fail("Página /alunos não definida no servidor para o método POST.")

     #      resposta = requests.get('http://localhost:5000/alunos')
     #      achei = False
     #      lista_alunos = resposta.json()

     #      for aluno in lista_alunos:
     #           if aluno['nome'] == 'Hiago':
     #                achei = True
          
     #      if not achei:
     #           self.fail("Erro na criação do aluno")

     # def test_003_alunos_atualiza_dados_id(self):
     #      get = requests.get('http://localhost:5000/alunos')
     #      lista_alunos = get.json()
     #      lastIndex = lista_alunos[-1]["id"]

     #      r = requests.put(f'http://localhost:5000/alunos/{lastIndex}', json={"nome": "Welington"})

     #      if r.status_code == 404:
     #           self.fail("Página /alunos/id não definida no servidor para o método PUT.")

     #      resposta = requests.get(f'http://localhost:5000/alunos/{lastIndex}')
     #      aluno = resposta.json()
     #      if not aluno['nome'] == 'Welington':
     #           self.fail("Dados não foram atualizados")

     # def test_004_alunos_delete_id(self):
     #      get = requests.get('http://localhost:5000/alunos')
     #      lista_alunos = get.json()
     #      lastIndex = lista_alunos[-1]["id"]

     #      r = requests.delete(f'http://localhost:5000/alunos/{lastIndex}')

     #      if r.status_code == 404:
     #           self.fail("Página /alunos/id não definida no servidor para o método DELETE.")
          
     #      resposta = requests.get('http://localhost:5000/alunos')
     #      lista_alunos = resposta.json()
     #      deletado = True

     #      for aluno in lista_alunos:
     #           if aluno['id'] == lastIndex:
     #                deletado = False

     #      if not deletado:
     #           self.fail("O aluno não foi deletado corretamente.")

     # def test_100_professores_retorna_lista(self):
     #      r = requests.get('http://localhost:5000/professores')

     #      if r.status_code == 404:
     #           self.fail("Página /professores não definida no servidor para o método GET.")

     #      try:
     #           professores = r.json()
     #      except:
     #           self.fail("Formato deveria ser JSON")

     #      self.assertEqual(type(professores),type([])) 

     # def test_101_professores_procura_id(self):
     #      r = requests.get('http://localhost:5000/professores/1')
          
     #      if r.status_code == 404:
     #           self.fail("Página /professores/id não definida no servidor para o método GET por Id.")

     #      try:
     #           professor = r.json()
     #      except:
     #           self.fail("Formato deveria ser JSON.")

     #      self.assertEqual(type(professor),type({}))

     # def test_102_professores_criacao(self):
     #      r = requests.post('http://localhost:5000/professores', json={'nome': 'Sidinei', 'data_nascimento': '07-08-1997', 'disciplina':'Matematica', 'salario': 3000})

     #      if r.status_code == 404:
     #           self.fail("Página /professores não definida no servidor para o método POST.")

     #      resposta = requests.get('http://localhost:5000/professores')
     #      achei = False
     #      lista_professores = resposta.json()

     #      for professor in lista_professores:
     #           if professor['nome'] == 'Sidinei':
     #                achei = True
          
     #      if not achei:
     #           self.fail("O professor não foi encontrado")

     # def test_103_professores_atualiza_dados_id(self):
     #      get = requests.get('http://localhost:5000/professores')
     #      lista_professores = get.json()
     #      lastIndex = lista_professores[-1]["id"]

     #      r = requests.put(f'http://localhost:5000/professores/{lastIndex}', json={'disciplina':'Desenvolvimento Mobile'})

     #      if r.status_code == 404:
     #           self.fail("Página /professores/id não definida no servidor para o método PUT.")

     #      resposta = requests.get(f'http://localhost:5000/professores/{lastIndex}')
     #      professor = resposta.json()
     #      if not professor['disciplina'] == 'Desenvolvimento Mobile':
     #           self.fail("Dados não foram atualizados")

     # def test_104_professores_delete_id(self):
     #      get = requests.get('http://localhost:5000/professores')
     #      lista_professores = get.json()
     #      lastIndex = lista_professores[-1]["id"]

     #      r = requests.delete(f'http://localhost:5000/professores/{lastIndex}')
          
     #      if r.status_code == 404:
     #           self.fail("Página /professores/id não definida no servidor para o método DELETE.")
     
     #      resposta = requests.get('http://localhost:5000/professores')
     #      lista_professores = resposta.json()
     #      deletado = True

     #      for professor in lista_professores:
     #           if professor['id'] == lastIndex:
     #                deletado = False

     #      if not deletado:
     #           self.fail("O professor não foi deletado corretamente.")

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
     
     def test_202_adiciona_turma(self):
          req_turmas = requests.post('http://127.0.0.1:5000/turmas',json={"nome": "Engenharia de Requisitos", "turno": "Manhã", "id_professor": 3})
          req_turmas2 = requests.get('http://127.0.0.1:5000/turmas')
          if req_turmas.status_code == 404:
                    self.fail("Página /turmas não definida no servidor para o método POST.")

          lista_turmas = req_turmas2.json()
          achei = False

          for turma in lista_turmas:
               if turma["nome"] == "Engenharia de Requisitos":
                    achei = True

          if not achei:
               self.fail("Não achei o objeto adicionado.")        

     def test_203_atualiza_turma(self):
          get = requests.get('http://127.0.0.1:5000/turmas')
          lista_turmas = get.json()
          last_index = lista_turmas[-1]['id']
          req_turmas = requests.put(f'http://127.0.0.1:5000/turmas/{last_index}', json = {"nome": "Lógica de Programação"})
          req_turmas_att = requests.get('http://127.0.0.1:5000/turmas')
          if req_turmas.status_code == 404:
                    self.fail("Página /turmas não definida no servidor para o método PUT.")

          retorno = req_turmas_att.json()
          atualizado = False

          for turma in retorno:
               if turma["nome"] == "Lógica de Programação":
                    atualizado = True
               
          if not atualizado:
               self.fail("Disciplina não atualizada.")

          retorno = req_turmas_att.json()

     def test_204_deleta_turma(self):
          get = requests.get('http://127.0.0.1:5000/turmas')
          lista_turmas = get.json()
          last_index = lista_turmas[-1]['id']
          req_turmas = requests.post('http://127.0.0.1:5000/turmas', json={"nome": "Engenharia de Requisitos", "turno": "Manhã", "id_professor":2})
          req_turmas3 = requests.delete(f'http://127.0.0.1:5000/turmas/{last_index}')
          req_turmas2 = requests.get('http://127.0.0.1:5000/turmas')
          if req_turmas.status_code == 404:
                    self.fail("Página /turmas não definida no servidor para o método DELETE.")

          lista_turmas = req_turmas2.json()
          deletado = True

          for turma in lista_turmas:
               if turma["id"] == last_index:
                    deletado = False
          
          if not deletado:
               self.fail("A turma não foi deletada.")     
                        

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()