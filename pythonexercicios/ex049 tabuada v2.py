# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.#
num= int(input('digite o numero para ver a sua tabuada: '))
for c in range(1, 11):
    print(num,' X ', c, '= ', num*c)