from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 55')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, seja bem-vindo ao nosso programa!')
print(f'''Aqui você terá a oportunidade de digitar quantos números quiser, e no final lhe mostraremos: 
\n1- {colors['yellow']}QUANTOS NÚMEROS{Style.RESET_ALL} foram digitados,
2- Qual foi a {colors['yellow']}SOMA{Style.RESET_ALL} entre todos eles.''')

contador = soma = numero = 0

while True:
    numero = int(input(f'\nDigite umm número de sua escolha a seguir [{colors['red']}999{Style.RESET_ALL} para {colors['red']}PARAR{Style.RESET_ALL}]: '))
    if numero == 999:
        break
    soma = soma + numero
    contador = contador + 1

print(f'''\nDe acordo com os dados analisados:
1- Você digitou um total de: {colors['blue']}{Style.BRIGHT}{contador}{Style.RESET_ALL} números,
2- A {colors['yellow']}SOMA{Style.RESET_ALL} dos números digitados é igual a: {colors['blue']}{Style.BRIGHT}{soma}{Style.RESET_ALL}.
Programa encerrado!''')
