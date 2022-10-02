# Faça um programa que leia tres numeros e
# mostre qual é o maior e qual é o menor
n1 = int(input('Type a value:'))
n2 = int(input('Type a value:'))
n3 = int(input('Type a value:'))
smaller = n1
if n2 < n1 and n2 < n3:
    smaller = n2
elif n3 < n1 and n3 < n2:
    smaller = n3

print('The smaller value is:{}'.format(smaller))
largest = n1
if n2 > n3 and n2 > n1:
    largest = n2
elif n3 > n1 and n3 > n2:
    largest = n3

print('The largest value is:{}'.format(largest))
