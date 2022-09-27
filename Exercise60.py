# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# ex: 5  5*4*3*2*1=120
c = int(input('Type a number:'))
total2, total3, n = 0, 0, 1
d = c

while d > 0:
    if d > 1:
        print('{} x '.format(d), end='')
    else:
        print('{} = '.format(d), end='')
    n *= c
    d -= 1
    c -= 1
print(n)

