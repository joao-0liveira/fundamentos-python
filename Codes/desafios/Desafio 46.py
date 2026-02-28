from colorama import Fore, Style, init

init(autoreset=False)

color = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA,
    'green': Fore.GREEN
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 46')
print('-=-'*6)

print(f'\n{Style.RESET_ALL}Olá! Seja muito bem-vindo ao nosso programa!')
print(f'''Aqui, você poderá inserir o {Style.BRIGHT}NOME, IDADE e SEXO{Style.RESET_ALL} de quatro pessoas, e lhe mostraremos:
A {color['green']}MÉDIA{Style.RESET_ALL} das idades.
O {color['green']}NOME{Style.RESET_ALL} do homem {color['green']}MAIS VELHO{Style.RESET_ALL}.
E quantas {color['green']}MULHERES{Style.RESET_ALL} têm mais de {color['green']}20 ANOS{Style.RESET_ALL}.
Para isso, basta responder a caixa de perguntas abaixo.''')

contador = 0
names = []
years = []
sex = []

for c in range(1, 5):
    list = (input(f'\nDigite, {Style.BRIGHT}RESPECTIVAMENTE{Style.RESET_ALL}, o {Style.BRIGHT}NOME, IDADE e SEXO{Style.RESET_ALL} da {c}ª pessoa a seguir, separados por vírgula: ')).split(', ')
    
    names.append(list[0])
    years.append(list[1])
    sex.append(list[2])

    years_int = [int(i) for i in years]

print('\n', '-'*60)

print(f'\nA {color['blue']}MÉDIA DAS IDADES{Style.RESET_ALL} inseridas na lista é igual a: {Style.BRIGHT}{(years_int[0]+years_int[1]+years_int[2]+years_int[3])/4} anos{Style.RESET_ALL}!')

if max(years_int) == years_int[0] and sex[0] == 'masculino':
    print(f'\nO {Style.BRIGHT}{names[0]}{Style.RESET_ALL} é o {color['blue']}HOMEM MAIS VELHO{Style.RESET_ALL} da lista, com {Style.BRIGHT}{years_int[0]}{Style.RESET_ALL} anos de idade.')
elif max(years_int) == years_int[1] and sex[1] == 'masculino':
    print(f'\nO {Style.BRIGHT}{names[1]}{Style.RESET_ALL} é o {color['blue']}HOMEM MAIS VELHO{Style.RESET_ALL} da lista, com {Style.BRIGHT}{years_int[1]}{Style.RESET_ALL} anos de idade.')
elif max(years_int) == years_int[2] and sex [2] == 'masculino':
    print(f'\nO {Style.BRIGHT}{names[2]}{Style.RESET_ALL} é o {color['blue']}HOMEM MAIS VELHO{Style.RESET_ALL} da lista, com {Style.BRIGHT}{years_int[2]}{Style.RESET_ALL} anos de idade.')
elif max(years_int) == years_int[3] and sex[3] == 'masculino':
    print(f'\nO {Style.BRIGHT}{names[3]}{Style.RESET_ALL} é o {color['blue']}HOMEM MAIS VELHO{Style.RESET_ALL} da lista, com {Style.BRIGHT}{years_int[3]}{Style.RESET_ALL} anos de idade.')
else:
    print('Na lista não foi informado nenhum dado de um homem. Ou há dois homens com idades iguais')

if years_int[0] > 20 and sex[0] == 'feminino':
    contador += 1
if years_int[1] > 20 and sex [1] == 'feminino':
    contador += 1
if years_int[2] > 20 and sex[2] == 'feminino':
    contador += 1
if years_int[3] > 20 and sex[3] == 'feminino':
    contador += 1

print(f'\nE na lista há: {Style.BRIGHT}{contador}{Style.RESET_ALL} mulher(es) com {color['blue']}MAIS DE 20 ANOS{Style.RESET_ALL} de idade')
print('\n', '-'*60)
