from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW,
    'magenta': Fore.MAGENTA,
    'red': Fore.RED
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 51')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, bem vindo ao nosso programa de matemática!')
print('''Aqui, você poderá ver os dez primeiros termos de uma progrssão aritmética que quiser!
Para isso, basta apenas nos informar o primeiro termo da progressão e a sua razão.''')

primeiro = int(input('\nDigite, a seguir, o primeiro termo da progressão: '))
razao = int(input('Agora, digite a razão desejada para a progressão: '))

contador = 1
termo = primeiro
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} → ', end='')
        termo = termo + razao
        contador = contador + 1
    print('Pausa')
    mais = int(input('\nQuantos termos a mais você deseja nessa PA? '))

print('\nPrograma encerrado!')
