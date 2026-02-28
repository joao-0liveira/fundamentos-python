import random
print('='*5, 'DESAFIO 20', '='*5)
print("""Olá! Seja muito bem-vindo ao nosso programa!
Aqui, você e o computador jogarão um jogo de adivinhação!
Em que o computador pensará entre um número de 1 até 5 e você precisará acertar! Vamos lá?""")
número = int(input('Para começar, digite um número de sua escolha a seguir, de 1 até o 5: '))
print(f'Ótimo! O número escolhido foi: {número}!')
escolha = random.randint(1, 5)
print(f'O computador escolheu o número: {escolha}')
if número == escolha:
    print('Parabéns! Você adivinhou o número que o computador escolheu!')
else:
    print('Você perdeu, tente novamente...')
print('Jogo finalizado!')
