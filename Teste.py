
pwinicial = input('senha inicial \n')
senha = ''
for letra in pwinicial:
    if letra in 'Ss': senha = senha + '$'
    if letra in 'Ii': senha = senha + '!'
    if letra in 'Pp': senha = senha + '>'
    if letra in 'Qq': senha = senha + '<'
    if letra in 'Ee': senha = senha + '&'
    if letra in 'Aa': senha = senha + '@'
    if letra in '0': senha = senha + 'o'
    if letra in 'Oo': senha = senha + '0'
    else: senha = senha + letra
    print (letra)
print (senha)