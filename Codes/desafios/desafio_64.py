from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

lista = ()

numero1 = int(input('\nDigite um valor a seguir: '))
numero2 = int(input('Digite o segundo valor a seguir: '))
numero3 = int(input('Digite o terceiro valor a seguir: '))
numero4 = int(input('Digite o quarto valor a seguir: '))

lista = (numero1, numero2, numero3, numero4)

print(f'\nNos números digitados, o {colors['blue']}número 9{Style.RESET_ALL} apareceu : {colors['yellow']}{lista.count(9)} vezes{Style.RESET_ALL}.')

procura = lista.count(3)
if procura == 0:
    print(f'O {colors['blue']}número 3{Style.RESET_ALL} foi digitado {colors['red']}nenhuma vez{Style.RESET_ALL}.')
else:
    print(f'O {colors['blue']}número 3{Style.RESET_ALL} apareceu na posição {colors['yellow']}{lista.index(3)+1}ª{Style.RESET_ALL}.')

print(f'Os {colors['blue']}números pares{Style.RESET_ALL} digitados foram: ', end='')
if lista[0] % 2 == 0:
    print(lista[0], end=', ')
if lista[1] % 2 == 0:
    print(lista[1], end=', ')
if lista[2] % 2 == 0:
    print(lista[2], end=', ')
if lista[3] % 2 == 0:
    print(lista[3], end='')
