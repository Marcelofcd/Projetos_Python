import math
c1=float(input('Digite o comprimento do cateto 1 '))
c2=float(input('Digite o comprimento do cateto 2 '))
h= math.sqrt(math.pow(c1,2)+math.pow(c2,2))
print('O tamanho da hipotenusa é {:.2f}' .format(h))
