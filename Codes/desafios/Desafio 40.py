print('-=-'*6)
print(' '*2, 'DESAFIO 40')
print('-=-'*6)
print('''Bem vindo ao nosso programa!
Aqui você poderá escolher SEIS números inteiros quaisquer e mostraremos a soma dos números pares que você escolher.''')
soma = 0
qtde = 0
for c in range(1, 7):
    números = int(input('Digite um valor a seguir: '))
    if números % 2 == 0:
        soma += números
        qtde +=  1
print(f'A soma dos {qtde} números pares digitados é igual a: {soma}')
