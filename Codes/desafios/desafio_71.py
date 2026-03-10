from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

lista = []
par = []
impar = []

while True:
    print('-'*35)
    numeros = int(input('Digitre um número a seguir: '))
    lista.append(numeros)

    if numeros % 2 == 0:
        par.append(numeros)
    else:
        impar.append(numeros)

    resposta = ''
    resposta = str(input(f'Você deseja continuar digitando valores? [{colors['blue']}S{Style.RESET_ALL}/{colors['red']}N{Style.RESET_ALL}]: '))
    if resposta in 'Nn':
        break

print(f'''\n1- A lista formada com {colors['blue']}todos os valores{Style.RESET_ALL} digitados é: {colors['yellow']}{lista}{Style.RESET_ALL},
2- A lista formada com {colors['blue']}valores pares{Style.RESET_ALL} digitados é: {colors['yellow']}{par}{Style.RESET_ALL},
3- A lista formada com {colors['blue']}valores ímpares{Style.RESET_ALL} digitados é: {colors['yellow']}{impar}{Style.RESET_ALL}.''')
