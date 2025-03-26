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
  for item in in_list:
    if item in proc_dict.keys():
      proc_dict[item] += 1
    else:
      proc_dict[item] = 1

  proc_dict_sorted = sorted(proc_dict.keys(), key=lambda v:(proc_dict[v], v), reverse=True)
  out_dict = proc_dict_sorted[:3]
  #out_dict = sorted( out_dict.keys(), key = lambda chave: (out_dict[chave], chave))
  return print(out_dict)

in_lista_numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

utils.cabecalho_exercicio("Top 3 mais frequentes")
verificar_top_3_frequentes(in_lista_numeros)
utils.pular_linha()
#Saída: [2, 1, 4]
