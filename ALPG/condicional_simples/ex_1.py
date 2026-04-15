'''
Q1. Faça um algoritmo que lê dois números, depois verifica se os dois números são iguais.
Se forem iguais, escrever "São iguais", se não, escrever "São diferentes".
'''

print('Verificação de números')
numero_um = int(input('Digite um número inteiro: '))
numero_dois = int(input('Digite outro número inteiro: '))

if numero_um == numero_dois:
    print(f'O número {numero_um} é igual ao número {numero_dois}.')
else:
    print(f'O número {numero_um} é diferente do número {numero_dois}.')