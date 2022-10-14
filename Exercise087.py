# Aprimore  o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.
matrizAll = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pairN = sumColumn = biggestLine = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrizAll[l][c] = int(input(f'Type a position {l},{c}: '))
for l in range(0, 3):
    sumColumn += matrizAll[l][2]
    for c in range(0, 3):
        print(f'[{matrizAll[l][c]:^3}]', end='')
        if c == 0:
            biggestLine = matrizAll[1][c]
        elif matrizAll[1][c] > biggestLine:
            biggestLine = matrizAll[1][c]

        if matrizAll[l][c] % 2 == 0:
            pairN += matrizAll[l][c]
    print()
print('Sum pair numbers:', pairN)
print('Sum column:', sumColumn)
print('Biggest line:', biggestLine)







