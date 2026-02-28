from colorama import Fore, Style, init

init(autoreset=False)

color = {
    'white': Fore.WHITE,
    'yellow': Fore.YELLOW,
    'red': Fore.RED,
    'blue': Fore.BLUE
}

print(f'{Style.BRIGHT}{color['white']}-=-'*6)
print(f' '*2, 'DESAFIO 42')
print(f'-=-'*6)
print(f'{Style.RESET_ALL}\nBem vindo ao nosso programa de matemática!')
print('aqui você poderá digitar qualquer número inteiro e te diremos se ele é um número primo ou não!')
primo = int(input('Para prosseguirmos, digite o número de sua escolha a seguir: '))
contador = 0
for c in range(1, primo+1):
    if primo % c == 0:    
        print(f'{color['blue']}', c, end=' ')
        contador += 1 
    else:
        print(f'{color['red']}', c, end=' ')
print(f'{Style.RESET_ALL}\nO número {primo} foi dividido {contador} vezes.')
if contador == 2:
    print(f'Logo, ele {Style.BRIGHT}{color['blue']}É PRIMO{Style.RESET_ALL}!')
else:
    print(f'Logo, ele {Style.BRIGHT}{color['red']}NÃO É PRIMO{Style.RESET_ALL}!')
