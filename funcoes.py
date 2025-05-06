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
    rolar = rolar_dados(len(dados_rolados)-len(dados_para_guardar))
    resposta.append(rolar)
    resposta.append(dados_no_estoque)
    return resposta
#porque nn salva??
