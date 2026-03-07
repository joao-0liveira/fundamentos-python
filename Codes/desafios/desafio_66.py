from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nTemos as seguintes vogais na palavra "{colors['blue']}{p.upper()}{Style.RESET_ALL}": ', end= '')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
