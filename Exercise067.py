# Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando
# o número for solicitado for negativo.
while True:
    check = int(input('Do you want see the multiples of which number?'))
    if check <= 0:
        break
    add = 1
    while add < 11:
        print("{} x {} = {}".format(check, add, (check*add)))
        add += 1
