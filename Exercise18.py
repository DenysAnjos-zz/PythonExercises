# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente
import math
angle = float(input('Type a angle:'))
sine = float(math.sin(math.radians(angle)))
cosine = float(math.cos(math.radians(angle)))
tangent = float(math.tan(math.radians(angle)))
print('Sine:{:.2f}\nCosine:{:.2f}\nTangent:{:.2f}'.format(sine, cosine, tangent))
