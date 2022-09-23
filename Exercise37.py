# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base da conversão.
# 1 para decimal, 2 para octal 3 para hexadecimal
number = int(input('Type a number to convert:'))
tyype = input('Choose between binary,octal and hexadecimal:').lower()

if tyype == 'binary':
    number = bin(number)
elif tyype == 'octal':
    number = oct(number)
else:
    number = hex(number)

print(number[2:])
