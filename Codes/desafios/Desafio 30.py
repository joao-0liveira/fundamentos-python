print('-=-'*6)
print(' '*2, 'DESAFIO 30')
print('-=-'*6)
print('''Olá! Seja bem-vindo ao portal do aluno da Escola Fellas Cut.
Na sessão do aluno, você poderá consultar a sua a sua situação, se você foi APROVADO, está em RECUPERAÇÂO ou foi REPROVADO.''')
nota1 = float(input('Para continuarmos o processe de verificação, digite a seguir a primeira nota obtida na avaliação final: '))
nota2 = float(input('Ótimo! Agora, digite a segunda nota obtida na avaliação final: '))
print(f'De acordo com os dados obtidos, suas notas foram: {nota1} e {nota2}.')
if (nota1 + nota2) / 2 < 5:
    print(f'''Portanto, a média obtida foi de: {(nota1 + nota2) / 2:.2f} pontos.
Status: REPROVADO.''')
elif 5 < (nota1 + nota2) / 2 < 6.9:
    print(f'''Portanto, a média obtida foi de: {(nota1 + nota2) / 2:.2f} pontos.
Status: Em RECUPERAÇÂO.''')
else:
    print(f'''Portanto, a média obtida foi de: {(nota1 + nota2) / 2:.2f} pontos.
Status: APROVADO!''')