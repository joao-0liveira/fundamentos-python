from colorama import Fore, Style, init
from datetime import date

init(autoreset=False)

color = {
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'white': Fore.WHITE
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 44')
print('-=-'*6)
print(f'\n{Style.RESET_ALL}Bem vindo ao nosso programa!')
print('Aqui você poderá ver, entre o ano de nascimento de sete pessoas, quais já antingiram a maioridade!')
print('Para começarmos, digite o ano de nascimento das sete pessoas no espaço que segue adiante:')
qtde = 0
qtd =0
ano = date.today().year
for c in range (1, 8):
    num = int(input(f'\nDigite o ano de nascimento da {c}ª pessoa: '))
    if ano - num >= 18:
        qtde += 1
    else:
        qtd += 1
print(f'\nA quantidade de pessoas que {color['blue']}atingiram a maioridade são{Style.RESET_ALL}: {Style.BRIGHT}{color['white']}{qtde}{Style.RESET_ALL}.')
print(f'De forma igual, {Style.BRIGHT}{color['white']}{qtd}{Style.RESET_ALL} pessoa(s) é/são {Style.BRIGHT}{color['red']}menores de idade!{Style.RESET_ALL}')
