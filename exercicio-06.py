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

d1 = {"a": 2, "b": 3, "c": 5, "e": 10}
d2 = {"a": 1, "b": 4, "d": 7, "x": 60}

#criar função passando por params 2 dicionarios
def combinar_dicts(in_dict_1: dict, in_dict_2: dict):
  #atribuir os valores do dict 1 ao novo dict
  proc_dict = in_dict_1

  #percorrer todos os items de dict 1 - declarar chave e valor próprios
  for k, v in in_dict_2.items():
    #verificar se chave de dict 1 e 2 são iguais
    if k in proc_dict.keys():
      #se forem, somar os valores das chaves 1 e 2 e atribuir ao novo dicto
      proc_dict[k] += v
    #se não forem iguais
    else:
      #atribuir valor referente a chave 2 ao novo dict
      proc_dict[k] = v
  #declarar var de saida do dict de saida reordenando pela chave
  out_dict = dict(sorted(proc_dict.items(), key= lambda item : item[0]))

  #retorno exibe no console o valor do novo dict
  return(print(out_dict))


utils.cabecalho_exercicio('6) Combinação de dicionários')
combinar_dicts(d1, d2)
utils.pular_linha()
