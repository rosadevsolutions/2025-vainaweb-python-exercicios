'''
Segundo Exercício: Ordenação de Tuplas
Dada uma lista de tuplas,
onde cada tupla contém o nome de uma pessoa e sua idade,
escreva uma função que retorne a lista ordenada pela idade de forma crescente.
Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)
Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”)
'''

vainawebers = [("Samuel", 20),("Karynne", 22),("Carol", 21),("Kleber", 23),("Vinicius", 25)]

def vainawebers_crescente(lista):
  lista_crescente = sorted(lista, key=lambda item: item[1])
  return print(lista_crescente)

vainawebers_crescente(vainawebers)
