from colorama import Fore, Style, init

init(autoreset=False)

colors = { 
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 60')
print(f'-=-{Style.RESET_ALL}'*6)

print('''\nOlá, seja bem vindo à seção de Caixa Eletrônico do Banco União!
Informe na caixa de texto a seguir o valor desejado a ser sacado.''')
print(f'{colors['yellow']}-{Style.RESET_ALL}'*70)

saque = int(input('Qual valor você deseja sacar: R$'))

total = saque
cedula = 50
totalced = 0

while True:
    if total >= cedula:
        total = total - cedula
        totalced = totalced + 1

    else:
        if totalced > 0: 
            print(f'O total de cédulas de R${cedula} foi de {totalced}')
        if cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1
        totalced = 0
        
        if total == 0:
            break

print('\nPrograma encerrado!')
