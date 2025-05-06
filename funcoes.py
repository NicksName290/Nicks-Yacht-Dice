#versao : 10
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#asdsasds
def guardar_dado(rolados, estoque, guardar):
    lista = []
    estoque.append(rolados[guardar])
    del dados_rolados[guardar]
    lista.append(rolados)
    lista.append(estoque)
    return lista

