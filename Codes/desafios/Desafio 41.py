# AN = A1 +(N - 1)*R
print('-=-'*6)
print(' '*2, 'DESAFIO 41')
print('-=-'*6)
print('''Bem vindo ao nosso programa de matemática!
Aqui você poderá ver os dez primeiros termos de uma progressão aritmética que você escolher!''')
a1 = int(input('Para começarmos, digite o primeiro termo da sequência a seguir: '))
razão = int(input('Agora, digite a razão da sua progessão: '))
print(f'Ótimo! Os dez primeiros termos de uma progrssão de razão {razão} são:')
dez = 10*razão+1
for c in range(a1, dez, razão):
    print(c, end= ' → ')
print('PROGRAMA FINALIZADO!')