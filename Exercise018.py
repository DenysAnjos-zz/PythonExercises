# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente
from math import sin, cos, tan, radians
angle = float(input('Type a angle:'))
sine = float(sin(radians(angle)))
cosine = float(cos(radians(angle)))
tangent = float(tan(radians(angle)))
print('Sine:{:.2f}\nCosine:{:.2f}\nTangent:{:.2f}'.format(sine, cosine, tangent))
