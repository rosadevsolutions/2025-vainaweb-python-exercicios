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

#criar função passando param/lista
def verificar_top_3_frequentes(in_list: list):
  #criar um dict pra contar alimentar com k,v
  proc_dict = {}

  #iterar o param
  for item in in_list:
    #verificar se o item consta entre as chaves da nova dict
    if item in proc_dict.keys():
      #se já houver a chace somar 1
      proc_dict[item] += 1
    #se não constar entre as chaves
    else:
      #apenas setar como 1
      proc_dict[item] = 1

  #variavel que recebe a lista ordenada com os valores decrescentes e exibindo as chaves
  proc_list_sorted = sorted(proc_dict.keys(), key=lambda v:(proc_dict[v], v), reverse=True)
  #variavel de saida com a lista acima com corte para exibir só 3 itens
  out_list = proc_list_sorted[:3]
  #retorno com a lista final
  return print(out_list)

in_lista_numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

utils.cabecalho_exercicio("Top 3 mais frequentes")
verificar_top_3_frequentes(in_lista_numeros)
utils.pular_linha()
