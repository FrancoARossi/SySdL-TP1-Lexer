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
	#No me cierra esta condicion de salida... en el algoritmo pone j <= k donde k es el numero de producciones de Ni
	# en este caso hay 1 sola produccion pero por como esta planteado el algoritmo cuando se llega al if por primera
	# vez j ya vale 2

	# esta bien que rompa ya que el procedimiento lo debe hacer solo una vez para PN1 (ya que tiene una sola produccion
	# el simbolo inicial)

	while (error and (j <= 1)):
		error = False
		Procesar(produ, pw, error)
		j += 1

# lo de la diapositiva no es un repetir hasta, es un while normal, ya que continua en el ciclo MIENTRAS
# se cumpla la condicion, lo que me parece raro es que en la condicion este error si negar, por lo que
# si llega con el valor por defecto (false) no va a entrar en el ciclo, deberiamos preguntar que onda eso.
# Para mi deberia ser while (not(error) and (j <= 1))

def Procesar(produ, pw, error):
	pass

def finDeCadena(TokenTypes, pw):
	#se compara TokenTypes(len(TokenTypes)) == lista[t]
	pass
