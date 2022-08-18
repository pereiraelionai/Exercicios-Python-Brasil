produto_1 = float(input('Digite o preço do produto 1: '))
produto_2 = float(input('Digite o preço do produto 2: '))
produto_3 = float(input('Digite o preço do produto 3: '))

if produto_1 == produto_2 and produto_1 == produto_3:
    print('Os preços são iguais.')
else:
    if produto_1 < produto_2 and produto_1 < produto_3:
        print('Compre o produto 1')
    elif produto_2 < produto_3:
        print('Compre o produto 2')
    else:
        print('Compre o produto 3')
