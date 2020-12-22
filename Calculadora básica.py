x = '=='

a=float(input('Número 1 \n'))
while x != '=':
    b=input('Operação  \n')
    c=float(input('Número 2 \n'))
    x=input('Resultado final (=)?')
    if b == '+':
        a=(a+c)
        print (a)
    if b == '-':
        a = (a - c)
        print (a)
    if b == '*':
        a = (a * c)
        print (a)
    if b == '/':
        a = (a / c)
        print (a)
    if b != '+' and b!='-' and b!='*' and b!='/':
        print ('Erro na indicação da operação!')

