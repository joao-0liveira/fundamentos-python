print('='*5, 'DESAFIO 18', '='*5)
print("""Olá! Seja muito bem-vindo ao nosso programa!
Aqui você poderá escrever a frase que quiser e indentificar:
Quantas vezes a letra "A" aparece,
Em que posição ela aparece a primeira vez,
E em que posição ela aparece pela última vez!""")
frase = str(input('Para iniciarmos, preciso que digite a frase de sua preferência a seguir: ')).lower().strip()
print(f"""Ótimo! O nosso sistema já analisou a sua frase! A seguir seguem os dados requeridos:
A letra "A" aparece: {frase.count('a')} vezes.
A letra "A" aparece pela primeira vez na posição: {frase.find('a')+1}.
E por fim, a letra "A" aparece pela última vez na posição: {frase.rfind('a')+1}.""")
