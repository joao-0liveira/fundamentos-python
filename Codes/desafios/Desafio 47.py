from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 47')
print('-=-'*6)

print(f'\n{Style.RESET_ALL}Bem vindo ao nosso programa!')
print(f'Aqui você poderá colocar qual é o seu {colors['blue']}SEXO{Style.RESET_ALL} na caixa de resposta que segue a seguir.')

sexo = str(input(f'Por favor, indique o seu sexo {colors['red']}[M/F]{Style.RESET_ALL}: ')).lower().strip()[0]

while sexo != 'f' and sexo != 'm':
    while sexo != 'f' and sexo != 'm':
        sexo = str(input('Dados inválidos. Por favor, informe seus dados novamente: ')).lower()

print('Dados recebidos com sucesso! Programa encerrado.')
