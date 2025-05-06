#versao : 6
import random
def rolar_dados(qnt):
  lista = []
  for a in range(qnt):
    valor = random.randint(1 , 6)
    lista.append(valor)
  return lista
#O github e uma bosta, eu ja poderia ter feito 20 exercicios desse 
#na porra do tempo que demora pra essa merda carregar a porra do arquivo correto
#porque caralhos essa merda ta instalando a versao de 1241209 anos atras
#tipo DA PRA VER QUE E A VERSAO CORRETA E SO DAR CNTR C CNTRL V
#EU TO A 1 HORA NOS EXERCICIOS MAIS FACEIS DO PLANETA POR CAUSA DESSA MERDA
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
    
