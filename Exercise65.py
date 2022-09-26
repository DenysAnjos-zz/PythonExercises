# Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor
# valor lido. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.
sum, total, media, biggest, lowest = 0, 0, 0, 0, 0

check = 'y'
while check == 'y':
    sum = int(input('Type a integer for sum:'))
    total += sum
    if biggest < sum:
        biggest = sum
    if lowest == 0:
        lowest = sum
    if lowest > sum:
        lowest = sum
    check = input('Do you want continue?(y/n)').lower()

print('Total:', total)
print('Biggest:', biggest)
print('Lowest:', lowest)
