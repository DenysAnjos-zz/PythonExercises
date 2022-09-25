# Desenvolva um programa que leia o
# nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20
mediaAge, olderName, womanU20, olderAge = 0, 0, 0, 0
olderName = str()

for c in range(1, 5):
    print('--- {}° ---'.format(c))
    nameCheck = str(input('Type your name:'))
    ageCheck = int(input('Type your age:'))
    sexCheck = str(input('Type (M) for men and (W) for women:')).lower()
    mediaAge += ageCheck
    if sexCheck == 'm' and ageCheck > olderAge:
        olderName = nameCheck
    elif sexCheck == 'w' and ageCheck < 20:
        womanU20 += 1

print('Media age:', mediaAge/4)
print('Older Men:', olderName, olderAge, 'years')
print('Women under 20:', womanU20)
