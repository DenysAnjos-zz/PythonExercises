# Crie um programa que crie uma matriz de dimensão 3x3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.
matrizAll = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matrizAll[l][c] = int(input(f'Type a position {l},{c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrizAll[l][c]:^3}]', end='')
    print()
