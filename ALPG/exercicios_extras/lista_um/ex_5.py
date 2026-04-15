'''
Q5. Simulador de Semáforo Inteligente
Crie um programa que pergunte ao usuário o estado do semáforo (1-Verde, 2-Amarelo, 3-Vermelho) e se há pedestres atravessando (1-Sim, 2-Não).
Se o sinal estiver Verde e não houver pedestres, exiba "Pode passar".
Se o sinal estiver Verde, mas houver pedestres, exiba "Aguarde os pedestres".
Se o sinal estiver Amarelo, exiba "Atenção, reduza a velocidade".
Se o sinal estiver Vermelho, exiba "Pare o veículo".
'''

print('Simulador de Semáforo')
semaforo = int(input('Digite o estado do semáforo.\n1- Verde\n2- Amarelo\n3- Vermelho\n'))
pedestres = int(input('Há pedestres atravessando?\n1- Sim\n2- Não\n'))

if semaforo == 1:
    if pedestres == 1:
        print('Aguarde os pedestres.')
    else:
        print('Pode passar.')
elif semaforo == 2:
    print('Atenção, reduza a velocidade.')
elif semaforo == 3:
    print('Pare o veículo.')
else:
    print('Opção inválida.')