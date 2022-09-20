# 4) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Km traveled:'))
days = float(input('Rented days:'))
total = (km*0.15) + (days*60)
print("Total payable:R${:.2f}".format(total))
