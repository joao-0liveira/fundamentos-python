from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'yellow': Fore.YELLOW
}

lista = []

numero = int(input('Digite um valor a seguir: '))
lista.append(numero)
print('Número adicinado ao final da lista.')

for contador in range(1, 5):
    numeros = int(input('\nDigite um valor a seguir: '))

    if lista[0] < numeros and numeros < lista[1]:
        lista.insert(1, numeros)
        print('Número adicionado na posição 1 da lista.')
    
    elif numeros > lista[0]:
        lista.append(numeros)
        print('Número adicionado no meio da lista.')
    
    elif numeros < lista[0]:
        lista.insert(0, numeros)
        print('Número adicionado no começo da lista.')
    
print(f'\nDe acordo com os dados fornecidos, a lista, em ordem, ficou da seguinte forma: {colors['yellow']}{lista}{Style.RESET_ALL}.')
