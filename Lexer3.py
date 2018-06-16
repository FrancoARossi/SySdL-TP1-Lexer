opLog = [':=', '<', '>', '>=', '<=', '!=', '==']
opMat = ['+', '*', '-', '/']
simbolos = ['(', ')', '{', '}', ',']

def lexer(src):
	tokens = []
	src = src + ' '
	i = 0
	start = 0
	state = 0
	
	while i < len(src) :
		c = src[i]
		word = src[start:i+1]
		if state == 0 :
			if c.isspace():
				i += 1
				state = 0
			else:
				start = i
				state = 1
		elif state == 1 :
			if (es_aceptado(word) and not c.isspace()) :
				i += 1
				state = 1
			else:
				i -= 1
				state = 2
		elif state == 2 :
			candidatos = evaluar(word)
			tokentype = candidatos[0]
			tokens.append((tokentype, word))
			i += 1
			state = 0
	return tokens
				
def es_aceptado(word):
	candidatos = []
	for (token, afd) in TT :
		if afd(word) :
			candidatos.append(token)		
	if len(candidatos) > 0 :
		return True
	else:
		return False

def evaluar(word):
	candidatos = []
	for (token,afd) in TT :
		if afd(word) :
			candidatos.append(token)
	return candidatos

def a_ID(word):
	s=0
	for c in word:
		if s==0 and c.isalpha():
			s=1
		elif s==1 and c.isalpha():
			s=1
		else:
			s=-1
			break
	return (s != -1)

def a_Num(word):
	s=0
	for c in word:
		if s == 0 and c.isdigit():
			s = 1
		elif s == 1 and c.isdigit():
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_OpRel1(word):
	s=0;
	for c in word:
		if s==0 and c==':':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	return (s != -1)

def a_OpRel2(word):
	s=0;
	for c in word:
		if s==0 and c=='<':
			s=1
		else:
			s=-1
			break
	return (s != -1)

def a_OpRel3(word):
	s=0;
	for c in word:
		if s==0 and c=='>':
			s=1
		else:
			s=-1
			break
	return (s != -1)


def a_OpRel4(word):
	s=0;
	for c in word:
		if s==0 and c=='<':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	return (s != -1)

def a_OpRel5(word):
	s=0;
	for c in word:
		if s==0 and c=='>':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	return (s != -1)
	
def a_OpRel6(word):
	s=0;
	for c in word:
		if s==0 and c=='!':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	return (s != -1)

def a_OpRel7(word):
	s=0;
	for c in word:
		if s==0 and c=='=':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	return (s != -1)

def a_re1 (word):
	s = 0
	for c in word:
		if s == 0 and c == 'i':
			s = 1
		elif s == 1 and c == 'n':
			s = 2
		elif s == 2 and c == 't':
			s = 3
		else:
			s = -1
			break
	return (s != -1)

def a_re2 (word):
	s = 0
	for c in word:
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
	return (s != -1)

def a_re3 (word):
	s = 0
	for c in word:
		if s == 0 and c == 'i':
			s = 1
		elif s == 1 and c == 'f':
			s = 2
		else:
			s = -1
			break
	return (s != -1)

def a_re4 (word):
	s = 0
	for c in word:
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
	return (s != -1)

def a_re5 (word):
	s = 0
	for c in word:
		if s == 0 and c == 'f':
			s = 1
		elif s == 1 and c == 'o':
			s = 2
		elif s == 2 and c == 'r':
			s = 3
		else:
			s = -1
			break
	return (s != -1)

def a_re6 (word):
	s = 0
	for c in word:
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
	return (s != -1)

def a_ParOpen (word):
	s = 0
	for c in word:
		if c == '(':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_ParClose (word):
	s = 0
	for c in word:
		if c == ')':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_BraOpen (word):
	s = 0
	for c in word:
		if c == '{':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_BraClose (word):
	s = 0
	for c in word:
		if c == '}':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_Comma (word):
	s = 0
	for c in word:
		if c == ',':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_SemiColon (word):
	s = 0
	for c in word:
		if c == ';':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_Sum (word):
	s = 0
	for c in word:
		if c == '+':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_Minus (word):
	s = 0
	for c in word:
		if c == '-':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_Product (word):
	s = 0
	for c in word:
		if c == '*':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

def a_Division (word):
	s = 0
	for c in word:
		if c == '/':
			s = 1
		else:
			s = -1
			break
	return (s != -1)

TT = [("int", a_re1), ("float", a_re2), ("if", a_re3), ("else",a_re4),
	 ("for", a_re5), ("while", a_re6), ("ID", a_ID), ("Num", a_Num), (":=", a_OpRel1),
	 ("<", a_OpRel2), (">", a_OpRel3), ("<=", a_OpRel4),
	 (">=", a_OpRel5), ("!=", a_OpRel6), ("==", a_OpRel7),
	 ("(", a_ParOpen), (")", a_ParClose),
	 ("{", a_BraOpen), ("}", a_BraClose), (",", a_Comma), (";", a_SemiColon),
	 ("+", a_Sum), ("-" ,a_Minus), ("*", a_Product), ("/", a_Division)]
	 # ("errorIDNum", a_ErrorIDNum), ("errorNumID", a_ErrorNumID), ("errorOpMat", a_ErrorOpMat),
	 # ("errorBraOpen", a_ErrorBraOpen), ("errorBraClose", a_ErrorBraClose), ("errorInvalido", a_ErrorInvalido)]

# Estas srcs deben devolver un token de error
prueba1 = lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2}")
print(prueba1)
prueba = lexer("int for abc")
for i in range(len(prueba)):
 	print (prueba[i])
# Exit Debug