from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 59')
print(f'-=-{Style.RESET_ALL}'*6)

print('\nSeja muito bem-vindo ao Super Mercado Fella Cut LTDA.')
print('-'*55)

soma = contador = totalmil =  0
barato = ''
menor = None

while True:
    nome = str(input('Insira o nome do produto desejado: '))
    preco = float(input('insira o valor do produto desejado: R$'))

    soma = soma + preco

    if preco > 1000:
        totalmil = totalmil + 1

    if menor is None:
        menor = preco
        barato = nome
    elif preco < menor:
        menor = preco
        barato = nome

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Você deseja continuar comprando? [S/N]: ')).strip()[0].lower()
        print('-'*55)
    if resposta == 'n':
        break

print('\n')
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'''O valor total da compra foi de: R${soma:.2f}.
Temos {totalmil} produtos que custam mais de R$1000.00.
O produto mais barato foi: {barato}, custando R${menor:.2f}.''')
