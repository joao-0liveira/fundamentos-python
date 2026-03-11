resposta = ''
geral = []

while True:
    print('-'*36)
    nome = (str(input('Digite o nome do aluno a seguir: ')))
    nota1 = (float(input('Digite a sua 1a nota: ')))
    nota2 = (float(input('Digite a sua 2a nota: ')))
    media = (nota1 + nota2) /  2
    geral.append([nome, [nota1, nota2], media])

    resposta = str(input('Você deseja continuar? [S/N]: '))
    if resposta in 'Nn':
        break

print('-='*30)
print(f'{'No':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)

for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')

print('-'*30)

while True:
    print('-'*30)
    pgt = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if pgt == 999:
        break

    if pgt <= len(geral)-1:
        print(f'As notas de {geral[pgt][0]} são: {geral[pgt][1]}.')

print('PROGRAMA FINALIZADO!')