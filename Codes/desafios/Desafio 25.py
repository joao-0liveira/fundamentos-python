print('='*5, 'DESAFIO 25', '='*5)
print("""Olá! Seja bem-vindo ao nosso programa!
Aqui, você poderá digitar três números quaisquer e o nosso programa irá selecionar o maior e o menor!""")
n1 = int(input('Para começarmos, digite o primeiro número a seguir: '))
n2 = int(input('Agora, o segundo número: '))
n3 = int(input('Por fim, digite o terceiro número a seguir: '))
print(f"""Ótimo! nosso sistema já captou os números escolhidos por você!
Foram: {n1, n2, n3}
O maior deles é o número: {max(n1, n2, n3)}.
E o menor deles é o número: {min(n1, n2, n3)}.
Obrigado por usar o nosso programa!""")
