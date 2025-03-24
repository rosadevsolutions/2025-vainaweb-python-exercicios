'''
Segundo Exercício: Ordenação de Tuplas
Dada uma lista de tuplas,
onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.
Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”)
'''

#importanto as funções do arquivo utils
import utils

vainawebers = [("Samuel", 20),("Karynne", 22),("Carol", 21),("Kleber", 23),("Vinicius", 25)]

def vainawebers_crescente(lista):
  lista_crescente = sorted(lista, key=lambda item: item[1])
  return print(lista_crescente)

utils.cabecalho_exercicio('2) Ordenação de Tuplas')
vainawebers_crescente(vainawebers)
utils.pular_linha()
