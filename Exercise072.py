# Crie um programa que tenha uma tupla totalmente
# preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo
# teclado(entre 0 e 20) e mostrá-lo por extenso
number = (0, 21)
position = ('zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine',
           'ten', 'eleven', 'twelve', 'thirteen',
           'fourteen', 'fifteen', 'sixteen',
           'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    check = int(input('Type a number:'))
    if check > -1 and check < 21:
        for number in range(1):
            print('You type the number between 0 and 20:', position[check])
        break
    else:
        print('Error!, try again')
