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
in_alunos_dict = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
i = 0

#criar função com passagem de param/dicionario
def media_tuplas(in_dict):

  #iterar dicionario pot items
  for key, val in in_dict.items():
    #calcular media
    proc_media = sum(val)/3
    #arredondar média pra cima com 2 casa decimais
    proc_media = round(proc_media, 2)
    #atribuir a média ao dicionario
    in_dict[key] = proc_media

  #converter dicionario em lista de tuplas
  out_list_tuples = list(in_dict.items())
  return print(out_list_tuples)

utils.cabecalho_exercicio('5) Tupla de médias')
media_tuplas(in_alunos_dict)
utils.pular_linha()
