from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

dados = []
lista = []
maior = None
pmaior = ''
menor = None
pmenor = ''

while True:
    print('-'*35)
    dados.append(str(input(f'Digite o {colors['blue']}nome{Style.RESET_ALL} da pessoa a seguir: ')))
    dados.append(int(input(f'Digite o {colors['blue']}peso{Style.RESET_ALL} da pessoa a seguir: ')))
    if maior is None:
        maior = dados[1]
        pmaior = dados[0]
    elif dados[1] > maior:
        maior = dados[1]
    
    if menor is None:
        menor = dados[1]
        pmenor = dados[0]
    elif dados[1] < menor:
        menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    pergunta = ''
    pergunta = str(input(f'Você deseja continuar inserindo dados? [{colors['blue']}S{Style.RESET_ALL}/{colors['red']}N{Style.RESET_ALL}]: '))
    if pergunta in 'Nn':
        break

print(f'\n1- Você registrou um total de {colors['yellow']}{len(lista)} pessoas{Style.RESET_ALL},')
print(f'2- O maior peso foi de: {colors['yellow']}{maior}kg{Style.RESET_ALL}. Peso de: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{colors['yellow']}{[p[0]]}{Style.RESET_ALL} ', end= '')
print()
print(f'3- O menor peso de foi de: {colors['yellow']}{menor}kg{Style.RESET_ALL}. Peso de: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{colors['yellow']}{[p[0]]}{Style.RESET_ALL} ', end='')
print()