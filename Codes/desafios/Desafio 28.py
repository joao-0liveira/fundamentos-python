print('-=-'*6)
print(' '*2, 'DESAFIO 28')
print('-=-'*6)
print('''Olá! Seja muito bem-vindo ao nosso programa de comparação númerica!
Aqui você poderá digitar dois números inteiros quaisquer e o nosso programa irá dizer qual é o maior.''')
primeiro = int(input('Para começarmos, digite o primeiro valor a seguir: '))
segundo = int(input('Ótimo, agora, digite o segundo valor a seguir: '))
print(f'O nosso sistema já captou os valores desejados para análise, são eles: {primeiro} e {segundo}.')
if primeiro > segundo:
    print(f'Logo, entre os dois números desejados, o primeiro valor digitado, ou seja: {primeiro}, é o maior entre eles.')
elif segundo > primeiro:
    print(f'Analisando os valores digitados pelo usuário, o segundo valor digitado, ou seja: {segundo}, é o maior entre eles.')
else:
    print(f'Entre os dois valores digitados, são eles: {primeiro} e {segundo}, não há maior ou menor, pois são iguais.')
