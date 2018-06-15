opLog = [':=', '<', '>', '>=', '<=', '!=', '==']
opMat = ['+', '*', '-', '/']
simbolos = ['(', ')', '{', '}', ',']

def lexer(src):
    tokens = []
    i = 0
    text = src + ' '

    

# Estas srcs deben devolver un token de error
prueba1 = lexer("int miFuncion(float a,int b){ for(c:=9, x <= y) a := 2+2}error")
for i in range(len(prueba1)):
 	print (prueba1[i])
# Exit Debug
