from Lexer.py import lexer

def parser(TokenTypes):
	error = False
	# la variable t (indice del token apuntado) es global
	t = 0
	PN1(t)
	if not error and finDeCadena(TokenTypes, t):
		return True
	else:
		return False

def PN1(pw):
	pass

def Procesar(produc, pw):
	pass

def finDeCadena(TokenTypes, t):
	#se compara TokenTypes(len(TokenTypes)) == lista[t]
	pass