print('='*5, 'DESAFIO 26', '='*5)
print("""Olá! Seja muito bem-vindo ao nosso programa!
Neste programa, você poderá atribuir três valores para as arestas de um triângulo.
E o nosso sistema verificará se esse triângulo poderá existir, de acordo com a condição de existência.""")
n1 = int(input('Para começarmos, atribua o valor da primeira aresta: '))
n2 = int(input('Agora, atribua o valor da segunda aresta: '))
n3 = int(input('Por fim, atribua o valor da terceira aresta: '))
print(f'''Ótimo! o nosso sistema já captou os valores atribuídos, são eles: {n1, n2, n3}.''')
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('De acordo com a análise dos valores solicitados, É POSSÍVEL formar um triângulo!')
else:
    print('''De acordo com a análise dos valores solicitados, NÃO SERÁ POSSÍVEL formar um triângulo
Atribua outros valores e tente novamente!''')
    