# Desenvolva um programa que leia seis
# números inteiros e mostre a soma apenas
# daqueles que forem pares. se o valor
# digitado for impar, desconsidere-o
sum = int()
for c in range(0, 6):
    n = int(input('Type a number:'))
    if n % 2 == 0:
        sum = sum + n

print('Sum:', sum)
