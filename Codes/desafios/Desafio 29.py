from datetime import date
print('-=-'*6)
print(' '*2, 'DESAFIO 29')
print('-=-'*6)
print('''Olá! Seja muito bem-vindo ao aplicativo do Exército Brasileiro!
Nessa sessão você poderá consultar a situação do seu alistamento militar obrigatório.''')
ano = int(input('Para iniciarmos a consulta de sua situação militar, informe, a seguir, o ano de seu nascimento: '))
print(f'De acordo com o analisado, seu ano de nascimento é: {ano}.')
alistar = date.today().year
if alistar - ano == 18:
    print(f'''Logo, no ano atual de {alistar}, você completa 18 anos, portanto, é necessário realizar o alistamento!
Procure a junta militar mais próxima e regularize a sua situação militar!''')
elif alistar - ano < 18:
    print(f'''Logo, no ano atual de {alistar}, você completa {alistar-ano} anos.
Portanto, aguarde {18-(alistar-ano)} ano(s) até completar a idade miníma necessária para o alistamento militar obrigatório.''')
elif alistar - ano > 18:
    print(f'''Ótimo, você já tem a idade necessária para realizar o alitamento militar!
De acordo com o ano atual, passaram {(alistar-ano)-18} ano(s) do seu perído de alistamento militar.
Esperamos que a sua situação esteja regularizada!''')
