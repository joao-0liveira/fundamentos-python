from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

lista = []

for c in range(1,6):
    lista.append(int(input(f'Digite o {colors['blue']}{c}º{Style.RESET_ALL} valor a seguir: ')))

print(f'\nFoi criada a seguinte lista com os valores fornecidos: {colors['yellow']}{lista}{Style.RESET_ALL}')
print(f'''1- O maior valor digitado na lista foi o valor: {colors['yellow']}{max(lista)}{Style.RESET_ALL}, na posição {colors['blue']}{lista.index(max(lista))+1}{Style.RESET_ALL},
2- O menor valor digitado na lista foi o valor: {colors['yellow']}{min(lista)}{Style.RESET_ALL}, na posição {colors['blue']}{lista.index(min(lista))+1}{Style.RESET_ALL}.''')
