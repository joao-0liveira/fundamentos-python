#frase = str(input('Digite uma frase: ')).strip().lower()
#inverso = frase[:: -1]
#print(f'{frase.replace(' ', '')}')
#print(f'{inverso.replace(' ', '')}')
from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'white': Fore.WHITE
}

print(f'{Style.BRIGHT}{colors['white']}-=-'*6)
print(' '*2, 'DESAFIO 43')
print('-=-'*6)
print(f'''{Style.RESET_ALL}\nSeja bem vindo ao nosso programa!
Aqui você poderá  poderá digitar uma frase qualquer e no nosso programa irá analisar se ela é um {colors['blue']}PALÍNDROMO{Style.RESET_ALL}.''')
frase = str(input('Para continuarmos, digite a frase de seu interesse a seguir: ')).strip().lower()
inverso = frase[::-1]
if frase.replace(' ', '') == inverso.replace(' ', ''):
    print(f'''A frase digitada: "{Style.BRIGHT}{colors['white']}{frase}{Style.RESET_ALL}", {colors['blue']}É UM PALÍNDROMO{Style.RESET_ALL}!''')
else:
    print(f'''A frase digitada: "{Style.BRIGHT}{colors['white']}{frase}{Style.RESET_ALL}", {colors['red']}NÃO É UM PALÍNDROMO!{Style.RESET_ALL}''')

