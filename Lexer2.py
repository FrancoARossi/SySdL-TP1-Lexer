opLog = [':=', '<', '>', '>=', '<=', '!=', '==']
opMat = ['+', '*', '-', '/']
simbolos = ['(', ')', '{', '}', ',']

def lexer(src):
    tokens = []
    i = 0
    text = src + ' '

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
			break
	if s == 2:
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
    if s == 3:
        tokens.append(("Reservada", lexeme))
    return s == 3

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

TT = [("ID", a_ID(lexeme)), ("Num", a_Num(lexeme)), (":=", a_OpRel1(lexeme)),
	 ("<", a_OpRel2(lexeme)), (">", a_OpRel3(lexeme)), ("<=", a_OpRel4(lexeme)),
	 (">=", a_OpRel5(lexeme)), ("!=", a_OpRel6(lexeme)), ("==", a_OpRel7(lexeme)),
	 ("int", a_re1(lexeme)), ("float", a_re2(lexeme)), ("if", a_re3(lexeme)), ("else",a_re4(lexeme)),
	 ("for", a_re5(lexeme)), ("while", a_re6(lexeme)), ("(", a_ParOpen(lexeme)), (")", a_ParClose(lexeme)),
	 ("{", a_BraOpen(lexeme)), ("}", a_BraClose(lexeme)), (",", a_Comma(lexeme)), (";", a_SemiColon(lexeme)),
	 ("+", a_Sum(lexeme)), ("-" ,a_Minus(lexeme)), ("*", a_Product(lexeme)), ("/", a_Division(lexeme)),
	 ("errorIDNum", a_ErrorIDNum(lexeme)), ("errorNumID", a_ErrorNumID(lexeme)), ("errorOpMat", a_ErrorOpMat(lexeme)),
	 ("errorBraOpen", a_ErrorBraOpen(lexeme)), ("errorBraClose", a_ErrorBraClose(lexeme)), ("errorInvalido", a_ErrorInvalido(lexeme))]

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
