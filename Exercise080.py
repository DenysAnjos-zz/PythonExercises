# Crie um programa que possa digitar cinco valores
# numéricos e cadastre-os em uma lista, já na
# posição correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.
numbers = list()
for c in range(0, 5):
    n = int(input('Type a number:'))
    if c == 0 or n >= numbers[-1]:
        numbers.append(n)
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
        pos += 1

print(numbers)

