# Escreva um programa que leia dois números inteiros
# e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
first = int(input('Type the first number:'))
second = int(input('Type the second number:'))
if first > second:
    print('The first number is bigger.')
elif second > first:
    print('The second number is bigger.')
else:
    print('They are equal.')
