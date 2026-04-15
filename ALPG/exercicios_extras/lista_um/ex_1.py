'''
Q1. Controle de Acesso por Altura e Idade
Um parque de diversões tem uma regra de segurança:
para andar na montanha-russa, a criança deve ter pelo menos 12 anos e medir no mínimo 1.50m de altura.
Escreva um programa que leia a idade e a altura e informe se ela pode ou não subir no brinquedo.
'''

print('Controle de Acesso por Altura e Idade')
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura em metros: "))

if idade >= 12:
    if altura >= 1.50:
        print("Pode subir no brinquedo!")
    else:
        print("Não pode subir no brinquedo, altura mínima não atingida.")
else:        
    print("Não pode subir no brinquedo, idade mínima não atingida.")