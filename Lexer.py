def lexer(cadena):
   
    tokens = []

def re1 (tokens, palabra):
    s = 0
    for c in palabra:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
            tokens.append(("<int>", "int"))
        else:
            s = -1
            break
    return (s == 3, tokens)

def re2 (tokens, palabra):
    s = 0
    for c in palabra:
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
            tokens.append(("<float>", "float"))
        else:
            s = -1
            break
    return (s == 5, tokens)

def re3 (tokens, palabra):
    s = 0
    for c in palabra:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
            tokens.append(("<if>", "if"))
        else:
            s = -1
            break
    return (s == 2, tokens)

def re4 (tokens, palabra):
    s = 0
    for c in palabra:
        if s == 0 and c == 'e':
            s = 1
        elif s == 1 and c == 'l':
            s = 2
        elif s == 2 and c == 's':
            s = 3
        elif s == 3 and c == 'e':
            s = 4
            tokens.append(("<else>", "else"))
        else:
            s = -1
            break
    return (s == 4, tokens)

def re5 (palabra):
    s = 0
    for c in palabra:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'o':
            s = 2
        elif s == 2 and c == 'r':
            s = 3
            tokens.append(("<for>", "for"))
        else:
            s = -1
            break
    return (s == 3, tokens)

def re6 (palabra):
    s = 0
    for c in palabra:
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
            tokens.append(("<while>", "while"))
        else:
            s = -1
            break
    return (s == 5, tokens)

# Al finalizar el lexer deberia aceptar esta cadena
lexer("int miFuncion(float a,int b){ for(c:=9, x == y) a := 2+2;}")