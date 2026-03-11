from time import sleep
from random import sample
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

ms = sample(range(1, 60), k=6)
 
print(f'{Style.BRIGHT}-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)

jogos = int(input(f'{Style.RESET_ALL}Quantos jogos da Mega Sena você vai querer fazer? Digite a seguir: '))

print()
print('-='*3, f'SORTEANDO {jogos} JOGOS', '-='*3)
for c in range(1, jogos+1):
    print(f'Jogo {c}: {sample(range(1, 60), k=6)}')
    sleep(1)
print('-='*5, '< BOA SORTE >', '=-'*5)
print()