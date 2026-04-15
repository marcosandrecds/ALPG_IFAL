'''
Q3. Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do usuário, e a senha.
Depois, pede que o usuário confirme novamente a senha.
O sistema deverá verificar se as senhas digitadas são iguais e se o nome do usuário foi informado.
Se forem iguais e o nome do usuário tiver sido preenchido, informar que o cadastro está correto.
Se não, pedir para verificar os dados digitados.
'''

print('Cadastro de usuário')
usuario = str(input('Digite o nome de usuário: '))
senha = int(input('Digite a senha: '))
confirmacao_senha = int(input('Digite a confirmação da senha: '))

if usuario != '':
    if senha == confirmacao_senha:
        print('Cadastro está correto.')
    else:
        print('Verificar os dados digitados, senha está divergente.')
else:
    print('Verificar os dados digitados, nome de usúario inválido.')