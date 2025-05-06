#Versao: 8
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#PELO AMOR ATUALIZA LOGOOO
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novo_estoque = dados_no_estoque + [dados_rolados[dado_para_guardar]]
    novos_dados = rolar_dados(len(dados_rolados) - 1)
    return [novos_dados, novo_estoque]
