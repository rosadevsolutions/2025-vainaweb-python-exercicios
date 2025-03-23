'''
Sétimo Exercício: Top 3 mais frequentes
Dada uma lista de números,
crie uma função que retorne
os três números mais frequentes
em ordem decrescente de frequência.
Se houver empates,
ordene pelo valor numérico.

Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
Saída: [2, 1, 4]
'''

#importanto as funções do arquivo utils
import utils

in_numeros_lista = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
out_numeros_mais_frequentes = []

def verificar_numeros_frequentes(lista):
  contador_1 = lista.count(1)
  contador_2 = lista.count(2)
  contador_3 = lista.count(3)
  contador_4 = lista.count(4)
  contador_5 = lista.count(5)

  print(contador_1)
  print(contador_2)
  print(contador_3)
  print(contador_4)
  print(contador_5)

  # Preciso compárar os valores
  # Ordenar do maior pro menor
  # e atribuir o numero
  # em caso de empate usar a ordem numerica
  #Inserir valores na nova lista

verificar_numeros_frequentes(in_numeros_lista)
