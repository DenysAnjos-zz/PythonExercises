# Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado
# a multa vai custar R$7,00 por cada km acima do limite
speed = int(input('Type your speed:'))
if speed <= 80:
    print('You were not fired!')
else:
    print('Fine amount:R${}'.format((speed-80)*7))
