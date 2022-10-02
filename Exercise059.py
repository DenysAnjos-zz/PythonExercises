# Crie um programa que leia dois valores
# e mostre um menu na tela:
# [1] somar [2] multiplicar [3] maior
# [4] novos números [5] sair do programa
# Seu programa deverá realizar a operação
# solicitada em cada caso.
value1 = int(input('Type the first value:'))
value2 = int(input('Type the second value:'))
check = int
while check != 5:
    print('[1] Sum!')
    print('[2] Multiply!')
    print('[3] Bigger!')
    print('[4] New numbers!')
    print('[5] Exit!')
    check = int(input('Type your choice:'))
    if check == 1:
        print('{} + {} = {}'.format(value1, value2, (value1 + value2)))
    elif check == 2:
        print('{} * {} = {}'.format(value1, value2, (value1 * value2)))
    elif check == 3:
        if value1 > value2:
            print('{} is bigger'.format(value1))
        else:
            print('{} is bigger'.format(value2))
    elif check == 4:
        value1 = int(input('Type the first value:'))
        value2 = int(input('Type the second value:'))
    else:
        print('End!')