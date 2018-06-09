def lexer(cadena):
   
    tokens = []

def a_re1 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 3)

def a_re2 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'l':
            s = 2
        elif s == 2 and c == 'o':
            s = 3
        elif s == 3 and c == 'a':
            s = 4
        elif s == 4 and c == 't':
            s = 5
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 5)

def a_re3 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 2)

def a_re4 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'e':
            s = 1
        elif s == 1 and c == 'l':
            s = 2
        elif s == 2 and c == 's':
            s = 3
        elif s == 3 and c == 'e':
            s = 4
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 4)

def a_re5 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'o':
            s = 2
        elif s == 2 and c == 'r':
            s = 3
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 3)

def a_re6 (tokens, acu):
    s = 0
    for c in acu:
        if s == 0 and c == 'w':
            s = 1
        elif s == 1 and c == 'h':
            s = 2
        elif s == 2 and c == 'i':
            s = 3
        elif s == 3 and c == 'l':
            s = 4
        elif s == 4 and c == 'e':
            s = 5
            tokens.append(("<" + acu + ">", acu))
        else:
            s = -1
            break
    return (s == 5)

def a_ParOpen (tokens, acu):
    s = 0
    for c in acu:
        if c == "("
            s = 1
            tokens.append(("<ParOpen>", acu))
        else:
            s = -1
    return (s == 1)

def a_ParClose (tokens, acu):
    s = 0
    for c in acu:
        if c == ")"
            s = 1
            tokens.append(("<ParClose>", acu))
        else:
            s = -1
    return (s == 1)

def a_BraOpen (tokens, acu):
    s = 0
    for c in acu:
        if c == "{"
            s = 1
            tokens.append(("<BraOpen>", acu))
        else:
            s = -1
    return (s == 1)

def a_BraClose (tokens, acu):
    s = 0
    for c in acu:
        if c == "}"
            s = 1
            tokens.append(("<BraClose>", acum))
        else:
            s = -1
    return (s == 1)

def a_Coma (tokens, acu):
    s = 0
    for c in acu:
        if c == ","
            s = 1
            tokens.append(("<Coma>", acum))
        else:
            s = -1
    return (s == 1)

def a_PointComa (tokens, acu):
    s = 0
    for c in acu:
        if c == ";"
            s = 1
            tokens.append(("<PointComa>", acum))
        else:
            s = -1
    return (s == 1)

def a_Sum (tokens, acu):
    s = 0
    for c in acu:
        if c == "+"
            s = 1
            tokens.append(("<Sum>", acum))
        else:
            s = -1
    return (s == 1)

def a_Minus (tokens, acu):
    s = 0
    for c in acu:
        if c == "-"
            s = 1
            tokens.append(("<Minus>", acum))
        else:
            s = -1
    return (s == 1)

def a_Product (tokens, acu):
    s = 0
    for c in acu:
        if c == "*"
            s = 1
            tokens.append(("<Product>", acum))
        else:
            s = -1
    return (s == 1)

def a_Division (tokens, acu):
    s = 0
    for c in acu:
        if c == "/"
            s = 1
            tokens.append(("<Division>", acum))
        else:
            s = -1
    return (s == 1)

# Al finalizar el lexer deberia aceptar esta cadena
lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2;}")

# Habria que mandar un mensaje de error en este caso
lexer("1 <( 2")