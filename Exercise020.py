# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle

st1 = str(input('First student:'))
st2 = str(input('Second student:'))
st3 = str(input('Third student:'))
st4 = str(input('Fourth student:'))
list = [st1, st2, st3, st4]
shuffle(list)
print('Order of presentation:')
print(list)