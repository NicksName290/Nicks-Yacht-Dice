#versao : 10
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#asdsasds
def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    lista = []
    dados_no_estoque.append(dados_rolados[dados_para_guardar])
    del dados_no_estoque[dados_para_guardar]
    lista.append(dados_rolados)
    lista.append(dados_no_estoque)
    return lista
