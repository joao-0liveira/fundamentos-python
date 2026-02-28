from colorama import Fore, Style, init

init(autoreset=False)

color = {
    'preto': Fore.BLACK,
    'verde': Fore.GREEN,
    'amarelo': Fore.YELLOW,
    'ciano': Fore.CYAN,
    'vermelho': Fore.RED,
    'azul': Fore.BLUE,
    'roxo': Fore.MAGENTA,
    'branco': Fore.WHITE,
    'reset': Fore.RESET
}

style = {
    'intenso': Style.BRIGHT,
    'apagado': Style.DIM
}


print(f'{Style.BRIGHT}{color['branco']}Olá! Estamos fazendo um teste com algumas cores!{Style.RESET_ALL}')
print(f'\n{Style.BRIGHT}Estamos testando utilizar cores:{Style.RESET_ALL} {color['vermelho']}VERMELHO{color['reset']}, {color['azul']}AZUL{color['reset']} e {color['roxo']}ROXO{color['reset']}!')
print(f'\n{Style.BRIGHT}{color['branco']}Você gostou do resultado?')
