def lexer(cadena):
   
    tokens = []
    var = (False, 0)
    cadena = cadena + "¬"

    while cadena[var[1]] != "¬":
        var = re1(cadena, var[1])
        if var[0]:
            tokens.append(("<int>", "int"))
        var = re2(cadena, var[1])
        if var[0]:
            tokens.append(("<float>", "float"))
        var = re3(cadena, var[1])
        if var[0]:
            tokens.append(("<if>", "if"))
        var = re4(cadena, var[1])
        if var[0]:
            tokens.append(("<for>", "for"))
        var = re5(cadena, var[1])
        if var[0]:
            tokens.append(("<while>", "while"))
    print(tokens)

def re1 (cadena, pos):
    s = 0
    for i in range(pos ,len(cadena)):
        c = cadena[i]
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'n':
            s = 2
        elif s == 2 and c == 't':
            s = 3
            i+=1
            break
        else:
            i-=s
            s = -1
            break
    return (s == 3, i)

def re2 (cadena, pos):
    s = 0
    for i in range(pos, len(cadena)):
        c = cadena[i]
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
            i+=1
            break
        else:
            i-=s
            s = -1
            break
    return (s == 5, i)

def re3 (cadena, pos):
    s = 0
    for i in range(pos, len(cadena)):
        c = cadena[i]
        if s == 0 and c == 'i':
            s = 1
        elif s == 1 and c == 'f':
            s = 2
            i+=1
            break
        else:
            i-=s
            s = -1
            break
    return (s == 2, i)

def re4 (cadena, pos):
    s = 0
    for i in range(pos, len(cadena)):
        c = cadena[i]
        if s == 0 and c == 'f':
            s = 1
        elif s == 1 and c == 'o':
            s = 2
        elif s == 2 and c == 'r':
            s = 3
            i+=1
            break
        else:
            i-=s
            s = -1
            break
    return (s == 3, i)

def re5 (cadena, pos):
    s = 0
    for i in range(pos, len(cadena)):
        c = cadena[i]
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
            i+=1
            break
        else:
            i-=s
            s = -1
            break
    return (s == 5, i)

lexer("intfloatifforwhile")