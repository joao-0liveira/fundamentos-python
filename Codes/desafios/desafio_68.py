from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'yellow': Fore.YELLOW,
    'green': Fore.GREEN,
    'red': Fore.RED
}

lista = []


while True:
    print('-'*30)
    numeros = (int(input('Digite um valor a seguir: ')))
    
    if numeros not in lista:
        lista.append(numeros)
        print('Valor adicionado com sucesso!')
    else:
        print('Esse valor já foi adicionado na lista!')
    
    resposta = str(input(f'Você deseja continuar adicionando números na lista? [{colors['green']}S{Style.RESET_ALL}/{colors['red']}N{Style.RESET_ALL}]: '))

    if resposta in 'Nn':
        print('\nTudo bem, lista finalizada!')
        break

print(f'Com os valores que você forneceu, criamos a lista: {colors['yellow']}{sorted(lista)}{Style.RESET_ALL}.')
