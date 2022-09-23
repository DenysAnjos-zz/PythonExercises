# Elabore um programa que calcule o valor a
# ser pago por um produto. considerando o
# seu preço normal e condição de pagamento:
# A vista dinheiro / cheque: 10% de desconto.
# A vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.
price = float(input('Type the product price:'))
method = str(input('Whats the payment methods? card, check, money?')).lower()
if method == 'card':
    inst = int(input('Type the number os installments:'))
    if inst <= 2:
        price = price - (price * (5 / 100))
    else:
        price = price + (price*(20/100))
else:
    price = price - (price * (10 / 100))
print('Total to pay:{:.2f}'.format(price))
