'''
Q4. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira;
para isso, simule 3 produtos e informe seus respectivos preços unitários.
Depois pergunte a quantidade que deseja comprar de cada produto.
Calcule o valor a pagar. Mas no momento do pagamento, perguntar como o cliente irá pagar:
em dinheiro ou Pix (terá 10% de desconto) ou cartão (sem desconto).
Informe o valor final a pagar.
'''

print('Compras da feira')
print('R$ 1,50 - Banana\nR$ 2,00 - Maçã\nR$ 3,00 - Uva')
banana = int(input('De quantas bananas você gostaria? '))
maca = int(input('De quantas maças você gostaria? '))
uva = int(input('De quantas uvas você gostaria? '))
conta = banana * 1.5 + maca * 2 + uva * 3

print(f'O valor parcial da conta é R$ {conta}.')

pagamento = int(input('Qual a forma de pagamento?\n1- Dinheirou ou Pix\n2- Cartão de crédito\n'))

if pagamento == 1:
    print(f'O valor final da compra é {conta - (conta * 0.1)}.')
else:
    print (f'O valor final da conta é {conta}.')