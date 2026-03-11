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

print()
for c in range(0, 3):
    coluna0.append(int(input(f'Digite um valor para {colors['yellow']}[0, {c}]{Style.RESET_ALL}: ')))
lista.append(coluna0[:])
coluna0.clear()

for c in range(0, 3):
    coluna1.append(int(input(f'Digite um valor para {colors['yellow']}[1, {c}]{Style.RESET_ALL}: ')))
lista.append(coluna1[:])
coluna1.clear()

for c in range (0, 3):
    coluna2.append(int(input(f'Digite um valor para {colors['yellow']}[2, {c}]{Style.RESET_ALL}: ')))
lista.append(coluna2[:])
coluna2.clear()

print()
print('-='*20)
print(f'''[  {lista[0][0]}  ] [  {lista[0][1]}  ] [  {lista[0][2]}  ]
[  {lista[1][0]}  ] [  {lista[1][1]}  ] [  {lista[1][2]}  ]
[  {lista[2][0]}  ] [  {lista[2][1]}  ] [  {lista[2][2]}  ]''')
print('-='*20)
print()
