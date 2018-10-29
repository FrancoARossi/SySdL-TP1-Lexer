from Lexer import lexer

VN = [ # No terminales
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


# Captura solo el token de la salida del Lexer e ignora el lexeme
def getTokenTypes(tokens):
	tokentypes = []
	for (token, lexeme) in tokens:
		tokentypes.append(token)
	return tokentypes

# Funcion principal
def parser(input):

	# Procesamiento de Producciones
	def Procesar(parte_derecha):
		print('Procesando ',parte_derecha)
		for simbolo in parte_derecha:
			print("Analizando simbolo", simbolo)
			if simbolo in variables["tokens"]:
				print(simbolo,' esta en los tokens')
				if (variables["tokens"][variables["pw"]] == simbolo):
					print('Y coincidio')
					variables["pw"] += 1
				else:
					print('Pero no coincidio, error = False')
					variables["error"] = True
					break
			elif (simbolo in VN):
				print(simbolo,' es un VN')
				i = VN.index(simbolo)
				print("pw", variables["pw"])
				PNi(i)
				if variables["error"]:
					print('Salio de procesar')
					break

	# Funcion para cada No terminal
	def PNi(i):
		print('Entro en PN',i,', osea, el PN de ',VN[i])
		variables["backtrack_pivot"] = variables["pw"]
		for parte_derecha in P[i]:
			print('Analizando ',parte_derecha,' de ',VN[i])
			print("pw", variables["pw"])
			variables["pw"] = variables["backtrack_pivot"]
			print("backtrack_pivot", variables["backtrack_pivot"])
			print("pw", variables["pw"])
			variables["error"] = False
			Procesar(parte_derecha)
			if variables["error"]:
				print('Salio de PN',i)
				break

	def finDeCadena():
		return (len(variables["tokens"]) - 1) == variables["pw"]

	tokens = lexer(input)
	tokens = getTokenTypes(tokens)
	print(tokens)
	variables = {
		"pw" : 0,
		"error" : False,
		"backtrack_pivot" : 0,
		"tokens" : tokens
	}
	PNi(0)
	if not variables["error"] and finDeCadena():
		return True
	else:
		return False


################################################################################
# Asserts
tests = [
			("int miFuncion(float a,int b){ for(c:=9, x := y,) a := 2+2;}", True),
			("float holi(int a, int b){ while( x := 20 := 11) ;}", True),
			("float far(int a, float b){ for( x := (2 + 3) + 20,,) ;}", True),
			("int miFuncion(float a,int b){ for(c:=5, x := y) a := 10+3;;}", False),
			("float a (:= 3 %~ ^^ ´ 2;)", False),
			("123abc", False),
			("a := 3 ++++ 2;", False),
			("float gatito(a > b);", False),
		]

assert parser(tests[0][0]) == tests[0][1]

# for (input, output) in tests:
# 	assert parser(input) == output
################################################################################
