def lexer(cadena):
	opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
	OpMat = ["+", "*", "-", "/"]
	simbolos = ["(", ")", "{", "}", ",", ";"]
	tokens = []
	
	for i in len(cadena):
		acu = ""
		if cadena[i].isAlpha():
			acu = acu + cadena[i]
			start=i
			for x in range(start,len(cadena)):
				if cadena[x].isAlpha():
					acu = acu + cadena{x]
				else:
					i = x
					break
			# Aca mandamos automatas de palabras
		elif cadena[i].isDigit():
			acu = acu + cadena{i]
			for x in range(start,len(cadena)):
				if cadena[x].isDigit():
					acu = acu + cadena[x]
				else:
					i = x
					break
			tokens.append(("<Num>",acu) # Aca ya sabemos que es un numero, asi que no llamamos al automata de num... ??
		elif cadena{i].isSpace(): # No debe hacer nada, que siga con el siguiente caracter
		else:
			acu = acu + cadena [i]
			if acu in (OpMat or simbolos):
				# Aca mandamos los automatas de simbolos de un caracter
			else:
				i+=1
				acu = acu + cadena[i]
				# Aca mandamos los automatas de simbolos doble

def a_OpRel1(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c==':':
			s=1
		elif S==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpMat>",acu)
	return s==2

def a_OpRel2(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='<':
			s=1
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==1

def a_OpRel3(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='>':
			s=1
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==1


def a_OpRel4(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='<':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==2

def a_OpRel5(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='>':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==2
	
def a_OpRel6(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='!':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==2

def a_OpRel7(tokens, acu):
	s=0;
	for c in x:
		if s==0 and c=='=':
			s=1
		elif s==1 and c=='=':
			s=2
		else:
			s=-1
			break
	if s==2:
		tokens.append("<OpRel>",acu)
	return s==2