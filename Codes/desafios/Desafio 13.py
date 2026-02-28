import random
print('='*5, 'DESAFIO 13', '='*5)
print('Olá! Seja bem vindo ao nosso programa de sorteios!')
print('Aqui você poderá sortear o nome de quatro alunos para decidir quem irá executar uma tarefa importante: \nApagar o quadro!')
aluno1 = str(input('Para começarmos, digite o nome do primeiro aluno a seguir: '))
aluno2 = str(input('Agora, o nome do segundo aluno a seguir: '))
aluno3 = str(input('O nome do terceiro aluno: '))
aluno4 = str(input('E por fim, Digite o nome do quarto aluno a seguir: '))
lista = [aluno1, aluno2, aluno3, aluno4]
print('Ótimo! nosso computador já iniciou o sorteio para descobrir quem será sorteado!')
print(f'E o aluno(a) sorteado, que apagará o quadro, é: {random.choice(lista)}!')
print('Obrigado por usar o nosso programa!')
