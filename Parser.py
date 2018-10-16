from Lexer.py import lexer

def parser(TokenTypes):
	error = False
	# la variable t (indice del token apuntado) es global
	pw = 0
	PN1(t, error)
	if not error and finDeCadena(TokenTypes, pw):
		return True
	else:
		return False

def PN1(pw, error):
	j = 1
	# Python no tiene un ciclo del tipo Repetir-Hasta, hay que usar un while true con un if como condicion de salida
	while True:
		error = False
		Procesar(produ, pw, error)
		j += 1
		#No me cierra esta condicion de salida... en el algoritmo pone j <= k donde k es el numero de producciones de Ni
		# en este caso hay 1 sola produccion pero por como esta planteado el algoritmo cuando se llega al if por primera
		# vez j ya vale 2 
		if error and (j <= 1):
			break


def Procesar(produ, pw, error):
	pass

def finDeCadena(TokenTypes, pw):
	#se compara TokenTypes(len(TokenTypes)) == lista[t]
	pass