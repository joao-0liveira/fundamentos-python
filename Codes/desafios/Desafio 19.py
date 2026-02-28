print('='*5, 'DESAFIO 19', '='*5)
print("""Olá! Seja muito bem-vindo ao nosso programa!
Aqui, você poderá escrever o seu nome completo e o nosso sistema identificará qual é o seu primeiro nome e o seu último sobrenome,
Para isso, basta nos fornecer o seu nome""")
nome = str(input('Para prosseguirmos, digite-o a seguir: ')).title()
print(f"""Ótimo! O nosso sistema já captou o seu nome e fez a sua análise, segue, a seguir, os dados aferidos: 
Nome completo: {nome}.
Primeiro nome: {nome.split()[0]}.
Último sobrenome: {nome.split()[-1]}.""")
