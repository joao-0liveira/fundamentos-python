print('-=-'*6)
print(' '*2, 'DESAFIO 39')
print('-=-'*6)
print('''Bem vindo ao nosso programa de calculadora virtual!
Aqui você poderá escolher um número inteiro qualquer e nosso programa irá lhe mostrar a sua respectiva tabuada.''')
escolha = int(input('Para continuarmos, digite, a seguir, um número de sua escolha: '))
print(f'Ótimo, o número escolhido foi: {escolha}. Segue a sua tabuada: ')
print('='*15)
for c in range(1, 11):
    print(f'{c} x {escolha} = {escolha*c}')
print('='*15)
