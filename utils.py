#Função pra criar separador
def separador():
  print(f'-' * 40)

#Função pra criar separador
def separador_titulo():
  print(f'=' * 40)

def pular_linha():
  print("\n")

#Função pra criar o cabeeçalho do exercício
def cabecalho_exercicio(titulo):
  pular_linha()
  separador_titulo()
  print(titulo.upper())
  separador_titulo()
