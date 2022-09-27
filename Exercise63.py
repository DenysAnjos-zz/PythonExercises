# Escreva um programa que leia um
# número N inteiro qualquer e mostre
# na tela os N primeiros elementos
# de uma sequencia de fibonacci.
# ex: 1 > 1 > 2 > 3 > 5 > 8 > 13 > 21
n = int(input('How many numbers do you want to show?'))
a, b, c, n2 = 1, 0, 0, 0
while n > n2:
    a = a + b
    b = c - b
    c = a + b
    if n != n2:
        print(a, end='')
        n2 += 1
        if n != n2:
            print(end=' > ')
