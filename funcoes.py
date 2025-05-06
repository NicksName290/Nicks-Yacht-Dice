#versao : 6
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista

def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    resposta = []
    dados_no_estoque.append(dados_rolados[dados_para_guardar])
    lista = []
    for a in range(dados_rolados-1):
      valor = random.randint(1 , 6)
      lista.append(valor)
    resposta.append(lista)
    resposta.append(dados_no_estoque)
    return resposta
    
