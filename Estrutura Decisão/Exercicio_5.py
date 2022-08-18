nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
mensagem = ''

if media == 10:
    mensagem = 'Aprovado com distinção'
elif media >= 7:
    mensagem = 'Aprovado'
else:
    mensagem = 'Reprovado'

print(mensagem)
