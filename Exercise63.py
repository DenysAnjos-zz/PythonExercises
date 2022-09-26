# Escreva um programa que leia um
# número N inteiro qualquer e mostre
# na tela os N primeiros elementos
# de uma sequencia de fibonacci.
# ex: 1 > 1 > 2 > 3 > 5 > 8 > 13 > 21
n = int(input('Type a integer:'))
n2 = int(input('Type a integer for sequence:'))
a, b = 1, 0
c = 0
while n < n2:
    n += 1
    a = a + b
    b = c - b
    c = a + b
    print(a, end=' > ')
