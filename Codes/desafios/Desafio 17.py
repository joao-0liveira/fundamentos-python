print('='*5, 'DESAFIO 17', '='*5)
print("""Olá, seja muito bem-vindo ao nosso programa!
Aqui você poderá identificar se no primeiro nome da sua cidade existe a palavra "SANTO".""")
nome = str(input('Para começarmos, por favor, digite o nome da sua cidade a seguir: '))
print(f"""Ótimo! O nosso sistema já captou o nome da sua cidade. que é: {nome}.
Agora, vamos para a dúvida, sua cidade começa com "SANTO": {'Santo' in nome.split()[0]}""")
