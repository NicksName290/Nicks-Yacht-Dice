#Versao 7
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista

def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    novo_estoque = dados_no_estoque + [dados_rolados[dados_para_guardar]]
    rolar = rolar_dados(len(dados_rolados) - 1)
    return [rolar, novo_estoque]

    
