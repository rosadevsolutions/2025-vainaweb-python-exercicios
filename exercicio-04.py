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

#crio a função com passgemn de parametro
def contador_palavras(in_str):
  #crio o dicionario a ser populado e exibido ao fim
  out_dict = {}

  # converto o param/string em list
  proc_list = in_str.split(', ')

  #itero a list
  for item in proc_list:
    #se não tiver o item na list entre as keys do dicionario
    if not item in out_dict.keys():
      #conto o item da list e atribuo ao dicionario
      out_dict[item] = proc_list.count(item)

  #retorno da função é a exibição do dicionario já populado
  return print(out_dict)


in_frutas = 'banana, pêra, maçã, morango, maçã, goiaba, morango, carambola, banana, pêra, morango'

utils.cabecalho_exercicio('4) Contagem de Palavras')
contador_palavras(in_frutas)
utils.pular_linha()


















































# def contador_palavras(texto):
#   proc_palavras = texto.split()

#   out_contador_item_1 = 0
#   out_contador_item_2 = 0
#   out_contador_item_3 = 0
#   out_dic_palavras = {}

#   for palavra in proc_palavras :
#     if(palavra == 'banana'):
#       out_contador_item_1 += 1
#     elif(palavra == 'maçã'):
#       out_contador_item_2 += 1
#     else:
#       out_contador_item_3 += 1

#   out_dic_palavras = {"banana": out_contador_item_1, "maçã": out_contador_item_2, "laranja": out_contador_item_3}
#   return out_dic_palavras


# in_texto= "banana maçã banana laranja maçã maçã"

# utils.cabecalho_exercicio('4) Contagem de Palavras')
# print(contador_palavras(in_texto))
