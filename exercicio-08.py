'''
Oitavo Exercício: Verificador de Palíndromos
Escreva uma função que recebe uma palavra
e retorna True se for um palíndromo
(ou seja, se pode ser lida da mesma forma de trás para frente)
e False caso contrário.

Exemplo:
entrada = "radar"
Saída: True
'''

#importanto as funções do arquivo utils
import utils

#crio a função com passagem de param/string
def verificar_palindromo(in_str):
  #crio var pra armazenar a inversao da string
  proc_str_reverse = ''.join(reversed(in_str))
  #crio var pra armazenar o valor do teste de comparacao de string e tring invertida
  out_message = proc_str_reverse == in_str
  #retorno o valor do var cond já exibindo no console
  return print(out_message)

utils.cabecalho_exercicio('8) Verificador de Palíndromos')
in_palavra = input('Informar uma palavra: ')
verificar_palindromo(in_palavra)
