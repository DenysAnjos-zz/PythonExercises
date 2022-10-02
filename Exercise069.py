# Crie um programa que leia a idade e o sexo de
# várias pessoas. A cada pessoa cadastrada, o
# programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.
people18 = totalMen = womanUnder20 = 0

while True:
    age = int(input('Type your age:'))
    sex = ' '
    while sex not in 'wm':
        sex = str(input('Type W for woman and M for men:')).lower()
    if age > 18:
        people18 += 1
    if sex == 'm':
        totalMen += 1
    if age < 20 and sex == 'w':
        womanUnder20
    check = ' '
    while check not in 'yn':
        check = input('Do you want continue?(y/n)')
    if check == 'n':
        break

print('People over 18:', people18)
print('Registered men:', totalMen)
print('Woman under 20:', womanUnder20)
