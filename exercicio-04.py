'''
Quarto Exercício: Contagem de Palavras
Crie uma função que recebe uma string
e conta quantas vezes cada palavra aparece nela.
Retorne um dicionário
onde a chave é a palavra e
o valor é a quantidade de ocorrências.
Exemplo: ["banana maçã banana laranja maçã maçã"]

Saída: {"banana": 2, "maçã": 3, "laranja": 1}
'''

#importanto as funções do arquivo utils
import utils

def contador_palavras(texto):
  proc_palavras = texto.split()

  out_contador_item_1 = 0
  out_contador_item_2 = 0
  out_contador_item_3 = 0
  out_dic_palavras = {}

  for palavra in proc_palavras :
    if(palavra == 'banana'):
      out_contador_item_1 += 1
    elif(palavra == 'maçã'):
      out_contador_item_2 += 1
    else:
      out_contador_item_3 += 1

  out_dic_palavras = {"banana": out_contador_item_1, "maçã": out_contador_item_2, "laranja": out_contador_item_3}
  return out_dic_palavras


in_texto= "banana maçã banana laranja maçã maçã"

utils.cabecalho_exercicio('4) Contagem de Palavras')
print(contador_palavras(in_texto))
