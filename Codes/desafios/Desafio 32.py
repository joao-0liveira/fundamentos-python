print('-=-'*6)
print(' '*2, 'DESAFIO 32')
print('-=-'*6)
print('''Olá! Seja bem vindo ao nosso programa de geometria!
Aqui você poderá atribuir valores para as arestas de um triângulo, e nosso programa dirá se ele poderá existir, além de dizer de qual tipo será.''')
a1 = int(input('Para começarmos, atribua o valor da primeira aresta a seguir: '))
a2 = int(input('Ótimo! Agora, um valor para a segunda aresta: '))
a3 = int(input('E por fim, um valor para a terceira aresta: '))
print(f'O nosso sistema já captou os valores atribuídos, que são: {a1}, {a2} e {a3}.')
if a1 < a2+a3 and a2 <a1+a3 and a3 < a1+a2 and a1 == a2 == a3:
    print('''De acordo com nossas análises, os valores que você atribuiu podem formar um triângulo!
E ele será EQUILÁTERO!''')
elif a1 < a2+a3 and a2 < a1+a3 and a3 < a1+a2 and a1 == a2 or a1 == a3 or a2 == a3:
    print('''De acordo com nossas análises, os valores que você atribuiu podem formar um triângulo!
E ele será ISÓSCELES!''')
elif a1 < a2+a3 and a2 < a1+a3 and a3 <a1+a2 and a1 != a2 != a3 != a1:
    print('''De acordo com nossas análises, os valores que você atribuiu podem formar um triângulo!
E ele será ESCALENO!''')
else:
    print('Com os valores que você nos informou, não será possível formar um triângulo, por favor, tente novamente atibuindo outros valores.')
