from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 51')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, bem vindo ao nosso programa de matemática!')
print('''Aqui, você poderá ver os dez primeiros termos de uma progrssão aritmética que quiser!
Para isso, basta apenas nos informar o primeiro termo da progressão e a sua razão.''')

termo1 = int(input('\nDigite, a seguir, o primeiro termo da progressão: '))
razao = int(input('Agora, digite a razão desejada para a progressão: '))

contador = 1
soma = termo1
expressao = ''

while contador < 10:
    expressao = expressao + f'{soma} + '
    soma = soma + razao
    contador = contador + 1

print(f'''\nA progressão que inicia-se no termo: {colors['blue']}{termo1}{Style.RESET_ALL}, e de razão: {colors['blue']}{razao}{Style.RESET_ALL},
pode ser escrita da seguinte forma: {Style.BRIGHT}{colors['yellow']}{expressao}{termo1*10}{Style.RESET_ALL}.''')

pergunta = str(input(f'\nDigite {colors['blue']}[S]{Style.RESET_ALL} para escolher um outro número de termos para essa progressão ou {colors['red']}[N]{Style.RESET_ALL} para finalizar o programa: ')).lower()

if pergunta == 'n':
    print('\nTudo bem! Programa finalizado!')
else:
    termos = int(input('\nÓtimo! nos informe qual é o número de termos que você deseja: '))
    while contador < termos:
        expressao = expressao + f'{soma} + '
        soma = soma + termo1
        contador = contador + 1
    print(f'''\nA nova progressão que inicia-se no termo: {colors['blue']}{termo1}{Style.RESET_ALL}, e de razão: {colors['blue']}{razao}{Style.RESET_ALL},
pode ser escrita da seguinte forma: {Style.BRIGHT}{colors['yellow']}{expressao}{termo1*termos}{Style.RESET_ALL}.''')
