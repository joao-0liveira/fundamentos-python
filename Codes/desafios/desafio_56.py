from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'yellow': Fore.YELLOW
}

print(f'{Style.BRIGHT}-=-'*6)
print(' '*2, 'DESAFIO 56')
print('-=-'*6)

print(f'''{Style.RESET_ALL}\nOlá! Seja bem-vindo ao nosso programa de matématica!
Aqui você terá a oportunidade de pesquisar a tabela de tabuada de qualque número que você desejar!''')

numero = 1

while True:
        
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        print('\nPrograma encerrado!')
        break
    
    print(f'{Style.BRIGHT}{colors['yellow']}-{Style.RESET_ALL}'*30)
    print(f'''{Style.BRIGHT}{numero} X 1 = {numero*1}
{numero} X 2 = {numero*2}
{numero} X 3 = {numero*3}
{numero} X 4 = {numero*4}
{numero} X 5 = {numero*5}
{numero} X 6 = {numero*6}
{numero} X 7 = {numero*7}
{numero} X 8 = {numero*8}
{numero} X 9 = {numero*9}
{numero} X 10 = {numero*10}{Style.RESET_ALL}''')
    print(f'{Style.BRIGHT}{colors['yellow']}-{Style.RESET_ALL}'*30)
