import random
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

contador = 1
lista = ()
sorteio = random.sample(range(1, 10), k=5)

lista = sorteio

print(f'\nOs valores sorteados foram: {colors['yellow']}{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}{Style.RESET_ALL} e {colors['yellow']}{lista[4]}{Style.RESET_ALL}.')
print(f'\n1-O {colors['blue']}MAIOR{Style.RESET_ALL} número sorteado é: {colors['yellow']}{max(lista)}{Style.RESET_ALL}.')
print(f'2- O {colors['red']}MENOR{Style.RESET_ALL} número sorteado é: {colors['yellow']}{min(lista)}{Style.RESET_ALL}.')
