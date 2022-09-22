# Faça um programa que leia tres numeros e
# mostre qual é o maior e qual é o menor
n1 = int(input('Type a value:'))
n2 = int(input('Type a value:'))
n3 = int(input('Type a value:'))
if n1 > n2 and n1 > n3:
    print('The first value is the largest')
elif n2 > n1 and n2 > n3:
    print('The second value is the largest')
elif n3 > n1 and n3 > n2:
    print('The third value is the largest')
else:
    print('There are two or more equal values')