from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 50')
print('-=-'*6)

print(f'''\n{Style.RESET_ALL}Olá, seja bem-vindo ao nosso programa de matemática!
Aqui, você teá a oportunidade de fazer o calculo de qualquer número em fatorial que quiser!
Para continuar, basta inserir o número de sua escolha na caixa de resposta.''')

número = int(input('\nDigite, a seguir, um número de sua escolha: '))

resultado = 1
contas = número
expressão = ''

while contas > 1:
    expressão = expressão + f' {contas} x'
    resultado = resultado * contas
    contas = contas - 1 

expressão = expressão + ' 1'

print(f'\nO resultado de {número}! é:{expressão} = {resultado}')
