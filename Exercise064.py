# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados
# e qual foi a soma entre eles, (desconsiderando o flag).
check, sum, quantity = 0, 0, 0
while check != 999:
    check = int(input('Type 999 for stop\nType a integer:'))
    sum += check
    quantity += 1
print('Total sum:', (sum-999))
print('Quantity entered:', (quantity-1))
