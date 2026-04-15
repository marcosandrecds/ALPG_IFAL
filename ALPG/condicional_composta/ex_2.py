'''
Q2. O cardápio de uma lanchonete é o seguinte:
Especificação
Código
Preço
Cachorro quente
100
1,20
Bauru simples
101
1,30
Bauru com ovo
102
1,50
Hambúrger
103
1,20
Cheeseburguer
104
1,30
Refrigerante
105
1,00

Escreva um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um item.
Caso o valor do código seja inválido, informar.
'''

print("Cardápio")
print("100 - Cachorro quente - R$ 1.20")
print("101 - Bauru simples - R$ 1.30")
print("102 - Bauru com ovo - R$ 1.50")
print("103 - Hambuguer - R$ 1.20")
print("104 - Cheeseburguer - R$ 1.30")
print("105 - Refrigerante - R$ 1.00")

codigo = int(input("Digite o código do produto: "))
qtd = int(input("Digite a quantidade que deseja: "))

valor_a_pagar = 0

if codigo == 100:
    valor_a_pagar = qtd * 1.20
elif codigo == 101:
    valor_a_pagar = qtd * 1.30
elif codigo == 102:
    valor_a_pagar = qtd * 1.50
elif codigo == 103:
    valor_a_pagar = qtd * 1.20
elif codigo == 104:
    valor_a_pagar = qtd * 1.30
elif codigo == 105:
    valor_a_pagar = qtd * 1.0
else:
    print("Código do produto inválido!")

if valor_a_pagar != 0:
    print(f"Valor a pagar: {valor_a_pagar}")