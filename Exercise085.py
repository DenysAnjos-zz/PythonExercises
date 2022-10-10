# Crie um programa onde o usuário possa digitar
# sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores
# pares e impares. No final, mostre os valores
# pares e ímpares em ordem crescente.
numbersAll = list()
numbersOdd = list()
numbersPair = list()
for n in range(0, 6):
    n = int(input('Type a number:'))
    numbersAll.append(n)
    if n % 2 == 0:
       numbersPair.append(n)
    else:
       numbersOdd.append(n)
    numbersAll.clear()
numbersPair.sort()
numbersOdd.sort()
print(f'Pair:{numbersPair} ')
print(f'Odd:{numbersOdd} ')