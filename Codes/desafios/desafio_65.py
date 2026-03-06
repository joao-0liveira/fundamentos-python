from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

lista = (
    'Pizza de Calabrasa Mineira', 82.00,
    'Pizza de Frango com Bacon', 98.00,
    'Pizza de 4 Queijos', 94.00,
    'Pizza de Lombo com Requeijão', 94.00,
    'Pizza Marguerita', 80.00,
    'Pizza de Muçarela', 75.00,
    'Pizza de Pepperoni', 88.00,
    'Pizza Portuguesa', 96.00,
)

print('-'*42)
print(f'{'Cardápio Pizza na Roça':^42}')
print('-'*42)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{Style.BRIGHT}{lista[posicao]:.<35}{Style.RESET_ALL}', end='')
    else:
        print(f'{colors['yellow']}R${lista[posicao]:>}{Style.RESET_ALL}')
print('-'*42)
