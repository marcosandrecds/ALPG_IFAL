'''
Q4. Elabore um algoritmo que leia 5 valores inteiros e apresente na tela o maior e o menor deles. 
'''

print("Apresentar maior e menor número")

num1 = int(input("Digite o 1o número: "))
num2 = int(input("Digite o 2o número: "))
num3 = int(input("Digite o 3o número: "))
num4 = int(input("Digite o 4o número: "))
num5 = int(input("Digite o 5o número: "))

maior = 0
menor = 0

#MAIOR
if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            if num1 > num5:
                maior = num1

if num2 > num1:
    if num2 > num3:
        if num2 > num4:
            if num2 > num5:
                maior = num2

if num3 > num1:
    if num3 > num2:
        if num3 > num4:
            if num3 > num5:
                maior = num3

if num4 > num1:
    if num4 > num2:
        if num4 > num3:
            if num4 > num5:
                maior = num4

if num5 > num1:
    if num5 > num2:
        if num5 > num3:
            if num5 > num4:
                maior = num5

#MENOR

if num1 < num2:
    if num1 < num3:
        if num1 < num4:
            if num1 < num5:
                menor = num1

if num2 < num1:
    if num2 < num3:
        if num2 < num4:
            if num2 < num5:
                menor = num2

if num3 < num1:
    if num3 < num2:
        if num3 < num4:
            if num3 < num5:
                menor = num3

if num4 < num1:
    if num4 < num2:
        if num4 < num3:
            if num4 < num5:
                menor = num4

if num5 < num1:
    if num5 < num2:
        if num5 < num3:
            if num5 < num4:
                menor = num5


print(f"Maior: {maior}")
print(f"Menor: {menor}")