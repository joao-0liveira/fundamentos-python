from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

dict = {}
gols = []

print()
dict['nome'] = str(input('Escreva o nome do jogador: '))
partidas = int(input(f'Quantas partidas {dict['nome']} jogou? '))

print('-'*25)
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))

dict['gols'] = gols
dict['total'] = sum(gols)

print('-'*25)
print(f'O jogador {colors['yellow']}{dict['nome']}{Style.RESET_ALL} jogou {partidas} partidas.')
for i, g in enumerate(gols):
    print(f'  → Na partida {colors['yellow']}{i+1}{Style.RESET_ALL} ele fez {colors['blue']}{g}{Style.RESET_ALL} gols')
print(f'Foi um total de {colors['blue']}{dict['total']}{Style.RESET_ALL} gols!')
