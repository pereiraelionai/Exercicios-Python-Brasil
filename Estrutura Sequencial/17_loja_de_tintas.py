from math import ceil

metros_pintar = int(input('Quantos metros quadrados devem ser pintados? '))
litros_necessarios = (metros_pintar * 1.1) / 6
latas_18 = ceil(litros_necessarios / 18)
latas_36 = ceil(litros_necessarios / 3.6)
latas_18_eco = 0
latas_36_eco = 0
preco_18 = 80
preco_36 = 25
resto = 0
if litros_necessarios >= 18:
    latas_18_eco = litros_necessarios // 18
    resto = litros_necessarios % 18
    if resto > 10.8:
        resto = 0
        latas_18_eco += 1
    print(resto)
if resto != 0:
    latas_36_eco = ceil(resto / 3.6)
if preco_18 * latas_18 < preco_36 * latas_36 and latas_18 == 1:
    latas_18_eco = 1
if latas_36_eco == 0 and preco_18 * latas_18 > preco_36 * latas_36:
    latas_36_eco = latas_36
print()
print(f'Para pintar {metros_pintar} metros quadrados você pode optar por latas de 18 litros ou 3,6 litros conforme quantidade abaixo:')
print(f'Latas de 18 litros: {int(latas_18)} lata(s) - Preço: R$ {preco_18 * latas_18:.2f}')
print(f'Latas de 3,6 litros: {int(latas_36)} lata(s) - Preço: R$ {preco_36 * latas_36:.2f}')
print(f'\033[1;33mSua melhor opção de compra é: \033[m')
print(f'Latas de 18 litros: {int(latas_18_eco)} lata(s)')
print(f'Latas de 3,6 litros: {int(latas_36_eco)} lata(s)')
print(f'Preço total: R$ {(latas_18_eco * preco_18) + (latas_36_eco * preco_36):.2f}')
