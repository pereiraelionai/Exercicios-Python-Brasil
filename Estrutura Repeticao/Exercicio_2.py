while True:
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')

    if not usuario == senha:
        print('Cadastro realizado com sucesso!')
        break
    print('A senha não pode ser igual ao usuário')
