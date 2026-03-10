from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'red': Fore.RED
}


while True:
    expressao = input('\nDigite a sua expressão a seguir: ')

    pts = expressao.count('(')
    ptss = expressao.count(')')
    if (pts + ptss) % 2 == 0:
        print('-'*40)
        print(f'A sua esxpressão digitada "{colors['yellow']}{expressao}{Style.RESET_ALL}" está {colors['blue']}CORRETA{Style.RESET_ALL}!')
    else:
        print('-'*40)
        print(f'A sua expressão digitada: "{colors['yellow']}{expressao}{Style.RESET_ALL}" está {colors['red']}INCORRETA{Style.RESET_ALL}!')
