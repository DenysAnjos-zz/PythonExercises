# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. no final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
from time import sleep
test = list()

all = list()
totalStudents = 0

check = 's'
while check not in 'nN':
    names = list()
    grades = list()
    media_notas = list()
    total_notas = 0
    n = str(input('Name:'))
    names.append(n)
    note1 = float(input('Grade 1:'))
    grades.append(note1)
    note2 = float(input('Grade 2:'))
    grades.append(note2)
    names.append(grades)
    total_notas = (note1 + note2) / 2
    names.append(total_notas)
    all.append(names[:])
    totalStudents += 1

    check = str(input('Do you want continue?(y/n) '))

print(f'N°   NAME    AVERAGE')
for a in range(0, totalStudents):
    print(f'{a}  {all[a].__getitem__(0)}  {all[a].__getitem__(2)} ')
    sleep(0.5)

check = int(input('Do you wanna show grades of which student? (999 to stop):'))
while check != 999:
    print(f'The grades of {all[check].__getitem__(0)} is {all[check].__getitem__(1)}')
    check = int(input('Do you wanna show grades of which student? (999 to stop):'))

