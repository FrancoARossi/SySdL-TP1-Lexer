from Lexer import lexer

error = False
Tokens = []
pw = 0

# TODO lineas de 281 caracteres son consideradas PESIMA practica,
# expresar esto en multiples lineas (idealmente, un element por linea)
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


# TODO las variables van todas en minisculas a menos que sean
# constantes o Clases
# TODO esto es un MUY mal nombre para esta funcion,
# lo que ustedes quieren es darle un nombre algo asi como
# getTokenTypes, dameTipoTokens, etc
# TODO Input no significa nada, en su lugar, utilicen "tokens"
#Captura solo el token de la salida del Lexer e ignora el lexema
def tratamientoTokens(Input):
        # TODO esto se deberia llamar tipo de tokens o algo similar
	tokens = []
	# TODO a, b son muy malos nombres de variables, denle un nombre mejor
	for (a,b) in Input:
		tokens.append(a)
	return tokens

def parser(Input):
        # TODO Prohibido utilizar "global", se van a ganar un monton de problemas
        # debido a la ambiguedad para declarar variables en python,
        # en su lugar utilicen el metodo que les mostre en clase:
        # definir la funcion parser y en su interior un diccionario en donde guardan
        # los tokens, los punteros, error, etc y tambien en su interior definen todas las funciones
        # que hacen referencia a dichos estados"
	global Tokens
	Tokens = lexer(Input)
	Tokens = tratamientoTokens(Tokens)
	PNi(0)
	# TODO error no se tiene idea de donde viene, esto es MUY mala programacion
	# TODO lo mismo con pw, es una variable magica que aparece de la nada, 
	# esto esta MUY mal
	# TODO "not" no es una funcion, es un operador, por lo que los parentesis estan de mas
	if not(error) and finDeCadena(Tokens, pw):
		return True
	else:
		return False

#Se define un procedimiento recursivo indirecto a reutilizar con el argumento i
def PNi(i):
        # TODO variables globales, remover
	global error
	global pw
	backtrack_pivot = pw
	j = 0
	# TODO parentesis innecesarios
	# TODO aca no se entiende lo que estan haciendo, 
	# si esto se corresponde a procesar las partes derechas que salen de un
	# no terminal indexado por "i" entonces deberia hacer algo como lo que
	# les pongo a continuacion
	# TODO se puede expresar mejor este ciclo
        # for parteDerecha in P[i]:
        #    error = False
        #    Procesar(parteDerecha)
        #    if not error:
        #      # todo bien
        # if error
        #   # todo mal
	while (not error and ( j < len(P[i]))):
		pw = backtrack_pivot
		error = False
		Procesar(P[i][j])
		j += 1

def Procesar(produ):
        # TODO remover variables globales
	global error
	global pw

        # TODO no estan utilizando los aspectos de alto nivel de python, hacer algo como lo que sigue:
        # for simbolo in produ:
        #    if es_terminal(simbolo):
        #       # do your thing
        #    else: # es no terminal
        #       # do your thing
	for k in range(0, len(produ)):
		if (produ[k] in Tokens):
			if (Tokens[pw] == produ[k]):
				pw += 1
			else:
				error = True
				break
		elif (produ[k] in VN):
			i = VN.index(produ[k])
			PNi(i)
			if error:
				break

def finDeCadena(Tokens, pw):
	return (len(Tokens) - 1) == pw

# TODO python es un lenguage en donde la indentacion 
# es importante, entonces TIENEN que tener una indentacion constante y consistente,
# aca se ve como mezclan espacios y tabs, utilizar o solo TABs o solo espacios, no
# mezlcar, el programa no me corre por estol
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

# TODO utilizar aspectos de alto nivel de python
# for (input, output) in inputs:
#    assert parse(input) == output
for i in range(10):
	assert parser(inputs[i][1]) == inputs[i][2]
################################################################################
