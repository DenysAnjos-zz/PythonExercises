# Crie um programa que simule o funcionamento de um caixa
# eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado(número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1
ballot50 = ballot20 = ballot10 = ballot5 = ballot2 = ballot1 = 0
value = int(input('Type a integer:'))
while True:
    if value >= 50:
        value -= 50
        ballot50 += 1
    elif value >= 20:
        value -= 20
        ballot20 += 1
    elif value >= 10:
        value -= 10
        ballot10 += 1
    elif value >= 5:
        value -= 5
        ballot5 += 1
    elif value >= 2:
        value -= 2
        ballot2 += 1
    else:
        value -= 1
        ballot1 += 1
    if value == 0:
        break

print('Banknotes 50:', ballot50)
print('Banknotes 20:', ballot20)
print('Banknotes 10:', ballot10)
print('Banknotes 5:', ballot5)
print('Banknotes 2:', ballot2)
print('Banknotes 1:', ballot1)

