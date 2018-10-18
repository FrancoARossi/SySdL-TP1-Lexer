from Lexer.py import lexer

error = False

def parser(TokenTypes):
	# la variable t (indice del token apuntado) es global
	pw = 0
	PN1(pw)
	if not error and finDeCadena(TokenTypes, pw):
		return True
	else:
		return False

def PN1(pw):
	global error
	#No me cierra esta condicion de salida... en el algoritmo pone j <= k donde k es el numero de producciones de Ni
	# en este caso hay 1 sola produccion pero por como esta planteado el algoritmo cuando se llega al if por primera
	# vez j ya vale 2

	# esta bien que rompa ya que el procedimiento lo debe hacer solo una vez para PN1 (ya que tiene una sola produccion
	# el simbolo inicial)

	j = 0
	while (error and (j <= 0)):
		error = False
		Procesar(produ, pw)
		j += 1

# lo de la diapositiva no es un repetir hasta, es un while normal, ya que continua en el ciclo MIENTRAS
# se cumpla la condicion, lo que me parece raro es que en la condicion este error si negar, por lo que
# si llega con el valor por defecto (false) no va a entrar en el ciclo, deberiamos preguntar que onda eso.
# Para mi deberia ser while (not(error) and (j <= 1))

def Procesar(produ, pw):
	global error
	# j tiene que ir desde 0 hasta la cantidad de producciones del VN
	# pero como sabe cuantas tiene si en los PNs esta hardcodeado?
	for j in (0, len(P[0])): #esto solo lo resuelve para PN1, creo que deberiamos pasar como parametro que VN estamos evaluando

def finDeCadena(TokenTypes, pw):
	#se compara TokenTypes(len(TokenTypes)) == lista[t]
	pass


VT = [
		"ParOpen", "ParClose", "BraOpen", "BraClose", "OpMat", "ID", "Num", "Reservada", "Comma", "SemiColon", "OpRel"
	]

VN = [
		"Funcion", "ListaArgumentos", "Argumento", "Declaracion", "ListaIdent", "Sentencia", "SentFor", "Expr", "ExprOpt", "SentWhile", "SentIf", "SentenciaCompuesta", "ListaSentencia", "ValorR", "Mag", "Factor", "Termino", "AuxVR", "AuxM", "AuxT"
	]

P = [ #producciones
		[ # <Funcion>
			[
				"ReservadaID", "ParOpen", "<ListaArgumentos>", "ParClose", "<SentenciaCompuesta>"
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
				"ReservadaID"
			]
		],
		[ # <Declaracion>
			[
				"Reservada", "<ListaIdent>", "SemiColon"
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
				"Reservada", "ParOpen", "<Expr>", "Comma", "<ExprOpt>", "Comma", "<ExprOpt>", "ParClose", "<Sentencia>", "SemiColon"
			]
		],
		[ # <ExprOpt>
			[
				"<Expr>"
			],
			[
				lambada #anulable? chan chan CHAN!
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
