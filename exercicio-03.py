'''
Terceiro Exercício: Contagem de Frequência
Escreva uma função que recebe uma string
e retorna um dicionário
onde as chaves são os caracteres da string
e os valores representam quantas vezes cada caractere aparece.
Exemplo: ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']

Saída: {'Java': 2, 'Ruby': 2, 'Javascript': 1}
'''

#importando as funções comuns criadas do arquivo utils
import utils

#declarar função passando um parametro
def contador_frequencia(in_str):
  #criar dicionário vazio para depois alimentar e exibir como resultado
  out_dict = {}

  #Param será uma string que será convertida em lista
  proc_list = in_str.split(' ')

  #iterar lista
  for item in proc_list:
    #verificar se o item não consta como chave no dicionario
    if not item in out_dict.keys():
      #contar o item de lista e atribuir ao dicionario
      out_dict[item] = proc_list.count(item)
  #exibir o dicionarioo
  return print(out_dict)

#string a passar como param quando chamar a função criada a cima
in_linguagens = 'Java Javascript Java Python C# Java Javascript Go Python Python Go'

utils.cabecalho_exercicio('3) Contagem de Frequência')
#chamando a função e passando o parametro
contador_frequencia(in_linguagens)
utils.pular_linha()
