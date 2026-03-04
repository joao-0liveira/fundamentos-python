from colorama import Fore, Style, init

init(autoreset=False)

colors = { 
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 58')
print(f'-=-{Style.RESET_ALL}'*6)

print('\nOlá, seja bem-vindo ao nosso programa de validação de dados!')
print(f'''Após preencher os dados que o nosso programa requisitará, você poderá ver:
1- Quantas pessoas tem mais de {colors['blue']}18 ANOS{Style.RESET_ALL},
2- Quantos {colors['yellow']}HOMENS{Style.RESET_ALL} foram cadastrados,
3- Quantas mulheres tem menos de {colors['blue']}20 ANOS{Style.RESET_ALL}.''')

contador = idade = 0 
homens = 0
mulheres = 0

while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo [M/F]: ')).strip()[0].lower()

        if idade > 18:
            contador = contador + 1

        if sexo == 'm':
            homens = homens + 1

        if idade < 20 and sexo == 'f':
            mulheres = mulheres + 1
    
    print('-'*25)
    
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip()[0].lower()
    
    if resposta == 'n':
        break

print(f'''\nO nosso programa já captou todos os dados inseridos:
1- Foram cadastradas {contador} pessoas com mais de 18 anos de idade,
2- Foram cadastrados {homens} homens no programa,
3- Foram cadastradas {mulheres} mulheres com menos de 20 anos no sistema.''')

print('\nPrograma encerrado!')
