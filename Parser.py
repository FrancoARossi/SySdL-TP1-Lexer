from Lexer import lexer

terminales = [ # Terminales
		'ParOpen',
		'ParClose',
		'BraOpen',
		'BraClose',
		'OpMat',
		'ID',
		'Num',
		'Reservada',
		'Comma',
		'SemiColon',
		'OpRel'
	  ]

no_terminales = [ # No terminales
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

producciones = [ # Producciones
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
# def getTokenTypes(tokens):
# 	tokentypes = []
# 	for (token, lexeme) in tokens:
# 		tokentypes.append(token)
# 	tokentypes.append("#")
# 	return tokentypes

# Funcion principal
def parser(input):

	def getTokenTypes():
		tokens = lexer(input)
		tokens.append(("#", "FinDeCadena"))
		return tokens

	def getCurrentToken():
		return variables["tokens"][variables["pw"]][0]

	def esTerminal(simbolo):
		return simbolo in terminales

	def esNoTerminal(simbolo):
		return simbolo in no_terminales

	# Procesamiento de Producciones
	def Procesar(parte_derecha):
		for simbolo in parte_derecha:
			simbolo_apuntado = getCurrentToken()
			if esTerminal(simbolo):
				if simbolo_apuntado == simbolo:
					variables["pw"] += 1
					# variables["producciones_utilizadas"].append(simbolo)
				else:
					variables["error"] = True
					break
			if esNoTerminal(simbolo):
				indice_no_terminal = no_terminales.index(simbolo)
				PNi(indice_no_terminal)
				#variables["producciones_utilizadas"].append((no_terminales[indice_no_terminal], parte_derecha))

	# Funcion para cada No terminal
	def PNi(indice_no_terminal):
		variables["error"] = False
		for parte_derecha in producciones[indice_no_terminal]:
			variables["error"] = False
			backtrack_pivot = variables["pw"]
			Procesar(parte_derecha)
			if variables["error"]:
				variables["pw"] = backtrack_pivot
				variables["error"] = False

		# if not variables["error"]:
		# 	variables["producciones_utilizadas"].append(producciones[indice_no_terminal])

	def esFinDeCadena():
		simbolo_apuntado = getCurrentToken()
		return simbolo_apuntado == "#"

	def printOutput(aceptada):
		if aceptada:
			print('La cadena:')
			print('	', input)
			print('es ACEPTADA con:')
			print()
			for (VN, produ) in variables["producciones_utilizadas"]:
				print(VN, '->', produ)
			print()
		else:
			print('La cadena:')
			print('	', input)
			print('NO es ACEPTADA')
			print()


	tokens = getTokenTypes()
	variables = {
		"pw" : 0,
		"error" : False,
		"tokens" : tokens,
		"producciones_utilizadas" : []
	}
	PNi(0)
	if not variables["error"] and esFinDeCadena():
		printOutput(True)
		return True
	else:
		printOutput(False)
		return False


################################################################################
# Asserts
tests = [
			# ("int miFuncion(float a,int b){ for(c:=9, x := y,) a := 2+2;}", True),
			# ("float holi(int a, int b){ while( x := 20 := 11) ;}", True),
			# ("float far(int a, float b){ for( x := (2 + 3) + 20,,) ;}", True),
			# ("float testing(int x){ if(x:=9, x := y,) a := 2+2; else (z := 33) z := 11;}", True),
			("int hola(float a){ perro := 8;}", True),
			# ("int estonoanda(float a,int b){ for(c:=5, x := y) a := 10+3;;}", False),
			# ("float a (:= 3  2;)", False),
			# ("123abc", False),
			# ("a := 3 ++++ 2;", False),
			# ("float gatito(a > b);", False)
		]

for (input, output) in tests:
	assert parser(input) == output
################################################################################
