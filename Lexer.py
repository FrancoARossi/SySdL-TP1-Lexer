opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
opMat = ["+", "*", "-", "/"]
simbolos = ["(", ")", "{", "}", ",", ";"]

def lexer(cadena):
	tokens = []
	i = 0
	cadena = cadena + " "
	
	while i<len(cadena):
		acu = ""
		if cadena[i].isalpha(): 
		#Es un caracter del alfabeto?
			acu = acu + cadena[i]
			i+=1
			for x in range(i,len(cadena)):
				if cadena[x].isalpha():
					acu = acu + cadena[x]
				else:
					i = x
					break
			if a_ErrorIDNum(tokens, acu, cadena, i):
				break
			evaluarAutomatasString(tokens,acu)
		elif cadena[i].isdigit():
	        # es un caracter numerico
			acu = acu + cadena[i]
			i+=1
			for x in range(i,len(cadena)):
				if cadena[x].isdigit():
					acu = acu + cadena[x]
				else:
					i = x
					break
			if a_ErrorNumID(tokens, acu, cadena, i):
				break
			a_Num(tokens,acu)
		elif cadena[i].isspace():
		#es un caracater del tipo espacio
			i+=1
		else:
			acu = acu + cadena[i]
			i += 1
			if (acu in opMat) or (acu in simbolos):
				if (acu in opMat) and (a_ErrorOpMat(tokens, acu, cadena, i)):
					break
				if (acu == "{") and (a_ErrorBraOpen(tokens, acu, cadena, i)):
					break
				if (acu == "}") and (a_ErrorBraClose(tokens, acu, cadena, i)):
					break
				evaluarAutomatasSimboloUnico(tokens,acu)
			else:
				if cadena[i]=="=":
					acu = acu + cadena[i]
					i+=1
				if a_ErrorInvalido (tokens, acu, cadena, i):
					break
				evaluarAutomatasSimbolosDobles(tokens,acu)
	return tokens

def evaluarAutomatasString(tokens,acu):
	if a_re1(tokens,acu):
		return
	if a_re2(tokens,acu):
		return
	if a_re3(tokens,acu):
		return
	if a_re4(tokens,acu):
		return
	if a_re5(tokens,acu):
		return
	if a_re6(tokens,acu):
		return
	a_ID(tokens,acu)


def evaluarAutomatasSimboloUnico(tokens,acu):
	if a_ParOpen(tokens,acu):
		return
	if a_ParClose(tokens,acu):
		return
	if a_BraOpen(tokens,acu):
		return
	if a_BraClose(tokens,acu):
		return
	if a_Coma(tokens,acu):
		return
	if a_PointComa(tokens,acu):
		return
	if a_Sum(tokens,acu):
		return
	if a_Minus(tokens,acu):
		return
	if a_Product(tokens,acu):
		return
	a_Divide(tokens,acu)

def evaluarAutomatasSimbolosDobles(tokens,acu):
	if a_OpRel1(tokens,acu):
		return
	if a_OpRel2(tokens,acu):
		return
	if a_OpRel3(tokens,acu):
		return
	if a_OpRel4(tokens,acu):
		return
	if a_OpRel5(tokens,acu):
		return
	if a_OpRel6(tokens,acu):
		return
	a_OpRel7(tokens,acu)

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

def a_ErrorIDNum (tokens, acu, cadena, i):
	error = False
	while cadena[i].isdigit():
		acu = acu + cadena[i]
		i += 1
		error = True
	if error:
		tokens.append(("<ErrorIDNum>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error

def a_ErrorNumID (tokens, acu, cadena, i):
	error = False
	while cadena[i].isalpha():
		acu = acu + cadena[i]
		i += 1
		error = True
	if error:
		tokens.append(("<ErrorNumID>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error

def a_ErrorOpMat (tokens, acu, cadena, i):
	error = False
	while cadena[i] in opMat:
		acu = acu + cadena[i]
		i += 1
		error = True
	if error:
		tokens.append(("<ErrorOpMat>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error

def a_ErrorBraOpen(tokens, acu, cadena, i):
	error = False
	if ((cadena[i-2] != ")") and (not cadena[i-2].isspace())):
		error = True
	if error:
		tokens.append(("<ErrorBraOpen>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error


def a_ErrorBraClose(tokens, acu, cadena, i):
	error = False
	if ((cadena[i] != "}") and (not cadena[i].isspace())):
		error = True
	if error:
		tokens.append(("<ErrorBraClose>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error

def a_ErrorInvalido (tokens, acu, cadena, i):
	error = False
	if (not acu in opLog):
		error = True
	if error:
		tokens.append(("<ErrorInvalido>", acu))
		for x in range(0,(len(tokens)-1)):
			del(tokens[0])
	return error

# Al finalizar el lexer debe aceptar estas cadenas
print(lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}"))
print('\n')
print(lexer("float miFuncion(int a,int b){ for(c:=9, x <= y) {while (3 == 3) {z := z+x}}}"))
print('\n')

#Esto desglosa la lista de tokens
prueba1=lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}")
for i in range(len(prueba1)):
	print (prueba1[i])

# Estas cadenas deben devolver un token de error
print(lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}error"))
print('\n')
print(lexer("int miFuncion(float a,int b)error{ for(c:=9, x <= y) a := 2+2;}"))
print('\n')
print(lexer("abc123"))
print('\n')
print(lexer("123abc"))
print('\n')
print(lexer("{1 := 2 ++2}"))
print('\n')
print(lexer("int a := 3, 4%"))

input("Pulse Enter para continuar")
