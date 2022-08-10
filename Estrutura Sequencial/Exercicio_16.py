from math import ceil
metros = float(input('Quantos m² devem ser pintados? '))
qtd_tinta = metros/3
preco_lata = 80

latas = qtd_tinta / 18
if latas < 1:
    latas = 1
latas = ceil(latas)

preco_total = preco_lata * latas
print(f'Para pintar {metros} m² você precisa de {latas} latas de tinta. O custo será de R${preco_total}.')
