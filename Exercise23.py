# Faça um programa que leia um número de  a 9999 e
# mostre na tela cada um dos digitos separados.
# ex: 1834 unidade:4 dezena:3 centena: 8 milhar: 1
n = int(input('Type your number:'))
uni = n // 1 % 10
ten = n // 10 % 10
hun = n // 100 % 10
tho = n // 1000 % 10
print('Unity:', uni)
print('Ten:', ten)
print('Hundred:', hun)
print('Thousand:', tho)
