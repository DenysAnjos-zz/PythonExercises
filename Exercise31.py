# Desenvolva um programa que pergunte a distancia de uma viagem
# em km, calcule o preço da passagem cobrando 0.5 por km
# para viagens de até 200km e 0.45 para viagens mais longas
dist = float(input('Type the travelled distance:'))
if dist <= 200:
    print('Total to pay:R$', (dist*0.5))
else:
    print('Total to pay:R$', (dist*0.45))

