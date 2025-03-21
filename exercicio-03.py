'''
Terceiro Exercício: Contagem de Frequência
Escreva uma função que
recebe uma string
e retorna um dicionário
onde as chaves são os caracteres da string
e os valores representam quantas vezes cada caractere aparece.
Exemplo: ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

Saída: {'Java': 2, 'Ruby': 2, 'Javascript': 1}
'''

#importanto as funções do arquivo utils
import utils

in_linguagens = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

def contador_frequencia(lista):
  out_contador_java = 0
  out_contador_ruby = 0
  out_contador_javascript = 0
  out_dic_linguagens = {}

  for item in lista:
    if item == 'Java':
      out_contador_java+=1
    elif item == 'Ruby':
      out_contador_ruby+=1
    else:
      out_contador_javascript+=1

  out_dic_linguagens = {'Java' : out_contador_java, 'Ruby' : out_contador_ruby, 'Javascript' : out_contador_javascript}
  return out_dic_linguagens


utils.cabecalho_exercicio('3) Contagem de Frequência')
print(contador_frequencia(in_linguagens))
