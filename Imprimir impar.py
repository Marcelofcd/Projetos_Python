n1 = int(input('Qual o primeiro número? \n'))
n2 = int(input('Qual o segundo número? \n'))
if n1>n2:
    print(f'Os números ímpares entre {n2} e {n1} são:')
    while n2<=n1:
        if (n2%2!=0):
            print(n2)
            n2=n2+1
        else:
            n2=n2+1
elif n2>n1:
    print(f'Os números ímpares entre {n1} e {n2} são:')
    while n1 <= n2:
        if (n1 % 2 != 0):
            print(n1)
            n1=n1+1
        else:
            n1=n1+1
else: print('Os números informados são iguais')