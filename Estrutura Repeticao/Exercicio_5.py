while True:
    try:
        populacao_a = input('Digite a quantidade da população A: ')
        taxa_a = float(input('Digite a taxa de crescimento da população A (%): '))
        populacao_b = input('Digite a quantidade da população B: ')
        taxa_b = float(input('Digite a taxa de crescimento da população B (%): '))
        anos = 0

        if populacao_a.isnumeric() and populacao_b.isnumeric():
            populacao_a = round(int(populacao_a))
            populacao_b = round(int(populacao_b))
        else:
            print('População inválida, digite um número inteiro positivo.')
            continue

        if taxa_b >= taxa_a and populacao_b >= populacao_a:
            print('A população A jamais alcançará a populção B.')
            continue

        if taxa_a >= taxa_b and populacao_a >= populacao_b:
            print('A população B jamais alcançará a população A.')
            continue

        if taxa_a <= 0 or taxa_b <= 0:
            print('Não permitido valores negativos ou igual a 0.')
            continue

        taxa_a = taxa_a/100
        taxa_b = taxa_b/100

        while True:
            populacao_a += populacao_a * taxa_a
            populacao_b += populacao_b * taxa_b
            print(f'População A: {populacao_a:.2f}\nPopulação B: {populacao_b:.2f}')
            print('------------------------------------')
            anos += 1
            if populacao_a > populacao_b:
                break
        print(f'Será necessário {anos} anos para a população menor ultrapassar a população maior.')
    except ValueError:
        print('Digite uma taxa válida, apenas números.')
