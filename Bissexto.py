bissexto = int(input('Digite um ano a partir de 1001 \n'))
if (bissexto%4==0):
    print('Ano bissexto')
elif (bissexto % 100 ==0 and bissexto % 400 ==0):
    print('Ano bissexto')
elif (bissexto % 100 ==0 and bissexto % 400 !=0):
    print('Ano não bissexto')
else:
    print('Ano não bissexto')