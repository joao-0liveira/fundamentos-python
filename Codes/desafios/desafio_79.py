from time import sleep
from operator import itemgetter
import random
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

dict = {
    'Jogador 1': random.randint(1,6),
    'Jogador 2': random.randint(1,6),
    'Jogador 3': random.randint(1,6),
    'Jogador 4': random.randint(1,6)
}    

print()
print('VALORES SORTEADOS:')
print('-'*20)
for k, v in dict.items():
    print(f'O {k} tirou {colors['yellow']}{v}{Style.RESET_ALL}.')
    sleep(1)

ranking = []
ranking = sorted(dict.items(), key=itemgetter(1), reverse=True)

print()
print('POSIÇÕES')
print('-'*30)
for i, v in enumerate(ranking):
    print(f'{colors['blue']}{i+1}o Lugar{Style.RESET_ALL}: {v[0]} com {v[1]} pontos.')
    sleep(1)
