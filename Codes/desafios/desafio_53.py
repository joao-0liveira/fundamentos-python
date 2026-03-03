from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 53')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, seja bem vindo ao nosso programa!')
print('Aqui você poderá digitar qualquer número que seja difente de 999, e no final lhe mostraremos a soma de todos que você digitar!')

flag = contador = soma = 0

flag = int(input('\nDigite um número de sua escolha a seguir: '))

while flag != 999:
    contador = contador + 1
    soma = soma + flag
    flag = int(input('Digite o próximo número desejado: '))

print(f'\nDe acordo com nossas análises, foram digitados: {colors['blue']}{contador}{Style.RESET_ALL} números!')
print(f'A soma dos {colors['blue']}{contador}{Style.RESET_ALL} números digitados é igual a: {colors['red']}{soma}{Style.RESET_ALL}.')
