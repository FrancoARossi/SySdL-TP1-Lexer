import time

def lexer(cadena):
	opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
	opMat = ["+", "*", "-", "/"]
	simbolos = ["(", ")", "{", "}", ",", ";"]
	tokens = []
	i = 0
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	aceptada = True
=======
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
	cadena = cadena + " "
		
	while i<len(cadena):
		acu = ""
		if cadena[i].isalpha():
			acu = acu + cadena[i]
			i+=1
			for x in range(i,len(cadena)):
				if cadena[x].isalpha():
					acu = acu + cadena[x]
				else:
					i = x
					if cadena[i].isdigit():
						print("### Esta gramatica no es aceptada ###")
						time.sleep(2)
						aceptada = False
						break
					break
			if not aceptada:
				break
			pertenece = a_re1(tokens,acu)
			if not pertenece:
				pertenece = a_re2(tokens,acu)
				if not pertenece:
					pertenece = a_re3(tokens,acu)
					if not pertenece:
						pertenece = a_re4(tokens,acu)
						if not pertenece:
							pertenece = a_re5(tokens,acu)
							if not pertenece:
								pertenece = a_re6(tokens,acu)
								if not pertenece:
									pertenece = a_ID(tokens,acu)
		elif cadena[i].isdigit():
			acu = acu + cadena[i]
			i+=1
			for x in range(i,len(cadena)):
				if cadena[x].isdigit():
					acu = acu + cadena[x]
				else:	
					i = x
					if cadena[i].isalpha():
						print("### Esta gramatica no es aceptada ###")
						time.sleep(2)
						aceptada = False
						break
					break
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
			if not aceptada:
				break
			a_Num(tokens, acu)
=======
			a_Num(tokens,acu)
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
			a_Num(tokens,acu)
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
			a_Num(tokens,acu)
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
		elif cadena[i].isspace():
			i+=1
		else:
			acu = acu + cadena[i]
			if (acu in opMat) or (acu in simbolos):
				i+=1
				if ((acu in opMat) and ((cadena[i] in opMat) or (cadena[i] in opLog) or (cadena[i] in simbolos))):
					print("### Esta gramatica no es aceptada ###")
					time.sleep(2)
					aceptada = False
					break
				if (((acu == "{") or (acu == "}")) and ((cadena[i].isdigit()) or (cadena[i] in opMat) or (cadena[i] in opLog))):
					print("### Esta gramatica no es aceptada ###")
					time.sleep(2)
					aceptada = False
					break
				pertenece = a_ParOpen(tokens,acu)
				if not pertenece:
					pertenece = a_ParClose(tokens,acu)
					if not pertenece:
						pertenece = a_BraOpen(tokens,acu)
						if not pertenece:
							pertenece = a_BraClose(tokens,acu)
							if not pertenece:
								pertenece = a_Coma(tokens,acu)
								if not pertenece:
									pertenece = a_PointComa(tokens,acu)
									if not pertenece:
										pertenece = a_Sum(tokens,acu)
										if not pertenece:
											pertenece = a_Minus(tokens,acu)
											if not pertenece:
												pertenece = a_Product(tokens,acu)
												if not pertenece:
													pertenece = a_Divide(tokens,acu)
			else:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
				i+=1
				if cadena[i] == "=":
=======
				if cadena[i]=="=":
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
				if cadena[i]=="=":
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
				if cadena[i]=="=":
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
					acu = acu + cadena[i]
					i+=1
				if ((not acu in opLog) or (cadena[i] in simbolos)):
						print("### Esta gramatica no es aceptada ###")
						time.sleep(2)
						aceptada = False
						break
				pertenece = a_OpRel1(tokens,acu)
				if not pertenece:
					pertenece = a_OpRel2(tokens,acu)
					if not pertenece:
						pertenece = a_OpRel3(tokens,acu)
						if not pertenece:
							pertenece = a_OpRel4(tokens,acu)
							if not pertenece:
								pertenece = a_OpRel5(tokens,acu)
								if not pertenece:
									pertenece = a_OpRel6(tokens,acu)
									if not pertenece:
										pertenece = a_OpRel7(tokens,acu)
	if aceptada:
		print(tokens)
		time.sleep(2)

def a_ID(tokens, acu):
	s=0
	for c in acu:
		if s==0 and c.isalpha():
			s=1
		elif s==1 and c.isalpha():
			s=1
		else:
			s=-1
			break
	if s==1:
		tokens.append(("<ID>",acu))
	return s==1

def a_Num(tokens, acu):
	s=0
	for c in acu:
		if s==0 and c.isdigit():
			s=1
		elif s==1 and c.isdigit():
			s=1
		else:
			s=-1
			break
	if s==1:
		tokens.append(("<Num>",acu))
	return s==1

def a_OpRel1(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c==':':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append(("<OpMat>",acu))
	return s==2

def a_OpRel2(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='<':
			s=1
		else:
			s=-1
			break
	if s==1:
		tokens.append(("<OpRel>",acu))
	return s==1

def a_OpRel3(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='>':
			s=1
		else:
			s=-1
			break
	if s==1:
		tokens.append(("<OpRel>",acu))
	return s==1


def a_OpRel4(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='<':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append(("<OpRel>",acu))
	return s==2

def a_OpRel5(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='>':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append(("<OpRel>",acu))
	return s==2
	
def a_OpRel6(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='!':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append(("<OpRel>",acu))
	return s==2

def a_OpRel7(tokens, acu):
	s=0;
	for c in acu:
		if s==0 and c=='=':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append(("<OpRel>",acu))
	return s==2

def a_re1 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
        else:
            s = -1
            break
    if s == 3:
        tokens.append(("<Reservada>", acu))
    return (s == 3)

def a_re2 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'l':
            s = 2
        elif s == 2 and c == 'o':
            s = 3
        elif s == 3 and c == 'a':
            s = 4
        elif s == 4 and c == 't':
            s = 5
        else:
            s = -1
            break
    if s == 5:
        tokens.append(("<Reservada>", acu))
    return (s == 5)

def a_re3 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
        else:
            s = -1
            break
    if s == 2:
        tokens.append(("<Reservada>", acu))
    return (s == 2)

def a_re4 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'e':
            s = 1
        elif s == 1 and c == 'l':
            s = 2
        elif s == 2 and c == 's':
            s = 3
        elif s == 3 and c == 'e':
            s = 4
        else:
            s = -1
            break
    if s == 4:
        tokens.append(("<Reservada>", acu))
    return (s == 4)

def a_re5 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'o':
            s = 2
        elif s == 2 and c == 'r':
            s = 3
        else:
            s = -1
            break
    if s == 3:
        tokens.append(("<Reservada>", acu))
    return (s == 3)

def a_re6 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'w':
            s = 1
        elif s == 1 and c == 'h':
            s = 2
        elif s == 2 and c == 'i':
            s = 3
        elif s == 3 and c == 'l':
            s = 4
        elif s == 4 and c == 'e':
            s = 5
        else:
            s = -1
            break
    if s == 5:
        tokens.append(("<Reservada>", acu))
    return (s == 5)

def a_ParOpen (tokens, acu):
    s = 0
    for c in acu:
        if c == '(':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<ParOpen>", acu))
    return (s == 1)

def a_ParClose (tokens, acu):
    s = 0
    for c in acu:
        if c == ')':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<ParClose>", acu))
    return (s == 1)

def a_BraOpen (tokens, acu):
    s = 0
    for c in acu:
        if c == '{':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<BraOpen>", acu))
    return (s == 1)

def a_BraClose (tokens, acu):
    s = 0
    for c in acu:
        if c == '}':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<BraClose>", acu))
    return (s == 1)

def a_Coma (tokens, acu):
    s = 0
    for c in acu:
        if c == ',':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<Comma>", acu))
    return (s == 1)

def a_PointComa (tokens, acu):
    s = 0
    for c in acu:
        if c == ';':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<SemiColon>", acu))
    return (s == 1)

def a_Sum (tokens, acu):
    s = 0
    for c in acu:
        if c == '+':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<OpMat>", acu))
    return (s == 1)

def a_Minus (tokens, acu):
    s = 0
    for c in acu:
        if c == '-':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<OpMat>", acu))
    return (s == 1)

def a_Product (tokens, acu):
    s = 0
    for c in acu:
        if c == '*':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<OpMat>", acu))
    return (s == 1)

def a_Division (tokens, acu):
    s = 0
    for c in acu:
        if c == '/':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<OpMat>", acu))
    return (s == 1)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
### Pruebas ###

# Al finalizar el lexer deberia aceptar esta cadena y mostrar la lista de Tokens
lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}")
lexer("float miFuncion(int a,int b){ for(c:=9, x <= y) {while (3 == 3) {z := z+x}}}")

# Estas cadenas no deben ser aceptadas
lexer("1 <( 2")
lexer("int miFuncion(float a,int b){2 }")
lexer("123for")
lexer("for123")
lexer("2 ]+) a")
=======
=======
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
# Al finalizar el lexer deberia aceptar esta cadena
lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;} int")

# Habria que mandar un mensaje de error en este caso
# lexer("1 <( 2")
<<<<<<< HEAD
<<<<<<< HEAD
# Esto lo podria generar la gramatica? El lexer los debería reconocer por separado ya que no toma en cuenta espacios
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
# Esto lo podria generar la gramatica? El lexer los debería reconocer por separado ya que no toma en cuenta espacios
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
=======
# Esto lo podria generar la gramatica? El lexer los debería reconocer por separado ya que no toma en cuenta espacios
>>>>>>> 81ae25dc114764c6d1ab4afc77c43007f042f089
