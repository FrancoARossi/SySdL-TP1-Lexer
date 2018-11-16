from Lexer import lexer

#Terminales
Terminales = [ # Terminales
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

# No Terminales
noTerminales = [ # No terminales
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

def leerCadena(src):
	tokens = lexer(src)
	tokens.append(('$', 'FIN DE CADENA'))
	return tokens

def procedimiento(noTerminal):
	punteroAuxiliar = estado['puntero']
	produccionesUsadas = estado['produccionesUsadas']
	for parteDerecha in producciones[noTerminal]:
		estado['error'] = False
		procesar(parteDerecha)
		if not estado['error']:
			produccionesUsadas.append((noTerminal,parteDerecha))
			break
		else:
			estado['puntero'] = punteroAuxiliar


def procesar(parteDerecha):
	for elemento in parteDerecha:
		if elemento in Terminales:
			cadena = estado['cadena']
			puntero = estado['puntero']
			posicion = 0
			if elemento == cadena[puntero][posicion]:
				estado['puntero'] = estado['puntero'] + 1
			else:
				estado['error'] = True
		if elemento in noTerminales:
			procedimiento(elemento)
		if estado['error']:
			break

estado = {
	'error':False,
	'puntero':0,
	'cadena':[],
	'produccionesUsadas':[]
}

def printOutput(aceptada):
	estado["produccionesUsadas"].reverse()

	if aceptada:
		print('La cadena:\n')
		print('	', input,'\n')
		print('es ACEPTADA con:')
		for (VN, produ) in estado["produccionesUsadas"]:
			print('	', VN, '->', produ)
	else:
		print('La cadena:\n')
		print('	', input,'\n')
		print('NO es ACEPTADA')

	print('\n-----------------------------------------------------------\n')

def parser(src) :
	estado['puntero'] = 0
	estado['produccionesUsadas'] = []
	estado['cadena'] = leerCadena(src)
	procedimiento('<Funcion>')
	cadena = estado['cadena']
	puntero = estado['puntero']
	#Como la cadena de entrada es de la forma: "(INT,2)(id,hola)..."
	#necesito el primero elemento de la tupla para comparar
	posicionPorTokenizador = 0
	if not estado['error'] and cadena[puntero][posicionPorTokenizador] == '$' :
		printOutput(True)
		return True
	else:
		printOutput(False)
		return False


################################################################################
# Asserts
tests = [
			("int miFuncion(float a,int b){ for(c:=9, x := y,) a := 2+2;}", True),
			("float holi(int a, int b){ while( x := 20 := 11) ;}", True),
			("float far(int a, float b){ for( x := (2 + 3) + 20,,) ;}", True),
			("float testing(int x){ if(x:=9, x := y,) a := 2+2; else (z := 33) z := 11;}", True),
			("int hola(float a){ perro := 8;}", True),
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
