# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. no final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
all = list()
cont = 0
while True:
    name = str(input('Type your name:'))
    grade1 = float(input('Type a grade 1:'))
    grade2 = float(input('Type a grade 2:'))
    average = (grade1 + grade2) / 2
    all.append([name, [grade1, grade2], average])
    cont += 1
    check = input('Do you want continue?(y/n)')
    if check in 'nN':
        break
for i, c in enumerate(all):
    print(f'N°{i:<3} Name:{c[0]:10}Average:{c[2]:<8}')
while True:
    check = int(input('Do you wanna see the grades of which student?(999 to stop):'))
    if check == 999:
        break
    if check <= len(all):
        print(f'The grades of {all[check][0]} are:{all[check][1]}')
