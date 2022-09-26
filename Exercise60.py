# Faça um programa que leia um número
# qualquer e mostre o seu fatorial.
# ex: 5  5*4*3*2*1=120
n = int(input('Type a number:'))
total2 = n * n
total2, total3, c = 0, 0, 0
while c != 5:
    print(n, end='*')
    total = n*(n-1)
    total2 += total
    total3 += total2+total-n
    n -= 1
    c += 1

print('=', total2)
print('=', total3)
