'''
Q3. Calculadora de Reajuste Salarial
Uma empresa dará aumento aos funcionários conforme o cargo informado via código:
Código 1 (Estagiário): 10% de aumento.
Código 2 (Analista): 7% de aumento.
Código 3 (Gerente): 5% de aumento. Qualquer outro código deve ser tratado como "Código não encontrado".
O programa deve ler o código e o salário atual, exibindo o novo salário.
'''

print('Calculadora de Reajuste Salarial')
codigo = int(input('Digite o código do cargo\n1- Estagiário\n2- Analista\n3- Gerente\n'))
salario = float(input('Digite o salário atual: '))

if codigo == 1:
    novo_salario = salario * 1.10
    print(f'o novo salário do Estagiário é {novo_salario}.')
elif codigo == 2:
    novo_salario = salario * 1.07
    print(f'o novo salário do Analista é {novo_salario}.')
elif codigo == 3:
    novo_salario = salario * 1.05
    print(f'o novo salário do Gerente é {novo_salario}.')
else:
    print("Código não encontrado")