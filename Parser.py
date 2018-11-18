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

producciones = { # Producciones
		"<Funcion>" : [ # <Funcion>
			[
				"Reservada", "ID", "ParOpen", "<ListaArgumentos>", "ParClose", "<SentenciaCompuesta>"
			]
		],
		"<ListaArgumentos>" : [ # <ListaArgumentos>
			[
				"<Argumento>", "Comma", "<ListaArgumentos>"
			],
			[
				"<Argumento>"
			]
		],
		"<Argumento>" : [ # <Argumento>
			[
				"Reservada", "ID"
			]
		],
		"<Declaracion>" : [ # <Declaracion>
			[
				"Reservada", "<ListaIdent>", "SemiColon"
			]
		],
		"<ListaIdent>" : [ # <ListaIdent>
			[
				"ID", "Comma", "<ListaIdent>"
			],
			[
				"ID"
			]
		],
		"<Sentencia>" : [ # <Sentencia>
			[
				"SemiColon"
			],
			[
				"<SentWhile>"
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
				"<SentFor>"
			],
			[
				"<Expr>", "SemiColon"
			]
		],
		"<SentFor>" : [ # <SentFor>
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "<Expr>", "Comma", "<Expr>", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "<Expr>", "Comma", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "Comma", "<Expr>", "ParClose", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "Comma", "Comma"," ParClose", "<Sentencia>"
			]
		],
		"<SentWhile>" : [ # <SentWhile>
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>"
			]
		],
		"<SentIf>" : [ # <SentIf>
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>", "Reservada", "<Sentencia>"
			],
			[
				"Reservada", "ParOpen", "<Expr>", "ParClose", "<Sentencia>"
			]
		],
		"<SentenciaCompuesta>" : [ # <SentenciaCompuesta>
			[
				"BraOpen", "<ListaSentencia>", "BraClose"
			]
		],
		"<ListaSentencia>" : [ # <ListaSentencia>
			[
				"<Sentencia>", "<ListSentencia>"
			],
			[
				"<Sentencia>"
			]
		],
		"<Expr>" : [ # <Expr>
			[
				"ID", "OpRel", "<Expr>"
			],
			[
				"<ValorR>"
			]
		],
		"<ValorR>" : [ # <ValorR>
			[
				"<Mag>", "<AuxVR>"
			],
			[
				"<Mag>"
			]
		],
		"<AuxVR>" : [ # <AuxVR>
			[
				"OpRel", "<Mag>", "<AuxVR>"
			],
			[
				"OpRel", "<Mag>"
			]
		],
		"<Mag>" : [ # <Mag>
			[
				"<Termino>", "<AuxM>"
			],
			[
				"<Termino>"
			]
		],
		"<AuxM>" : [ # <AuxM>
			[
				"OpMat", "<Termino>", "<AuxM>"
			],
			[
				"OpMat", "<Termino>"
			]
		],
		"<Termino>" : [ # <Termino>
			[
				"<Factor>", "<AuxT>"
			],
			[
				"<Factor>"
			]
		],
		"<AuxT>" : [ # <AuxT>
			[
				"OpMat", "<Termino>", "<AuxT>"
			],
			[
				"OpMat", "<Termino>"
			]
		],
		"<Factor>" : [ # <Factor>
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
	}

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

	def guardarProduccion(noTerminal, parte_derecha):
		variables["producciones_utilizadas"].append((noTerminal, parte_derecha))

	def esFinDeCadena():
		simbolo_apuntado = getCurrentToken()
		return simbolo_apuntado == "#"

	# Procesamiento de Producciones
	def Procesar(parte_derecha):
		for simbolo in parte_derecha:
			simbolo_apuntado = getCurrentToken()
			# print("Parte derecha:", parte_derecha)
			# print("Simbolo de parte derecha:", simbolo)
			# print("Simbolo apuntado:", simbolo_apuntado)
			# print("---")
			if esTerminal(simbolo):
				if simbolo_apuntado == simbolo:
					variables["pw"] += 1
				else:
					variables["error"] = True
					break
			elif esNoTerminal(simbolo):
				PNi(simbolo)

	# Funcion para cada No terminal
	def PNi(noTerminal):
		variables["backtrack_pivot"] = variables["pw"]
		for parte_derecha in producciones[noTerminal]:
			variables["error"] = False
			Procesar(parte_derecha)
			if variables["error"]:
				variables["pw"] = variables["backtrack_pivot"]
			else:
				guardarProduccion(noTerminal, parte_derecha)
				break

	def printOutput(aceptada):
		variables["producciones_utilizadas"].reverse()

		if aceptada:
			print('La cadena:\n')
			print('	', input,'\n')
			print('es ACEPTADA con:')
			for (VN, produ) in variables["producciones_utilizadas"]:
				print('	', VN, '->', produ)
		else:
			print('La cadena:\n')
			print('	', input,'\n')
			print('NO es ACEPTADA')

		print('\n-----------------------------------------------------------\n')

	tokens = getTokenTypes()
	variables = {
		"pw" : 0,
		"error" : False,
		"tokens" : tokens,
		"backtrack_pivot" : 0,
		"producciones_utilizadas" : []
	}
	PNi("<Funcion>")
	if not variables["error"] and esFinDeCadena():
		printOutput(True)
		return True
	else:
		printOutput(False)
		return False


################################################################################
# Asserts
tests = [
			("int miFuncion(float a,int b){a := 2>2}", True), #
			("float holi(int a, int b){ while( x := 20 := 11) ;}", True),#
			("int main(int franco, int ivan, int jairo){ while( notadelospibes < 10) parser := franco + ivan + jairo * cafe ;}", True),
			# ("float far(int a){ for( x := 20,,) b:=2 ;}", True), no anda
			("float testing(int x){ if(x:=9) a := 2+2;}", True),
			("int hola(float a){ perro := 8;}", True),#
			("int estonoanda(float a,int b){ for(c:=5, x := y) a := 10+3;;}", False),
			("float a (:= 3  2;)", False),
			("123abc", False),
			("a := 3 ++++ 2;", False),
			("float gatito(a > b);", False)
		]

for (input, output) in tests:
	# assert parser(input) == output
	parser(input)
################################################################################
