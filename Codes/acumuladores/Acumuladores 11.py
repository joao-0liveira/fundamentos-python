from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'red': Fore.RED,
    'blue': Fore.BLUE
}

print('\npeça um número e diga se ele é PRIMO.')

primo = int(input('Digite um número a seguir e diremos se ele é primo: '))
contador = 0

for c in range (1, primo+1):
    if primo % c == 0:
        print(f'{colors['blue']}', c, end=' ')
        contador = contador + 1
    else:
        print(f'{colors['red']}', c, end=' ')

if contador < 2:
    print(f'\n{Style.RESET_ALL}O número digitado "{primo}" não é um número primo!')
elif contador == 2:
    print(f'\n{Style.RESET_ALL}O número digitado "{primo}" é um número primo!')
else:
    print(f'\n{Style.RESET_ALL}O número digitado "{primo}" não é um número primo!')
