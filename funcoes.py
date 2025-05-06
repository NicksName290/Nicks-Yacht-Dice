import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista

def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    resposta = []
    for i in dados_para_guardar:
        dados_no_estoque.append(dados_rolados[i])
    rolar = rolar_dados(len(dados_rolados)-len(dados_para_guardar))
    resposta.append(rolar)
    resposta.append(dados_no_estoque)
    return resposta
