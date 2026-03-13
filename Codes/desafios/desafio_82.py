from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

lista = []
dict = {}
s = media = 0

print()
while True:
    print('-'*25)
    dict.clear()
    dict['nome'] = str(input('Nome: '))
    
    while True:
        dict['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dict['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite apenas M ou F.')
    
    dict['idade'] = int(input('Idade: '))
    s = s + dict['idade']
    lista.append(dict.copy())

    while True:
        resposta = str(input('Deseja contunar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        else:
            print('Erro, digite apenas Sim ou Não.')



    if resposta in 'N':
        break

print('=-'*30)
print(f'1- Ao todo, foram cadastradas {colors['yellow']}{len(lista)} pesssoas{Style.RESET_ALL}.')
print(f'2- A {colors['blue']}média{Style.RESET_ALL} das idade é de: {colors['yellow']}{s/len(lista):.2f} anos{Style.RESET_ALL}.')
print(f'3- As {colors['blue']}mulheres{Style.RESET_ALL} cadastradas são: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
        print
print(f'4- Lista de pessoas que estão {colors['blue']}acima da idade média{Style.RESET_ALL}: ', end='')
for p in lista:
    if p['idade'] > (s/len(lista)):
        print(p['nome'], end=' ')
