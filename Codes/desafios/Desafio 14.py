import random
print('='*5, 'DESAFIO ', '='*5)
print('Olá! Seja bem vindo ao nosso programa!')
print('Aqui, um professor precisará sortear a ordem da apresentação de cinco aluno, e você será responsável por nomeá-los.')
aluno1 = str(input('Para começarmos, digite o nome do primeiro aluno a seguir: '))
aluno2 = str(input('A seguir, o nome do segundo aluno: '))
aluno3 = str(input('O nome do terceiro aluno: '))
aluno4 = str(input('E por fim, digite o nome do quarto aluno a seguir: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'Ótimo! O nosso sistema já captou o nome dos alunos e já fez o sorteio! \nSegue, a seguir, a ordem de apresentação: {lista}.')
