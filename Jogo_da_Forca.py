forca = input('Digite uma palavra \n')
palavra = forca
print('\n' *1000)
tamanho = int(len(forca))
print (f'A palavra tem {tamanho} letras')
contagem = 0
temp=[]
while tamanho!=0:
    palavra[tamanho-1]= palavra.replace('$')
    tamanho-=1
print (palavra)
print (temp)
letra = input ('Digite uma letra \n')
i = 1
while contagem <=9:
    tamanho=0
    while tamanho !=len(forca):
        if letra == forca[tamanho]:
            temp [tamanho] = letra
        tamanho+=1
    print (temp)
    letra = input ('Digite outra letra \n')
    contagem +=1
    igual=temp.strip()
    print (igual)
print(forca[0])