import random
def rolar_dados(qnt):
  lista = []
  i = 0
  random = 0
  while i != qnt:
    random = random.randit(1 , 6)
    lista.append(random)
  return lista
