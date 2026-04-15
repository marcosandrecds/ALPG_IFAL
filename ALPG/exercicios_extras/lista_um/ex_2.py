'''
Q2. Classificação de Produtos (Peso)
Crie um algoritmo que leia o peso de um produto (em gramas) e o classifique em:
Leve: Até 250g.
Médio: Acima de 250g até 500g.
Pesado: Acima de 500g até 1000g.
Carga Especial: Acima de 1000g.
Nota: Se o peso for zero ou negativo, informe "Peso Inválido".
'''

print('Classificação de Produtos')
peso = float(input("Digite o peso do produto (em gramas): "))

if peso <= 0:
    print("Peso Inválido")
elif peso <= 250:
    print("Leve")
elif peso <= 500:
    print("Médio")
elif peso <= 1000:
    print("Pesado")
else:
    print("Carga Especial")