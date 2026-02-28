import random
print('-=-'*6)
print(' '*2, 'DESAFIO 35')
print('-=-'*6)
print('''Olá! Seja bem vindo ao nosso programa!
Aqui, você disputará uma partida de pedra, papel e tesoura contra o computador.
Será que você consegue ganhar?''')
escolha = str(input('Digite, a seguir, a sua escolha entre pedra, papel e tesoura: ')).lower()
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print(f'O computador escolheu: {computador}.')
if escolha == 'pedra' and computador == 'tesoura' or escolha == 'tesoura' and computador == 'papel' or escolha == 'papel' and computador == 'pedra':
    print('PARABÉNS! Você ganhou o jogo!')
elif escolha == 'tesoura' and computador == 'pedra' or escolha == 'papel' and computador == 'tesoura' or escolha == 'pedra' and computador == 'papel':
    print('Infelizmente você perdeu... Tente novamente.')
else:
    print('O jogo foi um EMPATE! Tente novamente.')
