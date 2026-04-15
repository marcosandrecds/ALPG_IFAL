'''
Q6. Elabore um algoritmo que verifica e informa se a pessoa pode concorrer à vaga de cotista em uma universidade.
Para isso, solicite duas informações do usuário. A primeira: se a pessoa está cadastrada no Bolsa Família (S ou N);
e a segunda: se possui mais de três filhos (S ou N).
Para concorrer à vaga de cotista, deve estar cadastrado no Bolsa Família ou ter mais de 3 filhos.
'''

print('Vaga de cotista')
bolsa_familia = int(input('Você está cadastrado no programa Bolsa Família?\n1- Sim\n2- Não\n'))
quantidade_filhos = int(input('Você possui mais de 3 filhos?\n1- Sim\n2- Não\n'))

if bolsa_familia == 1:
    print('Você pode concorrer, por estar cadastrado no Bolsa Família.')

if bolsa_familia != 1:
    if quantidade_filhos == 1:
        print('Você pode concorrer à vaga de cotista, por possuir 3 ou mais filhos.')
    else:
        print('Você não pode concorrer à vaga de cotista por não atender nenhum requisito nescessário.')