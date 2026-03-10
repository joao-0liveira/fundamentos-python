from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

lista = []
par = []
impar = []

print('-'*35)
for c in range(1, 8):
    numero = int(input(f'Digite o {colors['blue']}{c}º{Style.RESET_ALL} número a seguir: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

lista.append(par[:])
lista.append(impar[:])
par.clear()
impar.clear()

print()
print('-='*20)
print(f'1- Os {colors['blue']}valores pares{Style.RESET_ALL} digitados foram: {colors['yellow']}{lista[0]}{Style.RESET_ALL},')
print(f'2- Os {colors['blue']}valores ímpares{Style.RESET_ALL} digitadops foram: {colors['yellow']}{lista[1]}{Style.RESET_ALL}.')
