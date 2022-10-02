# Crie um programa que leia vários números inteiros
# pelo teclado. O  programa só vai parar quando o
# usuário digitar ovalor 999, que é a condição de
# parada. No final, mostre quantos números foram
# digitados e quais foram a soma entre eles
# (desconsiderando o flag)

sum = cont = 0
while True:
    check = int(input('Type a value (999 to stop):'))
    if check == 999:
        break
    sum += check
    cont += 1

print("The sum of the values is:", sum)
print('Total numbers:', cont)