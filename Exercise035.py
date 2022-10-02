# Desenvolva um programa que leia o comprimento
# das três retas e diga ao usuário se elas podem
# ou não formar um triangulo. Matematicamente, para três segmentos formarem um triângulo, o
#  * comprimento de cada lado deve ser menor que a soma dos outros dois
l1 = float(input('Type a first length:'))
l2 = float(input('Type a second length:'))
l3 = float(input('Type a third length:'))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Its not a triangle!')
else:
    print('Its a triangle!')

