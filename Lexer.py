def lexer(cadena):
   
    tokens = []
    reservadas = ["int", "float", "if", "for", "while"]
    opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
    opMat = ["+", "*", "-", "/"]
    simbolos = ["(", ")", "{", "}", ",", ";"]         

    #Apartir de aca se aplicarian los automatas 

def re1 (acum):
    s = 0
    for c in acum:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
            break
        else:
            s = -1
            break
    return s == 3

def re2 (acum):
    s = 0
    for c in acum:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and 'l':
            s = 2
        elif s == 2 and 'o':
            s = 3
        elif s == 3 and  'a':
            s = 4
        elif s == 4 and 't':
            s = 5
            break
        else:
            s = -1
            break
    return s == 5

def re3 (acum):
    s = 0
    for c in acum:
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
            break
        else:
            s = -1
            break
    return s == 2

def re4 (acum):
    s = 0
    for c in acum:
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'o':
            s = 2
        elif s == 2 and c == 'r':
            s = 3
            break
        else:
            s = -1
            break
    return s == 3
def re5 (acum):
    s = 0
    for c in acum:
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
            break
        else:
            s = -1
            break
    return s == 5