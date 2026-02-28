print('='*5, 'DESAFIO 22', '='*5)
print("""Olá, seja muito bem vindo ao nosso programa!
Aqui você poderá escrever qualquer número e o nosso sistema identificará se ele é PAR ou ÍMPAR.""")
número = int(input('Para começarmos, por favor, digite o número de sua escolha a seguir: '))
if número % 2 == 0:
    print(f"""O número: {número}, que você escolheu, é um número PAR!""")
else:
    print(f"""O número: {número}, que você escolheu, é um número ÍMPAR!""")
print('Sessão finalizada!')
