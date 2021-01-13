try:
    num = int(input('Digite um numero\n'))
    print(num)
except:
    print('Não inteiro')
# except Valueerror / zeroDivisionError: - é possível especificar a mensagem para cada tipo de erro