'''
Sexto Exercício: Combinação de dicionários
Escreva uma função que recebe dois dicionários
onde as chaves são strings e os valores são inteiros.
A função deve combinar os dicionários
somando os valores das chaves que aparecem em ambos.
Exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
Saída: {"a": 3, "b": 7, "c": 5, "d": 7}
'''

#importanto as funções do arquivo utils
import utils

d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}

#criar função que passa por params 2 dicionarios
def combinar_dicionarios(in_dict_1, in_dict_2):
  #crio o dicionario para ser alimentado com a fusão
  proc_dict_3 = {}

  #somo os valores com chaves iguais e mesclando com os não repetidos
  proc_dict_3 = {k: in_dict_1.get(k, 0) + in_dict_2.get(k, 0) for k in set(in_dict_1) | set(in_dict_2)}

  #reordeno o dicionario pela chave
  out_dict_3_sorted = dict(sorted(proc_dict_3.items(), key= lambda item : item[0]))

  #retorno com a exibição no console do dicionario reordenado
  return print(out_dict_3_sorted)



utils.cabecalho_exercicio('6) Combinação de dicionários')
combinar_dicionarios(d1, d2)
utils.pular_linha()
