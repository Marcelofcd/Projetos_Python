pwinicial = input('senha inicial \n')
senha = ''
for letra in pwinicial:
    if letra in 'Ss': senha = senha + '$'
    elif letra in 'Ii': senha = senha + '!'
    elif letra in 'Pp': senha = senha + '>'
    elif letra in 'Qq': senha = senha + '<'
    elif letra in 'Ee': senha = senha + '&'
    elif letra in 'Aa': senha = senha + '@'
    elif letra in '0': senha = senha + 'o'
    elif letra in 'Oo': senha = senha + '0'
    else: senha = senha + letra
print (senha)