from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 54')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, seja bem vindo ao nosso programa!')
print(f'''Aqui, você terá a oportunidade de digitar quantos números quiser, e o nosso programa:
      
1- Calculará a {colors['yellow']}MÈDIA ENTRE TODOS{Style.RESET_ALL} os valores,
2- Qual foi o {colors['yellow']}MAIOR{Style.RESET_ALL} e o {colors['yellow']}MENOR{Style.RESET_ALL} valor lido pelo programa.''')

resposta = 'Sim'
numero = soma = 0
contador = 0
maior = menor = None

while resposta == 'Sim':
    numero = int(input('\nDigite um valor a seguir: '))
    soma = soma + numero
    
    if maior is None:
        maior = numero
    elif numero > maior:
        maior = numero
    
    if menor is None:
        menor = numero
    elif numero < menor:
        menor = numero

    contador = contador + 1

    resposta = str(input(f'Você deseja continuar? [{colors['blue']}Sim{Style.RESET_ALL}/{colors['red']}Não{Style.RESET_ALL}]: ')).title()

print(f'''\nDe acordo com os dados analisados pelo nosso programa:
1- A média entre os {colors['yellow']}{contador}{Style.RESET_ALL} números digitados é igual a: {colors['blue']}{soma/contador}{Style.RESET_ALL}.
2- O {Style.BRIGHT}MAIOR{Style.RESET_ALL} valor digitado foi o número: {colors['yellow']}{maior}{Style.RESET_ALL}, e o {Style.RESET_ALL}MENOR{Style.RESET_ALL} digitado foi o número: {colors['yellow']}{menor}{Style.RESET_ALL}.''')
