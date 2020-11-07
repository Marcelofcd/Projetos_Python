a = int(input('Digite um valor \n'))
b = int(input('Digite um valor \n'))
c = int(input('Digite um valor \n'))
if (a<b+c) and (b<a+c) and (c<a+b):
    print (f'É possível gerar um triângulo com os valores informados {a}, {b}, {c} ')
    if a==b==c:
        print('O triângulo é equilátero')
    elif (a==b) or (a==c) or (b==c):
            print ('O triangulo é isósceles')
    elif (a!=b) and (a!=c) and (b!=c):
        print ('O triângulo é escaleno')
else: print ('Não é possível formar um triângulo')