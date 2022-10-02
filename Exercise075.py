# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final mostre:
# Quantas vezes apareceu o valor 9. Em que posição foi
# digitado o primeiro valor 3. Quais foram os números pares
number = int(input('Type a number:')), int(input('Type a number:')),\
         int(input('Type a number:')), int(input('Type a number:'))
print(f'The number 9 appeared {number.count(9)} times.')
if 3 in number:
    print(f'The first 3 appears initially in position {number.index(3)+1}.')
else:
    print('The value 3 was not typed.')
print('The pairs are:')
for n in number:
    if n % 2 == 0:
        print(n, end=' ')