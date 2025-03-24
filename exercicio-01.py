'''
Primeiro Exercício: Soma de elementos pares
Escreva uma função que recebe uma lista de números inteiros
e retorna a soma de todos os elementos pares contidos nela.
Exemplo: [2,4,10,3,9,7,15,22]
Saída: A soma dos pares é: x
'''

#importanto as funções do arquivo utils
import utils

in_numeros_lista = [2,4,10,3,9,7,15,22]

def proc_numeros_pares_calc(numeros):
  out_numeros_pares_soma = 0
  for numero in numeros:
    if(numero % 2 == 0):
      out_numeros_pares_soma = out_numeros_pares_soma + numero
  return print(f'A soma dos pares é: {out_numeros_pares_soma}')

utils.cabecalho_exercicio('1) Soma de elementos pares')
proc_numeros_pares_calc(in_numeros_lista)
utils.pular_linha()
