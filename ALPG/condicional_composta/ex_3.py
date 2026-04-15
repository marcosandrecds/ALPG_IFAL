'''
Q3. Escreva um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre.
Calcular a sua média (aritmética), informar o nome e o resultado final:
Aprovado (media >= 7),
Reprovado (media <= 5),
ou em Recuperação (media entre 5.1 a 6.9).
'''

nome = input("Digite o nome do estudante: ")

nota1 = float(input("Digite a 1a nota: "))
nota2 = float(input("Digite a 2a nota: "))
nota3 = float(input("Digite a 3a nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"{nome}: Aprovado")
elif media <= 5:
    print(f"{nome}: Reprovado")
else:
    print(f"{nome}: Em recuperação")