# Escreva um programa que leia um valor em metros e o
# exiba convertido em milimetros, centimetros, decimetros, metros, decametros, hectometros, km  #
meter = float(input('Type a value in meters:'))
print('mm:{:.1f}'.format(meter*1000))
print('cm:{:.1f}'.format(meter*100))
print('dm::{:.1f}'.format(meter*10))
print('dam:{:.1f}'.format(meter/10))
print('hm:{:.2f}'.format(meter/100))
print('km:{:.3f}'.format(meter/1000))
