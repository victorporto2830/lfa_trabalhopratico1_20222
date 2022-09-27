def Arquivo(arquivo): 
  #Abre o arquivo em modo leitura
	arquivo = open(arquivo, "r")
	automato = []
	for linha in arquivo:
    #Adicionar cada linha do arquivo na lista
		automato.append(linha.strip("\n").replace(" ", "").split(","))
  #Fecha o arquivo
	arquivo.close()
  #Retrona a lista para serguirmos
	return automato

def dados(automato):
	automa = {}
	chave = ''
	for li in automato:
		if (li[0] == '#states'):
			chave = 'states'
			automa[chave] = []
			continue
		elif (li[0] == '#initial'):
			chave = 'initial'
			automa[chave] = []
			continue

		elif (li[0] == '#accepting'):
			chave = 'accepting'
			automa[chave] = []
			continue

		elif (li[0] == '#alphabet'):
			chave = 'alphabet'
			automa[chave] = []
			continue

		elif (li[0] == '#transitions'):
			chave = 'transitions'
			automa[chave] = []
			continue
    
		automa[chave].append(li[0])

	return automa

def LeituraPalavra(palavra, EstadoInicio, EstadoFinal, regras):
  #O esado inicial é o estado atual
	EstatadoAtual = EstadoInicio[0]
	i = 0
  #Faz um loop pra pegar letra por letra da palavra
	for letra in palavra:
		validacao = False
    #Faz o loop pra pegar regra por regra dentro da primeira letra
		for regra in regras:
			regra = regra.replace(">", ":")
			regra = regra.replace(',', ':')
			regra = regra.split(':')
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
		regra = regra.replace(">", ":")
		regra = regra.replace(',', ':')
		regra = regra.split(':')
		RegraEstadoEntrada, RegraLetra, RegraEstadoSaida = regra
    #Se a regra de entrada nao existir
		if RegraEstadoEntrada not in estados:
			return False
    #Se a regra de saida nao existir
		if RegraEstadoSaida not in estados:
			return False
	return True


automato = Arquivo(input("Arquivo: "))
palavra = input("Palavra: ")
#Pega dos dados da primeira linha da lista
dados = dados(automato)
#Busca estado inicial
EstadoInicio = dados['initial']
#Le as regras para transicao
regras = dados['transitions']
#Joga os dados nas variaveis
alfabeto = dados['alphabet']
estados = dados['states']
EstadoFinal = dados['accepting']
#Printa as informações
print("\nAlfabeto: {}".format(alfabeto))
print("Estados: {}".format(estados))
print("Estado Inicial: {}".format(EstadoInicio))
print("Estado Final: {}".format(EstadoFinal))
print("Regras de Transição: ")
for regra in regras:
  print(regra)
print()
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
