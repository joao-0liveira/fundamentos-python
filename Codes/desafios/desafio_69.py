from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'yellow': Fore.YELLOW
}

lista = []

for c in range(0, 5):
    numeros = int(input('\nDigite um número a seguir: '))

    if c == 0 or numeros > lista[-1]:
        lista.append(numeros)
        print('Número adicionado ao final da lista')
    else:
        
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                print(f'Número adicionado na posição {pos+1}')
                break
            pos = pos + 1
            
print(f'\nDe acordo com os dados fornecidos, a lista, em ordem, ficou da seguinte forma: {colors['yellow']}{lista}{Style.RESET_ALL}.')
