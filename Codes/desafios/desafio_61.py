from colorama import Fore, Style, init

init(autoreset=False)

color = {
    'yellow': Fore.YELLOW
}

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('\nDigite um número a seguir: '))
    if 0 <= numero <= 20:
        break

print(f'Você digitou o número {color['yellow']}{numeros[numero]}{Style.RESET_ALL}.')
