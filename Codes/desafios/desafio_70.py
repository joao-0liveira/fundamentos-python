from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW
}

lista = []

while True:
    print('-'*35)
    numeros = int(input('Digite um número a seguir: '))
    lista.append(numeros)

    pergunta = ''
    pergunta = str(input(f'Você deseja continuar? [{colors['green']}S{Style.RESET_ALL}/{colors['red']}N{Style.RESET_ALL}]: '))
    if pergunta in 'Nn':
        break

print(f'''\nDe acordo com os dados coletados, fizemos uma lista com os seguintes números fornecidos: {colors['yellow']}{lista}{Style.RESET_ALL}.
1- A {colors['blue']}quantidade de números{Style.RESET_ALL} digitados foi de: {colors['yellow']}{len(lista)}{Style.RESET_ALL},
2- A lista de valores, ordenada de forma {colors['blue']}decrescente{Style.RESET_ALL} fica da seguintye forma: {colors['yellow']}{sorted(lista, reverse=True)}{Style.RESET_ALL},''')

if 5 in lista:
    print(f'3- O valor "{colors['blue']}5{Style.RESET_ALL}" {colors['yellow']}está{Style.RESET_ALL} na lista.')
else:
    print(f'3- O valor "{colors['blue']}5{Style.RESET_ALL}" {colors['yellow']}não está{Style.RESET_ALL} na lista.')
