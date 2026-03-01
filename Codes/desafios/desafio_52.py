from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'red': Fore.RED,
    'blue': Fore.BLUE
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 52')
print('-=-'*6)

print(f'{Style.RESET_ALL}\nOlá, bem vindo ao nosso programa!')
print('Aqui você poderá digitar um número inteiro x qualquer e lhe mostraremos os x primeiros termos de uma Sequência de Fibonacci.')

x = int(input('\nPara prosseguirmos, digite o número de sua escolha a seguir: '))

t1 = 0
t2 = 1

print(f'\n{t1} → {t2} ', end='')

contador = 3

while contador <= x:
    t3 = t1 + t2
    print(f'{Style.BRIGHT}→ {t3} {Style.RESET_ALL}', end='')
    t1 = t2
    t2 = t3
    contador = contador + 1
print('FIM')
