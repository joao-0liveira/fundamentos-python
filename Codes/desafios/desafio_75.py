from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

coluna0 = []
coluna1 = []
coluna2 = []
lista = []
s = 0

print()
for c in range(0, 3):
    numeros = (int(input(f'Digite um valor para {colors['yellow']}[0, {c}]{Style.RESET_ALL}: ')))
    if numeros % 2 == 0:
        s = s + numeros
    coluna0.append(numeros)
lista.append(coluna0[:])
coluna0.clear()

for c in range(0, 3):
    numeros1 = (int(input(f'Digite um valor para {colors['yellow']}[1, {c}]{Style.RESET_ALL}: ')))
    if numeros1 % 2 == 0:
        s = s + numeros1
    coluna1.append(numeros1)
lista.append(coluna1[:])
coluna1.clear()

for c in range (0, 3):
    numeros2 = (int(input(f'Digite um valor para {colors['yellow']}[2, {c}]{Style.RESET_ALL}: ')))
    if numeros2 % 2 == 0:
        s = s + numeros2
    coluna2.append(numeros2)
lista.append(coluna2[:])
coluna2.clear()

print()
print(f'{Style.BRIGHT}-='*12)
print(f'''[  {lista[0][0]}  ] [  {lista[0][1]}  ] [  {lista[0][2]}  ]
[  {lista[1][0]}  ] [  {lista[1][1]}  ] [  {lista[1][2]}  ]
[  {lista[2][0]}  ] [  {lista[2][1]}  ] [  {lista[2][2]}  ]''')
print('-='*12)
print()

print(f'\n{Style.RESET_ALL}1- A {colors['blue']}SOMA{Style.RESET_ALL} de todos {colors['yellow']}valores pares{Style.RESET_ALL} digitados é: {s},')
print(f'2- A {colors['blue']}SOMA{Style.RESET_ALL} de todos os valores da {colors['yellow']}terceira coluna{Style.RESET_ALL} é: {lista[0][2] + lista[1][2] + lista[2][2]},')
print(f'3- O {colors['blue']}MAIOR{Style.RESET_ALL} valor da {colors['yellow']}terceira linha{Style.RESET_ALL} é: {max(lista[2][0], lista[2][1], lista[2][2])}.')
