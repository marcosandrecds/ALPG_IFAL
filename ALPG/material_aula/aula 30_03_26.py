'''1) Programa de conversão de temperaturas.
Solicita a entrada temperatura em grau Celsius, e mostra a conversão Kelvin e Farenheit.
'''

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_kelvin = temp_celsius + 273
temp_farenheit = temp_celsius * 1.8 + 32

#Efetuando as conversões
temp_kelvin = temp_celsius + 273
temp_farenheit = temp_celsius * 1.8 + 32

print(f"A temperatura de {temp_celsius} Celsius equivale a {temp_kelvin} Kelvin");
print(f"A temperatura de {temp_celsius} Celsius equivale a {temp_farenheit} Farenheit");

''''
2) Programa que converte tempo.
Solicita a entrada do tempo em horas e mostra a conversão para minutos e segundos.

tempo_minutos = tempo_horas * 60
tempo_segundos = tempo_horas * 3600
'''

tempo_horas = float(input("Digite o tempo em horas: "));

tempo_minutos = tempo_horas * 60
tempo_segundos = tempo_horas * 3600

print(f"{tempo_horas} hora(s) equivale a {tempo_minutos} minutos");
print(f"{tempo_horas} hora(s) equivale a {tempo_segundos} segundos");

'''
3) Dada a entrada de 4 notas, calcule a média e mostre a situação final do estudante:
> Aprovado: quando a média é maior ou igual a 6;
> Reprovado: quando a média é menor que 6.

Saída esperada:
> Média é igual a {media}.
> Situação: {aprovado ou reprovado}
'''

nota1 = float(input("Digite a 1a nota: "));
nota2 = float(input("Digite a 2a nota: "));
nota3 = float(input("Digite a 3a nota: "));
nota4 = float(input("Digite a 4a nota: "));

media = (nota1 + nota2 + nota3 + nota4) / 4;

if media >= 6:
    print("Aprovado");
else:
    print("Reprovado");

'''
4. Dada a entrada de um número inteiro de 1 a 7.
Escreva o dia da semana correspondente, sabendo que 1 representa o domingo.
Se o número não for válido (não for de 1 a 7), escreva: Número inválido.
'''

dia_da_semana = int(input("Digite um número de 1 a 7: "));

if dia_da_semana == 1:
    print("Domingo");
elif dia_da_semana == 2:
    print("Segunda");
elif dia_da_semana == 3:
    print("Terça");
elif dia_da_semana == 4:
    print("Quarta");
elif dia_da_semana == 5:
    print("Quinta");
elif dia_da_semana == 6:
    print("Sexta");
elif dia_da_semana == 7:
    print("Sábado");
else:
    print("Número inválido");
