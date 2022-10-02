# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m2
width = float(input('Wall width:'))
height = float(input('Wall height:'))
area = width*height
print('The area is: {:.1f} and {:.1f} liters of paint will be needed.'.format(area, (area*0.5)))


