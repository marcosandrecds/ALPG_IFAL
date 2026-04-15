'''
Q1. Elabore um algoritmo que, dada a idade de um nadador, o classifica em uma das seguintes categorias:
 
Infantil A = 5 - 7 anos
Infantil B = 8-10 anos
Juvenil A = 11-13 anos
Juvenil B = 14-17 anos
Adulto = Maior ou igual a 18 anos

Se não estiver enquadrado em nenhuma categoria, não poderá competir.
'''

idade = int(input("Digite a idade do nadador: "))

if idade < 5:
    print("Não poderá competir")
elif idade <= 7:
    print("Infantil A")
elif idade <= 10:
    print("Infantil B")
elif idade <= 13:
    print("Juvenil A")
elif idade <= 17:
    print("Juvenil B")
else:
    print("Adulto")