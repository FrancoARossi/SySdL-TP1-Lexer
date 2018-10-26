from Lexer import lexer

VN = [
		"<Funcion>",
		"<ListaArgumentos>",
		"<Argumento>",
		"<Declaracion>",
		"<ListaIdent>",
		"<Sentencia>",
		"<SentFor>",
		"<SentWhile>",
		"<SentIf>",
		"<SentenciaCompuesta>",
		"<ListaSentencia>",
		"<Expr>",
		"<ValorR>",
		"<AuxVR>",
		"<Mag>",
		"<AuxM>",
		"<Termino>",
		"<AuxT>",
		"<Factor>"
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


#Captura solo el token de la salida del Lexer e ignora el lexeme
def getTokenTypes(tokens):
	tokentypes = []
	for (token, lexeme) in tokens:
		tokentypes.append(token)
	return tokentypes

def parser(input):
	global Tokens
	tokens = lexer(input)
	tokens = getTokenTypes(tokens)
	PNi(0)
	if not error and finDeCadena(Tokens, pw):
		return True
	else:
		return False
	
	def PNi(i):
	global error
	global pw
	backtrack_pivot = pw
	j = 0
	while (not error and ( j < len(P[i]))):
		pw = backtrack_pivot
		error = False
		Procesar(P[i][j])
		j += 1

	def Procesar(produ):
		global error
		global pw

		for simbolo in produ:
			if simbolo in tokens:
				if (tokens[pw] == produ[k]):
					pw += 1
				else:
					error = True
					break
			elif (produ[k] in VN):
				i = VN.index(produ[k])
				PNi(i)
				if error:
					break

#Se define un procedimiento recursivo indirecto a reutilizar con el argumento i


def finDeCadena(Tokens, pw):
	return (len(Tokens) - 1) == pw

################################################################################
# Asserts
 inputs = [
 			("int miFuncion(float a,int b){ for(c:=5, x := y) a := 10+3;;}", False),
 			("int miFuncion(float a,int b){ for(c:=9, x := y) a := 2+2;}", True),
 			("a := 3 %~ ^^ ´ 2;", True),
 			("123abc", True),
 			("a := 3 ++++ 2;", True),
 			("a := 3 -+/** 2;", True),
 			("a := 3 % 2;", True),
 			("abc123", True),
 			("float holi(int a, int b){ while( x := 20) ;}", True),
 			("float gatito(a > b);", True),
 		]

test = 7

for i in range(10):
	assert parser(inputs[i][1]) == inputs[i][2]
################################################################################
