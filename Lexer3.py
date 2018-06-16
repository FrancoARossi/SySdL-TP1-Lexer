opLog = [':=', '<', '>', '>=', '<=', '!=', '==']
opMat = ['+', '*', '-', '/']
simbolos = ['(', ')', '{', '}', ',']

def lexer(src):
	tokens = []
	i = 0
	src = src + ' '
	error = False;
	while i < len(src):
		if not error:
			lexeme = ""
			#Es un caracter del alfabeto?
			if src[i].isalpha():
				#Lexeme acumula caracteres anteriores mas actuales
				lexeme = lexeme + src[i]
				i += 1
				#Aqui formula la cadena string
				for x in range(i, len(src)):
					if src[x].isalpha():#if3
						lexeme = lexeme + src[x]
						#Si el que le sige es un numero corto el ciclo
						#Ejemplo if3
						if src[x+1].isdigit():
							error = True
							break
					else:
						break
						i = x
				#fin de acumulacion lexeme
				if(evaluarAutomatasString(lexeme)):
					tokens.append(("Reservada", lexeme))
				else:
					tokens.append(("ID", lexeme))
			elif src[i].isdigit():
		        # es un caracter numerico
				lexeme = lexeme + src[i]
				i += 1
				for x in range(i, len(src)):
					if src[x].isdigit():
						lexeme = lexeme + src[x]
					else:
						i = x
						break
				if a_ErrorNumID(tokens, lexeme, src, i):
					break
				a_Num(lexeme)
			elif src[i].isspace():
			#es un caracater del tipo espacio
				i += 1
			else:
				lexeme = lexeme + src[i]
				i += 1
				if (lexeme in opMat) or (lexeme in simbolos):
					if (lexeme in opMat) and (a_ErrorOpMat(tokens, lexeme, src, i)):
						break
					if (lexeme == "{") and (a_ErrorBraOpen(tokens, lexeme, src, i)):
						break
					if (lexeme == "}") and (a_ErrorBraClose(tokens, lexeme, src, i)):
						break
					evaluarAutomatasSimboloUnico(lexeme)
				else:
					if src[i]=="=":
						lexeme = lexeme + src[i]
						i += 1
					if a_ErrorInvalido(tokens, lexeme, src, i):
						break
					evaluarAutomatasSimbolosDobles(lexeme)
		else:
			break

	return tokens

def evaluarAutomatasString(lexeme):
	if a_re1(lexeme) or a_re2(lexeme) or a_re3
		return True
	# if a_re2(lexeme):
	# 	return True
	# if a_re3(lexeme):
	# 	return True
	# if a_re4(lexeme):
	# 	return True
	# if a_re5(lexeme):
	# 	return True
	# if a_re6(lexeme):
	# 	return 'True'
	# if a_ID(lexeme):
	# 	return True


def evaluarAutomatasSimboloUnico(lexeme):
	if a_ParOpen(lexeme):
		return
	if a_ParClose(lexeme):
		return
	if a_BraOpen(lexeme):
		return
	if a_BraClose(lexeme):
		return
	if a_Comma(lexeme):
		return
	if a_SemiColon(lexeme):
		return
	if a_Sum(lexeme):
		return
	if a_Minus(lexeme):
		return
	if a_Product(lexeme):
		return
	a_Divide(lexeme)

def evaluarAutomatasSimbolosDobles(lexeme):
	if a_OpRel1(lexeme):
		return
	if a_OpRel2(lexeme):
		return
	if a_OpRel3(lexeme):
		return
	if a_OpRel4(lexeme):
		return
	if a_OpRel5(lexeme):
		return
	if a_OpRel6(lexeme):
		return
	a_OpRel7(lexeme)

def a_ID(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c.isalpha():
			s = 1
		elif s == 1 and c.isalpha():
			s = 1
		else:
			s = -1
			break
	if s == 1:
		tokens.append(("ID", lexeme))
	return s == 1

def a_Num(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c.isdigit():
			s = 1
		elif s == 1 and c.isdigit():
			s = 1
		else:
			s = -1
			break
	if s == 1:
		tokens.append(("Num", lexeme))
	return s == 1

def a_OpRel1(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == ':':
			s = 1
		elif s == 1 and c == '=':
			s = 2
		else:
			s = -1
			break
	if s == 2:
		tokens.append(("OpMat", lexeme))
	return s == 2

def a_OpRel2(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '<':
			s = 1
		else:
			s = -1
			break
	if s == 1:
		tokens.append(("OpRel", lexeme))
	return s == 1

def a_OpRel3(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '>':
			s = 1
		else:
			s = -1
			break
	if s == 1:
		tokens.append(("OpRel", lexeme))
	return s == 1


def a_OpRel4(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '<':
			s = 1
		elif s == 1 and c == '=':
			s = 2
		else:
			s = -1
	if s == 2:
		break
		tokens.append(("OpRel", lexeme))
	return s == 2

def a_OpRel5(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '>':
			s = 1
		elif s == 1 and c == '=':
			s = 2
		else:
			s = -1
			break
	if s == 2:
		tokens.append(("OpRel", lexeme))
	return s == 2

def a_OpRel6(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '!':
			s = 1
		elif s == 1 and c == '=':
			s = 2
		else:
			s = -1
			break
	if s == 2:
		tokens.append(("OpRel", lexeme))
	return s == 2

def a_OpRel7(lexeme):
	s = 0
	for c in lexeme:
		if s == 0 and c == '=':
			s = 1
		elif s == 1 and c == '=':
			s = 2
		else:
			s = -1
			break
	if s == 2:
		tokens.append(("OpRel", lexeme))
	return s == 2

def a_re1 (lexeme):
    s = 0
    for c in lexeme:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
        else:
            s = -1
            break
    return s == 3:

def a_re2 (lexeme):
    s = 0
    for c in lexeme:
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
        tokens.append(("Reservada", lexeme))
    return s == 5

def a_re3 (lexeme):
    s = 0
    for c in lexeme:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
        else:
            s = -1
            break
    if s == 2:
        tokens.append(("Reservada", lexeme))
    return s == 2

def a_re4 (lexeme):
    s = 0
    for c in lexeme:
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
        tokens.append(("Reservada", lexeme))
    return s == 4

def a_re5 (lexeme):
    s = 0
    for c in lexeme:
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
        tokens.append(("Reservada", lexeme))
    return s == 3

def a_re6 (lexeme):
    s = 0
    for c in lexeme:
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
        tokens.append(("Reservada", lexeme))
    return s == 5

def a_ParOpen (lexeme):
    s = 0
    for c in lexeme:
        if c == '(':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("ParOpen", lexeme))
    return (s == 1)

def a_ParClose (lexeme):
    s = 0
    for c in lexeme:
        if c == ')':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("ParClose", lexeme))
    return s == 1

def a_BraOpen (lexeme):
    s = 0
    for c in lexeme:
        if c == '{':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("BraOpen", lexeme))
    return (s == 1)

def a_BraClose (lexeme):
    s = 0
    for c in lexeme:
        if c == '}':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("BraClose", lexeme))
    return s == 1

def a_Comma (lexeme):
    s = 0
    for c in lexeme:
        if c == ',':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("Comma", lexeme))
    return s == 1

def a_SemiColon (lexeme):
    s = 0
    for c in lexeme:
        if c == ';':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("SemiColon", lexeme))
    return s == 1

def a_Sum (lexeme):
    s = 0
    for c in lexeme:
        if c == '+':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("OpMat", lexeme))
    return s == 1

def a_Minus (lexeme):
    s = 0
    for c in lexeme:
        if c == '-':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("OpMat", lexeme))
    return s == 1

def a_Product (lexeme):
    s = 0
    for c in lexeme:
        if c == '*':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("OpMat", lexeme))
    return s == 1

def a_Division (lexeme):
    s = 0
    for c in lexeme:
        if c == '/':
            s = 1
        else:
            s = -1
    if s == 1:
        tokens.append(("OpMat", lexeme))
    return s == 1

def a_ErrorIDNum (tokens, lexeme, src, i):
	error = False
	while src[i].isdigit():
		lexeme = lexeme + src[i]
		i += 1
		error = True
	if error:
		tokens.append(("ErrorIDNum", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error

def a_ErrorNumID (tokens, lexeme, src, i):
	error = False
	while src[i].isalpha():
		lexeme = lexeme + src[i]
		i += 1
		error = True
	if error:
		tokens.append(("ErrorNumID", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error

def a_ErrorOpMat (tokens, lexeme, src, i):
	error = False
	while src[i] in opMat:
		lexeme = lexeme + src[i]
		i += 1
		error = True
	if error:
		tokens.append(("ErrorOpMat", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error

def a_ErrorBraOpen(tokens, lexeme, src, i):
	error = False
	if (src[i-2] != ")") and (not src[i-2].isspace()):
		error = True
	if error:
		tokens.append(("ErrorBraOpen", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error


def a_ErrorBraClose(tokens, lexeme, src, i):
	error = False
	if (src[i] != "}") and (not src[i].isspace()):
		error = True
	if error:
		tokens.append(("ErrorBraClose", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error

def a_ErrorInvalido (tokens, lexeme, src, i):
	error = False
	if (not lexeme in opLog):
		error = True
	if error:
		tokens.append(("ErrorInvalido", lexeme))
		for x in range(0, len(tokens) - 1):
			del(tokens[0])
	return error

# Al finalizar el lexer debe aceptar estas srcs
print(lexer("int miFuncion(float a,int b){ for(c:=9, x = y) a := 2+2}"))
print('\n')
print(lexer("float miFuncion(int a,int b){ for(c:=9, x <= y) {while (3 == 3) {z := z+x}}}"))
print('\n')

# Estas srcs deben devolver un token de error
print(lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2}error"))
print('\n')
print(lexer("int miFuncion(float a,int b)error{ for(c:=9, x <= y) a := 2+2}"))
print('\n')
print(lexer("abc123"))
print('\n')
print(lexer("123abc"))
print('\n')
print(lexer("{1 := 2 ++2}"))
print('\n')
print(lexer("int a := 3, 4%"))
print('\n')
"if( x == 'x3') "
