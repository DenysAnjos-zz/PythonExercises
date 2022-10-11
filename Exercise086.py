# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.
matriz1 = list()
matriz2 = list()
matriz3 = list()
matrizAll = list()
count = count2 = 0
for n in range(0, 9):
    if count == 0:
        n = int(input(f'Type a a value for {count,count2}:'))
        matriz1.append(n)
        matrizAll.append(matriz1[:])
        matriz1.clear()
        count2 += 1
        if n == 3:
            count = 1
            count2 = 0
    elif count == 1:
        n = int(input(f'Type a a value for {count, count2}:'))
        matriz2.append(n)
        matrizAll.append(matriz2[:])
        matriz2.clear()
        count2 += 1
        if n == 6:
            count = 2
            count2 = 0
    else:
        n = int(input(f'Type a a value for {count, count2}:'))
        matriz3.append(n)
        matrizAll.append(matriz3[:])
        matriz3.clear()
        count2 += 1
count = 0
for m in matrizAll:
    if count < 3:
        print(matrizAll[count], end='')
        count += 1
        if count == 3:
            print('')
    elif count < 6:
        print(matrizAll[count], end='')
        count += 1
        if count == 6:
            print('')
    else:
        print(matrizAll[count], end='')
        count += 1

matrix = []
for n in range(0, 3):
    matrix_linha = []
    for j in range(0, 3):
        number = int(input(f'Type a a value for {n, j}:'))
        matrix_linha.append(number)
    matrix.append(matrix_linha[:])
