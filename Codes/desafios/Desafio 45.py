from colorama import Fore, Style, init

init(autoreset=False)

color = {
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'white': Fore.WHITE,
    'cyan': Fore.CYAN
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 45')
print('-=-'*6)

print(f'''\n{Style.RESET_ALL}Bem vindo ao nosso programa!
Aqui você poderá ver, entre o peso de cinco pessoas, qual é o menor e o maior!
Na caixa de respostas a seguir, insira os dados requisitados.''')
peso = []
for c in range(1, 6):
    pesos = float(input(f'\nInsira a massa da {c}ª pessoa: '))
    peso.append(pesos)
print(f'\nO menor peso inserido é igual a: {Style.BRIGHT}{color['blue']}{min(peso)}Kg{Style.RESET_ALL}.')
print(f'E o maior peso inserido é igual a: {Style.BRIGHT}{color['red']}{max(peso)}Kg{Style.RESET_ALL}.')
