from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 49')
print('-=-'*6)

print(f'\n{Style.RESET_ALL}Olá! Seja Bem vindo ao nosso programa!')
print('Aqui você poderá escolher dois números inteiros e o nosso programa lhe mostrará um menu com as possibilidades disponúveis.')

primeiro = int(input('\nPara começarmos, digite o primeiro número a seguir: '))
segundo = int(input('Ótimo, agora escolha o segundo número: '))
 
print('\nSegue nosso menu: ')

escolha = 0

while escolha != 5:
    print(f'''\n{Style.BRIGHT}{colors['blue']}[1]{Style.RESET_ALL} {Style.BRIGHT}Somar
{colors['blue']}[2]{Style.RESET_ALL} {Style.BRIGHT}Multiplicar
{colors['blue']}[3]{Style.RESET_ALL} {Style.BRIGHT}Maior
{colors['blue']}[4]{Style.RESET_ALL} {Style.BRIGHT}Novos números
{colors['blue']}[5]{Style.RESET_ALL} {Style.BRIGHT}Sair do programa{Style.RESET_ALL}''')

    escolha = int(input('→ Qual a sua escolha? '))

    while escolha == 0 or escolha > 5:
        escolha = int(input('Número inválido, por favor digite outro número: '))
    
    if escolha == 1:
        print(f'Você escoheu a {colors['red']}SOMA{Style.RESET_ALL} entre os valores {primeiro} e {segundo}, que é igual a: {Style.BRIGHT}{primeiro+segundo}{Style.RESET_ALL}.')
        print('-'*65)
    
    elif escolha == 2:
        print(f'Você escolheu a {colors['red']}MULTIPLICAÇÃO{Style.RESET_ALL} entre os números {primeiro} e {segundo}, que é igual a: {Style.BRIGHT}{primeiro*segundo}{Style.RESET_ALL}.')

    elif escolha == 3:
        print(f'Comparando os valores {primeiro} e {segundo}, o {colors['red']}MAIOR{Style.RESET_ALL} número é: {Style.BRIGHT}{max(primeiro, segundo)}{Style.RESET_ALL}.')

    elif escolha == 4:
        primeiro = int(input('Escolha novamente um primeiro número: '))
        segundo = int(input('Agora, escolha novamente um segundo número: '))

print('\nTudo bem! Programa finalizado!')
