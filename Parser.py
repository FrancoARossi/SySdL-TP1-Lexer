from Lexer.py import lexer

error = False
Tokens = []

def parser(Tokens):
	# la variable t (indice del token apuntado) es global
	global Tokens = Tokens
	pw = 0
	PN0(pw)
	if not error and finDeCadena(Tokens, pw):
		return True
	else:
		return False

def PNi(i, pw):
	global error
	#No me cierra esta condicion de salida... en el algoritmo pone j <= k donde k es el numero de producciones de Ni
	# en este caso hay 1 sola produccion pero por como esta planteado el algoritmo cuando se llega al if por primera
	# vez j ya vale 2

	# esta bien que rompa ya que el procedimiento lo debe hacer solo una vez para PN1 (ya que tiene una sola produccion
	# el simbolo inicial)

	j = 0
	while (not error and ( j < P[i].len()):
		error = False
		Procesar(P[i][j], pw)
		j += 1

# lo de la diapositiva no es un repetir hasta, es un while normal, ya que continua en el ciclo MIENTRAS
# se cumpla la condicion, lo que me parece raro es que en la condicion este error si negar, por lo que
# si llega con el valor por defecto (false) no va a entrar en el ciclo, deberiamos preguntar que onda eso.
# Para mi deberia ser while (not(error) and (j <= 1))

def Procesar(produ, pw):
	global error
	# k tiene que ir desde 0 hasta la cantidad de producciones del VN
	# pero como sabe cuantas tiene si en los PNs esta hardcodeado?
	for k in (0, len(produ)-1): #esto solo lo resuelve para PN1, creo que deberiamos pasar como parametro que VN estamos evaluando
		if (produ[k] in Tokens):
			if (Tokens[pw] == produ[k]):
				pw += 1
			else:
				error = True
				break
		elif (produ[k] in VN):
			i = VN.index(produ[k])
			PNi(i, pw)
			if error:
				break

def finDeCadena(Tokens, pw):
	#se compara Tokens(len(Tokens)) == lista[t]
	pass


VT = [
		"ParOpen", "ParClose", "BraOpen", "BraClose", "OpMat", "ID", "Num", "Reservada", "Comma", "SemiColon", "OpRel"
	]

VN = [
		"<Funcion>", "<ListaArgumentos>", "<Argumento>", "<Declaracion>", "<ListaIdent>", "<Sentencia>", "<SentFor>", "<ExprOpt>", "<SentWhile>", "<SentIf>", "<SentenciaCompuesta>", "<ListaSentencia>", "<Expr>", "<ValorR>", "<AuxVR>", "<Mag>", "<AuxM>", "<Termino>", "<AuxT>", "<Factor>"
	]

P = [ # Producciones
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
