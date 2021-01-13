aluguel = float(input('Aluguel \n'))
iptu = float(input('IPTU \n'))
cota_extra = float(input ('Cota Extra \n'))
fundo_reserva = float(input ('Fundo de Reserva \n'))
multa_diaria = float(input('Multa Diária por atraso \n'))
m = ()
if multa_diaria>20:
    multa_diaria=20
valor_multa = float(multa_diaria*1/100*aluguel)
if valor_multa == 0:
    juros_mora = 0
else:
    juros_mora = 0.1/30*aluguel
Total = aluguel+iptu-cota_extra-fundo_reserva+valor_multa+juros_mora
mes= int(input('Mês do Aluguel\n'))
if (mes == 1):
    m = 'Janeiro'
if (mes == 2):
    m = 'Fevereiro'
if (mes == 3):
    m = 'Março'
if (mes == 4):
    m = 'Abril'
if (mes == 5):
    m = 'Maio'
if (mes == 6):
    m = 'Junho'
if (mes == 7):
    m = 'Julho'
if (mes == 8):
    m = 'Agosto'
if (mes == 9):
    m = 'Setembro'
if (mes == 10):
    m = 'Outubro'
if (mes == 11):
    m = 'Novembro'
if (mes == 12):
    m = 'Dezembro'
print (f'Aluguel {m}/2020 R$ {aluguel}')
print (f'IPTU R$ {iptu}')
print (f'Cota Extra R$ -{cota_extra}')
print (f'Fundo de Reserva R$ -{fundo_reserva}')
print('Multa Diária por atraso R$ {:.2f}'.format(valor_multa))
print('Juros de Mora R$ {:.2f}'.format(juros_mora))
print('TOTAL R$ {:.2f}'.format(Total))