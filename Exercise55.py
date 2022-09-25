# Faça um programa que leia o peso
# de cinco pessoas. No final mostre
# qual foi o maior e o menor peso lido
lighter = int()
haviest = int()
check = float(input('Type your weight in KG:'))
lighter = check
for c in range(0, 4):
    check = float(input('Type your weight in KG:'))
    if check < lighter:
        lighter = check
    elif check > haviest:
        haviest = check
print('Haviest:KG {}'.format(haviest))
print('Lighter:KG {}'.format(lighter))
