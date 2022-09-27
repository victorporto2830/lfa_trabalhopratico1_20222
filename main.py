import re

def Arquivo(arquivo):
  #Abre o arquivo em modo leitura
	arquivo = open(arquivo, "r")
	automato = []
	for linha in arquivo:
    #Adicionar cada linha do arquivo na lista
		automato.append(linha)
  #Fecha o arquivo
	arquivo.close()
  #Retrona a lista para serguirmos
	return automato

def PrimeiraLinhaLimpa(automato):
  #Pega a primeira linha da lista, que serão o alfabeto e estados (inicial e final)
	Primeira = automato[0]
	regex = re.compile(r'\{[^\}]*\}')
  #Pega os dados da primeira linha
	dados = re.findall(regex, Primeira)
	resultado = []
  #Adiciona os dados na lista
	for elemento in dados: 
		resultado.append(elemento.strip("{}").replace(" ", "").split(","))
	return resultado

def EstadoInicial(automato):
	Primeira = automato[0]
  #Pega o estado inicial na primera linha
	regex = re.compile(r"Z|,\sq\w*,\s{")
	dado = re.findall(regex, Primeira)
	EstadoInicio = [elemento.strip(",{ ") for elemento in dado]
	return EstadoInicio

def RegrasTransicao(automato):
	regras = []
  #Faz um loop dentro da lista automato para pegar os dados
	for i in range(1, len(automato)):
		automato[i] = automato[i].strip("\n").replace(" ", "").split(",")
		regras.append(automato[i])
	return regras

def LeituraPalavra(palavra, EstadoInicio, EstadoFinal, regras):
  #O esado inicial é o estado atual
	EstatadoAtual = EstadoInicio[0]
	i = 0
  #Faz um loop pra pegar letra por letra da palavra
	for letra in palavra:
		validacao = False
    #Faz o loop pra pegar regra por regra dentro da primeira letra
		for regra in regras:
      #Separa a linha de ragras em 3 variaveis
			RegraEstadoEntrada, RegraLetra, RegraEstadoSaida = regra
      #Testa regra por rega em cima da letra atual
			if (RegraEstadoEntrada == EstatadoAtual) and (RegraLetra == letra):
        #Printa o estado atual a palavra restante e o proximo estado
				print("(" + EstatadoAtual + ", " + palavra[i:] + ") = " + RegraEstadoSaida)
        #Se o estado atual for igual ao de confirmacao
				EstatadoAtual = RegraEstadoSaida
        #Valida
				validacao = True
        #Finaliza o loop
				break
		i += 1
    #Se nao houver validacao
		if not validacao:
			return False
  #Quando sair do loop FOR se o estado atual for o estado final
	if EstatadoAtual in EstadoFinal:
		return True
	else:
		return False

def Validado(alfabeto, estados, EstadoFinal, regras):
  #Se nao tiver estados
	if len(estados[0]) == 0:
		return False
  #Loop na lista estados
	for estado in EstadoFinal:
    #Se nao existir o estado final na lista
		if estado not in estados:
			return False
  #loop para testar regras
	for regra in regras:
		RegraEstadoEntrada, RegraLetra, RegraEstadoSaida = regra
    #Se a regra de entrada nao existir
		if RegraEstadoEntrada not in estados:
			return False
    #Se a regra de saida nao existir
		if RegraEstadoSaida not in estados:
			return False
	return True


automato = Arquivo(input("Arquivo:"))
palavra = input('Palavra: ')
#Pega dos dados da primeira linha da lista
dados = PrimeiraLinhaLimpa(automato)
#Busca estado inicial
EstadoInicio = EstadoInicial(automato)
#Le as regras para transicao
regras = RegrasTransicao(automato)
#Joga os dados nas variaveis
alfabeto = dados[0]
estados = dados[1]
EstadoFinal = dados[2]
#Testa se a palavra e valida ou nao
if Validado(alfabeto, estados, EstadoFinal, regras):
  print("Processamento: ")
  validade = LeituraPalavra(palavra, EstadoInicio, EstadoFinal, regras)
else:
  print("Arquivo invalido, tente novamente")
  
if validade == True: 
  print("\nPalavra Valida")
else:
  print("\nPalavra Invalida")  
