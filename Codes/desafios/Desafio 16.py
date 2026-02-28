print('='*5, 'DESAFIO 16', '='*5)
print("""Olá, seja muito bem-vindo ao nosso programa!
Aqui você poderá ver qual é a UNIDADE, a DEZENA, a CENTENA, e a UNIDADE DE MILHAR de um número que escolher de 0 a 9999!""")
número = int(input('Para começarmos, é necessário que você digite um número de 0 a 9999 a seguir: '))
print(f"""Ótimo! O número escolhido foi: {número}. E a seguir estão as informações sore ele:
O valor da sua UNIDADE é: {número // 1 % 10}.
O valor da sua DEZENA é: {número // 10 % 10}.
O valor da sua CENTENA é: {número // 100 % 10}.
E por fim, o valor da sua UNIDADE DE MILHAR é: {número // 1000 % 10}.""")
