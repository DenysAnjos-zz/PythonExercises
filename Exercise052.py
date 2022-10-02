# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo
n = int(input('Type a number:'))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(c, '= true')
        total += 1
    else:
        print(c, '= false')

print('The number {} was divisible for {} numbers.'.format(n, total))
if total == 2:
    print('{} is a prime number'.format(n))
else:
    print('{} is not a prime number'.format(n))