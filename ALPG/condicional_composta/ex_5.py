'''
Q5. Dados três valores, verificar se eles podem ser os comprimentos dos lados de um triângulo e, se forem verificar se é um triângulo equilátero, isósceles ou escalenos. Se eles não formarem um triângulo, escrever a mensagem "Esses lados não formam um triângulo". Se formarem um triângulo, informar qual o tipo.

Considere as seguintes propriedades: 
O comprimento de cada lado em um triângulo é menor que a soma dos outros dois lados; 
Equiláteros: tem os comprimentos dos três lados iguais;
Isósceles: tem os comprimentos de dois lados iguais; 
Escaleno: tem os comprimentos dos três lados diferentes.
'''

print('Verificar se os lados formam um triângulo e qual o tipo')
lado1 = float(input("Digite o comprimento do 1o lado: "))
lado2 = float(input("Digite o comprimento do 2o lado: "))
lado3 = float(input("Digite o comprimento do 3o lado: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if (lado1 == lado2) and (lado2 == lado3):
        print("Triângulo equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Esses lados não formam um triângulo")