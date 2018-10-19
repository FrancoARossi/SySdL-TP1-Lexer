from Lexer import lexer

error = False
Tokens = []

VN = [
		"<Funcion>", "<ListaArgumentos>", "<Argumento>", "<Declaracion>", "<ListaIdent>", "<Sentencia>", "<SentFor>", "<SentWhile>", "<SentIf>", "<SentenciaCompuesta>", "<ListaSentencia>", "<Expr>", "<ValorR>", "<AuxVR>", "<Mag>", "<AuxM>", "<Termino>", "<AuxT>", "<Factor>"
	]

P = [ # Producciones
		[ # <Funcion>
			[
				"Reservada", "ID", "ParOpen", "<ListaArgumentos>", "ParClose", "<SentenciaCompuesta>"
			]
		],
		[ # <ListaArgumentos>
			[
				"<Argumento>"
			],
			[
				"<Argumento>", "Comma", "<ListaArgumentos>"
			]
		],
		[ # <Argumento>
			[
				"Reservada", "ID"
			]
		],
		[ # <Declaracion>
			[
				"Reservada", "<ListaIdent>", "SemiColon"
			]
		],
		[ # <ListaIdent>
			[
				"ID", "Comma", "<ListaIdent>"
			],
			[
				"ID"
			]
		],
		[ # <Sentencia>
			[
				"<SentFor>"
			],
			[
				"<SentWhile>"
			],
			[
				"<Expr>", "SemiColon"
			],
			[
				"<SentIf>"
			],
			[
				"<SentenciaCompuesta>"
			],
			[
				"<Declaracion>"
			],
			[
				"SemiColon"
			]
		],
		[ # <SentFor>
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "<Expr>", "Comma", "<Expr>", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "Comma", "<Expr>", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "<Expr>", "Comma", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "Comma"," ParClose", "<Sentencia>"
			]
		],
		[ # <SentWhile>
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>"
			]
		],
		[ # <SentIf>
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>", "Reservada", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>"
			]
		],
		[ # <SentenciaCompuesta>
			[
				"BraOpen", "<ListaSentencia>", "BraClose"
			]
		],
		[ # <ListaSentencia>
			[
				"<Sentencia>", "<ListSentencia>"
			],
			[
				"<Sentencia>"
			]
		],
		[ # <Expr>
			[
				"ID", "OpRel", "<Expr>"
			],
			[
				"<ValorR>"
			]
		],
		[ # <ValorR>
			[
				"<Mag>", "<AuxVR>"
			],
			[
				"<Mag>"
			]
		],
		[ # <AuxVR>
			[
				"OpRel", "<Mag>", "<AuxVR>"
			],
			[
				"OpRel", "<Mag>"
			]
		],
		[ # <Mag>
			[
				"<Termino>", "<AuxM>"
			],
			[
				"<Termino>"
			]
		],
		[ # <AuxM>
			[
				"OpMat", "<Termino>", "<AuxM>"
			],
			[
				"OpMat", "<Termino>"
			]
		],
		[ # <Termino>
			[
				"<Factor>", "<AuxT>"
			],
			[
				"<Factor>"
			]
		],
		[ # <AuxT>
			[
				"OpMat", "<Termino>", "<AuxT>"
			],
			[
				"OpMat", "<Termino>"
			]
		],
		[ # <Factor>
			[
				"ParOpen", "<Expr>", "ParClose"
			],
			[
				"OpMat", "<Factor>"
			],
			[
				"OpMat", "<Factor>"
			],
			[
				"Num"
			],
			[
				"ID"
			]
		]
	]


#Captura solo el token de la salida del Lexer e ignora el lexema
def tratamientoTokens(Input):
	tokens = []
	for (a,b) in Input:
		tokens.append(a)
	return tokens

def parser(Input):
	global Tokens
	Tokens = lexer(Input)
	Tokens = tratamientoTokens(Tokens)
	print(Tokens)
	print("")
	pw = 0
	PNi(0, pw)
	if not(error) and finDeCadena(Tokens, pw):
		return True
	else:
		return False

#Se define un procedimiento recursivo indirecto a reutilizar con el argumento i
def PNi(i, pw):
	global error
	backtrack_pivot = pw
	j = 0
	while (not error and ( j < len(P[i]))):
		pw = backtrack_pivot
		error = False
		print(P[i][j])
		Procesar(P[i][j], pw)
		j += 1

def Procesar(produ, pw):
	global error

	#esto solo lo resuelve para PN1, creo que deberiamos pasar como parametro que VN estamos evaluando
	for k in range(0, len(produ)):
		if (produ[k] in Tokens):
			if (Tokens[pw] == produ[k]):
				pw += 1
				print("Token == produ[k]:", produ[k])
			else:
				error = True
				break
		elif (produ[k] in VN):
			print("Token in VN:", produ[k])
			i = VN.index(produ[k])
			PNi(i, pw)
			if error:
				break

def finDeCadena(Tokens, pw):
	return (len(Tokens) - 1) == pw

################################################################################
# Asserts
inputs = [
			["int miFuncion(float a,int b){ for(c:=5, x := y) a := 10+3;;}", False],
			["int miFuncion(float a,int b){ for(c:=9, x := y) a := 2+2;}", True],
			["a := 3 %~ ^^ ´ 2;", True],
			["123abc", True],
			["a := 3 ++++ 2;", True],
			["a := 3 -+/** 2;", True],
			["a := 3 % 2;", True],
			["abc123", True],
			["float holi(int a, int b){ while( x := 20) ;}", True],
			["float gatito(a > b);" True],
		]

test = 7
assert parser(inputs[test][1])) == inputs[test][2]

# for i in range(10):
# 	assert parser(inputs[i][1]) == inputs[i][2]
################################################################################
