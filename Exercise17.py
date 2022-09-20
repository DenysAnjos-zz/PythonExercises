# Faça um programa que leia o comprimeiro do cateto oposto
# e do cateto adjacente de um triangulo retangulo, calcule
# e mostre o comprimento da hipotenusa.

from math import hypot
oppositeSide = float(input('Type a opposite side length:'))
adjacentSide = float(input('Type a adjacent side length:'))
hypotenuse = hypot(oppositeSide, adjacentSide)
print('Hypotenuse:{:.2f}'.format(hypotenuse))