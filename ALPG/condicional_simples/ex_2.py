'''
Q2. Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou igual ao segundo número.
Se for, escrever "O número {valor do número 1} é maior ou igual ao número {valor do número 2}".
Se não, escrever "O número {valor do número 1} é menor que número {valor do número 2}".
'''

print('Verificação de números')
numero_um = int(input('Digite um número inteiro: '))
numero_dois = int(input('Digite outro número inteiro: '))

if numero_um >= numero_dois:
    print(f'O número {numero_um} é maior ou igual ao número {numero_dois}.')
else:
    print(f'O número {numero_um} é menor que o número {numero_dois}.')