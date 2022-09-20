# um professor quer sortear um dos seus quatro alunos para apgar o quadro,
# faça um programa que ajuda ele lendo o nome deles e escrevendo o nome do escolhido
from random import choice

student1 = str(input('Type your name:'))
student2 = str(input('Type your name:'))
student3 = str(input('Type your name:'))
student4 = str(input('Type your name:'))
list = [student1, student2, student3, student4]
drawn = choice(list)
print('Student drawn:', drawn)
