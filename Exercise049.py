# Refaça o desafio 09 mostrando a tabuada
# de um número que o usuário escolher, só
# que agora utilizando um laço for.
n = int(input('Type a integer:'))
for c in range(1, 11):
    print('{:2} * {} = {:2}'.format(c, n, (c*n)))
