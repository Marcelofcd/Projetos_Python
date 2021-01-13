x = [3, 4, 8, 615, 321]
x2 = ['asd', 'df', 'dfgf', 's']
print (x[::]) #igual a mandar imprimir toda a lista
print (x[1:]) #imprime do elemento 1 ao final da lista
print (x[:3]) #imprime do início da lista até o elemento nº 3 -1
"""
x.pop() # remove o último argumento - exceto se dentro do parenteses indicar o index a ser excluído
x.remove('322') # remove um elemento específico

del x # exclui a variável ou um elemento do index se for x[0] por exemplo

x.clear() # apaga os elementos da lista
"""
x.sort() # organiza em ordem alfabética ou numerica - OBS não colocará iniciados com minúscula junto com maiúscula
x.sort(reverse=True) # organiza em ordem contrária à alfabética ou numerica
x.reverse() # inverte a ordem estabelecida na lista

x.extend(x2) # adiciona a 2ª lista a 1ª

x = x2.copy() # copia a lista 2 para a 1