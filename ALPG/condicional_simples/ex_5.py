'''
Q5. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de uma feira,
que só permite a compra se a pessoa tiver dinheiro para pagar à vista 
e estiver com a anuidade da associação de produtor rural em dia. 
'''

print('Compras da feira')
pagamento = int(input('Você pagar à vista?\n1- Sim\n2- Não\n'))
anuidade = int(input('A sua anuidade está em dia?\n1- Sim\n2- Não\n'))

if pagamento == 1:
    if anuidade == 1:
        print('Você pode participar da feira.')
    else:
        print('Você não pode participar da feira, regularize sua anuidade.')
else:
    print('Aceitamos apenas pagamento à vista.')