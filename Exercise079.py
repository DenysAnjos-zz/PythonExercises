# Crie um programa onde o usuário possa digitar vários
# valores numéricos e cadastre-os em uma lista. Caso o
# número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
numbers = list()
while True:
    n = int(input('Type a number:'))
    if n not in numbers:
        numbers.append(n)
    r = str(input('Do you want continue?(y/n)'))
    if r in 'nN':
        break
numbers.sort()
print(numbers)