from datetime import date
print('-=-'*6)
print(' '*2, 'DESAFIO 31')
print('-=-'*6)
print('''Olá! Seja bem-vindo ao portal da Conferência Nacional de Natação!
Na pagina do participante, você poderá ver em qual categoria poderá participar o campeonato reginal de natação.''')
nascimento = int(input('Para prosseguirmos, por favor, digite o ano de seu nascimento a seguir: '))
ano = date.today().year
print(f'De acordo com nossas análises, você possui {ano-nascimento} anos.')
idade = ano-nascimento
if idade <= 9:
    print(f'Logo, você está apto para participar da categoria MIRIM do campeonato!')
elif 9 < idade <= 14:
    print('Logo, você está apto para participar da categoria INFANTIL do campeonato!')
elif 14 < idade <=19:
    print('Logo, você está apto para participar da categoria JUNIOR do campeonato!')
elif 19 < idade <=20:
    print('Logo, você está apto para participar da categoria SÊNIOR do campeonato!')
else:
    print('Logo, você está apto participar da categoria MASTER do campeonato!')
print('Desejamos boa sorte durante a competição!')
