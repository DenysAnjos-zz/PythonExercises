# Refaça o desafio 035 dos triângulos,
# acrescentando o recurso de mostrar
# que tipo de triangulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
l1 = float(input('Type a first length:'))
l2 = float(input('Type a second length:'))
l3 = float(input('Type a third length:'))
if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print('Its not a triangle!')
elif l1 == l2 == l3:
    print("Is an equilateral triangle!")
elif l1 != l2 != l3 != l1:
    print('Is a isosceles triangle!')
else:
    print('Is an scalene triangle!')
