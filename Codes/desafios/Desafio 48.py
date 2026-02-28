from colorama import Fore, Style, init
from random import randint
from time import sleep

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 48')
print('-=-'*6)

print(f'\n{Style.RESET_ALL}Bem vindo ao nosso programa de jogos online!')
print('Aqui você jogará um programa em que terá que adivinhar o mesmo número que o computador "pensar".')
print('Funcionará da seguinte maneira: O computador vai "pensar" em um número de 1 a 10. E você irá digitar o número que acha que ele "pensou" até acertar.')

print('\n')
print(f'{Style.BRIGHT}='*10)
print('PREPARADO?')
print('='*10)

print(f'\n{Style.RESET_ALL}O COMPUTADOR ESTÁ ESCOLHENDO UM NÚMERO...')
sleep(3)

tentativas = 1
computador = randint(1, 10)

escolha = int(input('\nO computador escolheu um número! Tente adivinha-lo a seguir: '))

while escolha != computador:
    if escolha > computador:
        tentativas += 1
        escolha = int(input('Menos, escolha outro número: '))
    elif escolha < computador:
        tentativas += 1
        escolha = int(input('Mais, escolha outro número: '))

print(f'\nVocê ganhou! {colors['blue']}PARABÉNS!{Style.RESET_ALL}')
print(f'Para você vencer, foram necessárias {Style.BRIGHT}{colors['magenta']}{tentativas}{Style.RESET_ALL} tentativas!')
print(f'\n{Style.BRIGHT}JOGO FINALIZADO!{Style.RESET_ALL}')
