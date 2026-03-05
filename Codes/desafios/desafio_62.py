from colorama import Fore, Style, init

init(autoreset=False)

colors = {
    'blue': Fore.BLUE,
    'red': Fore.RED,
    'yellow': Fore.YELLOW
}

print(f'''\nOlá, seja bem vindo ao nosso programa de futebol brasileiro!
Aqui você poderá consultar as seguintes informações acerca do Campeonato Brasileiro:''')

print('-'*60)
print(f'''1- Os {colors['yellow']}5 PRIMEIROS{Style.RESET_ALL} colocados da tabela,
2- Os {colors['yellow']}ÚLTIMOS 4{Style.RESET_ALL} colocados da tabela,
3- Uma lista com os times organizados em {colors['yellow']}ORDEM ALFABÉTICA{Style.RESET_ALL},
4- Em que posição está o time {colors['yellow']}ATLÉTICO-MG{Style.RESET_ALL}.''')

brasileiro = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense', 'Athletico-PR', 
              'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol', 'Flamengo','Coritiba', 
              'Santos', 'Botafogo', 'EC Vitória', 'Remo', 'Atlético-MG', 'Internacional', 'Cruzeiro', 'Vasgo da Gama')

print('\n')
print(f'Os 4 primeiros colocados do Campeonato Brasileiro 2026 são: {brasileiro[:5]}.')
print('-'*125)
print(f'Os últimos 4 colocados da tabela são: {brasileiro[16:21]}.')
print('-'*125)
print(f'Times em ordem alfabética: {sorted(brasileiro)}.')
print('-'*125)
print(f'O Atlético-MG está na {brasileiro.index('Atlético-MG')+1}ª posição.')
print('-'*125)

print('\nPrograma Finalizado!')