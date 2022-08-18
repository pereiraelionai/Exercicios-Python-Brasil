turno = input('Digite o seu turno M-Matutino, V-Vespertino, N-Noturno: ').upper()

match turno:
    case 'M':
        print('Bom dia!')
    case 'V':
        print('Boa tarde!')
    case 'N':
        print('Boa noite!')
    case _:
        print('Turno inválido!')
