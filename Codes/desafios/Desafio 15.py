print('='*5, 'DESAFIO 15', '='*5)
print("""Olá, seja muito bem-vindo ao nosso programa!
Aqui você poderá ver o seu nome completo em letras maiúsculas e minúsculas,
Quantas letras tem o seu nome completo,
E quantas letras tem o seu primeiro nome!""")
nome = str(input('Para começarmos, basta digitar o seu nome completo a seguir: '))
#lista = [nome.split()]
print(f'Ótimo! Seu nome é: {nome}.')
print(f"""A seguir, {nome}, estão os dados acerca do seu nome:
Nome completo em letras maiúsculas: {nome.upper()}.
Nome completo em letras minúsculas: {nome.lower()}.
Quantas letras há no seu nome completo: {len(nome.replace(' ',''))} letras.
Quantas letras há no seu primeiro nome: {len(nome.split()[0])} letras.""")
