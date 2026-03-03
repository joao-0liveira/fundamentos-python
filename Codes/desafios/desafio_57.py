from random import randint
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 57')
print(f'-=-{Style.RESET_ALL}')

print(f'''\nOlá, seja muito bem-vindo ao nosso programa de jogos online!
Aqui você poderá jogar {Style.BRIGHT}{colors['yellow']}PAR OU ÍMPAR{Style.RESET_ALL} contra o computador!''')

escolha = contador = 0
pi = 'par'

while True:
    computador = randint(1, 10)

    escolha = int(input('\nDigite um valor a seguir: '))
    pi = str(input('PAR ou ÍMPAR? ')).lower()

    if (escolha + computador) % 2 == 0 and pi == 'par':
        contador = contador + 1
        print('-'*25)
        print(f'PARABÉNS! Você {colors['blue']}{Style.BRIGHT}VENCEU{Style.RESET_ALL}!')
        print('-'*25)
        print(f'Você jogou o número "{escolha}" e o computador "{computador}". Total de {escolha +computador} é {colors['yellow']}PAR{Style.RESET_ALL}.')
    
    if (escolha + computador) % 2 != 0 and pi == 'impar':
        contador = contador + 1
        print('-'*25)
        print(f'PARABÉNS! Você {colors['blue']}{Style.BRIGHT}VENCEU{Style.RESET_ALL}!')
        print('-'*25)
        print(f'Você jogou o número "{escolha}" e o computador "{computador}". Total de {escolha+computador} é {colors['yellow']}ÍMPAR{Style.RESET_ALL}.')
    
    if (escolha + computador) % 2 == 0 and pi == 'impar':
        print('-'*25)
        print(f'Que azar, você {colors['red']}PERDEU{Style.RESET_ALL}!')
        print('-'*25)
        print(f'Você jogou o número "{escolha}" e o computador "{computador}". Total de {escolha+computador} é {colors['yellow']}PAR{Style.RESET_ALL}.')
        break

    if (escolha + computador) % 2 != 0 and pi == 'par':
        print('-'*25)
        print(f'Que azar, você {colors['red']}PERDEU{Style.RESET_ALL}!')
        print('-'*25)
        print(f'Você jogou o número "{escolha}" e o computador "{computador}". Total de {escolha+computador} é {colors['yellow']}ÍMPAR{Style.RESET_ALL}.')
        break

print(f'\nVocê ganhou um total de: {contador} vezes.')
