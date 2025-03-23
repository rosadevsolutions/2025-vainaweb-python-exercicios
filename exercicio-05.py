'''
Quinto Exercício: Tupla de médias
Dado um dicionário onde
as chaves são nomes de alunos e
os valores são listas com suas notas,
crie uma função que retorna uma lista de tuplas,
onde cada tupla contém o nome do aluno e sua média de notas.

Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]
'''

#importanto as funções do arquivo utils
import utils

#Entrada - Dicionário
alunos_set = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
i = 0

def media_tuplas(dicionario):
  for chave, valores in dicionario.items():
    media = sum(valores)/3
    media = round(media, 2)
    dicionario[chave] = media
  conversao_tupla = dicionario.items()
  return print(conversao_tupla)

media_tuplas(alunos_set)
