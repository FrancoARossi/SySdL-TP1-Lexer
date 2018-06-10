import time

def lexer(cadena):
	opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
	simbolos = ["(", ")", "{", "}", ",", ";", "+", "*", "-", "/"]
	tokens = []
	x = 0
	start = 0

	while start < len(cadena):
		acu = ""
		if cadena[start].isalpha():
			acu = acu + cadena[start]
			start+=1
			for x in range(start,len(cadena)):
				if cadena[x].isalpha():
					acu = acu + cadena[x]
				else:
					start = x
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
								tokens.append(("<ID>",acu))
		elif cadena[start].isdigit():
			acu = acu + cadena[start]
			start += 1
			for x in range(start,len(cadena)):
				if cadena[x].isdigit():
					acu = acu + cadena[x]
				else:
					start = x
					break
			tokens.append(("<Num>",acu))               # Aca ya sabemos que es un numero, asi que no llamamos al automata de num... ??
		elif cadena[start].isspace():
			start += 1
			pass      # No debe hacer nada, que siga con el siguiente caracter
		else:
			acu = acu + cadena [start]
			start += 1
			if acu in simbolos:
				pertenece = a_ParOpen(tokens,acu)
				if not pertenece:
					pertenece = a_ParClose(tokens,acu)
					if not pertenece:
						pertenece = a_BraOpen(tokens,acu)
						if not pertenece:
							pertenece = a_BraClose(tokens,acu)
							if not pertenece:
								pertenece = a_Comma(tokens,acu)
								if not pertenece:
									pertenece = a_PointComma(tokens,acu)
									if not pertenece:
										pertenece = a_Sum(tokens,acu)
										if not pertenece:
											pertenece = a_Minus(tokens,acu)
											if not pertenece:
												pertenece = a_Product(tokens,acu)
												if not pertenece:
													pertenece = a_Divide(tokens,acu)
			else:
				if (not cadena[start].isalpha()) and (not cadena[start].isdigit()) and (not cadena[start].isspace()):
					acu = acu + cadena[start]
					print(acu)
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
	print(tokens)
	time.sleep(5)


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
	if s==2:
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
	if s==2:
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

def a_Comma (tokens, acu):
    s = 0
    for c in acu:
        if c == ',':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<Comma>", acu))
    return (s == 1)

def a_PointComma (tokens, acu):
    s = 0
    for c in acu:
        if c == ';':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("<PointComma>", acu))
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

# Al finalizar el lexer deberia aceptar esta cadena
lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}")

# Habria que mandar un mensaje de error en este caso
# lexer("1 <( 2")
