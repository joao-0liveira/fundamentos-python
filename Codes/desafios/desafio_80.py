from datetime import date
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow':  Fore.YELLOW
}

dict = {}
ano = date.today().year

while True:
    dict['nome'] = str(input('Digite o seu nome: '))
    dict['nascimento'] = int(input('Digite o ano de seu nascimento: '))
    dict['idade']= ano - dict['nascimento']
    dict['ctps'] = int(input(f'Informe a sua Carteira de Trabalho {Style.BRIGHT}[0 se não possui]{Style.RESET_ALL}: '))
    if dict['ctps'] == 0:
        break
    
    dict['contratação'] = int(input('Qual o ano da sua contratação: '))
    dict['aposentadoria'] = (dict['contratação']+35) - dict['nascimento']
    dict['salário'] = float(input('Informe o seu salário: R$'))
    break

print('-='*35)
for k, v in dict.items():
    print(f'O campo {colors['blue']}{k}{Style.RESET_ALL} tem o valor: {colors['yellow']}{v}{Style.RESET_ALL}.')
