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


def verificar_palindromo(palavra):
  proc_palavra_reversa = ''.join(reversed(palavra))
  out_mensagem = "False"

  if proc_palavra_reversa == palavra:
    out_mensagem = "True"

  return print(out_mensagem)


utils.cabecalho_exercicio('8) Verificador de Palíndromos')
in_palavra = input('Informar uma palavra: ')
verificar_palindromo(in_palavra)
