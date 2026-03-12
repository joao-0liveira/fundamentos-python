from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

aluno = {}

aluno['nome'] = str(input('Digite o nome do aluno(a): '))
aluno['média'] = float(input('Digite a média do aluno(a): '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 7 > aluno['média'] >=6:
    aluno['situação'] = 'EM RECUPERAÇÂO'
else:
    aluno['situação'] = 'REPROVADO'

print(f'\nO nome do(a) aluno(a) é: {colors['yellow']}{aluno['nome']}{Style.RESET_ALL}.')
print(f'A média obtida foi de: {colors['yellow']}{aluno['média']}{Style.RESET_ALL}.')
print(f'A situação é de: {aluno['situação']}')
