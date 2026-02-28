print('-=-'*6)
print(' '*2,  'DESAFIO 27')
print('-=-'*6)
print('''Olá! Seja bem-vindo ao portal do Banco Fellas Cuts.
Nessa sessão, você poderá consultar as condições de empréstimo bancário para compra de uma residência.''')
valor = float(input('Para iniciarmos o processo de verificação do empréstimo, digite, a seguir, o valor do imóvel: '))
salário = float(input(f'O valor do imóvel foi computado pelo sistema, digite a seguir, o valor do seu salário atual e atualizado: '))
anos = int(input('O valor do seu salário foi computado pelo nosso sistema, digite a seguir em quantos anos pretende fazer a quitação do empréstimo: '))
print(f'De acordo com dados fornecidos, o valor mensal das parcelas será de: R${valor/(anos*12):.2f}.')
prestação = valor/(anos*12)
if prestação > salário*0.3:
    print(f'''Porém, de acordo com os dados fornecidos, o valor da prestação mensal ultrapassa 30% do seu salário, que seria de: R${salário*0.3:.2f}.
Configurando, portanto, na negação do pedido de empréstimo, deivdo às políticas internas da instituição bancária.''')
elif prestação == salário*0.3:
    print(f'''De acordo com as análises do nosso sistema, o valor da prestação mensal do seu empréstimo é igual a 30% do seu salário, que seria de: R${salário*0.3:.2f}.
De acordo com as políticas de nossa intituição bancária, o empréstimo não poderá ser realizado. ''')
elif prestação < salário*0.3:
    print('''De acordo com as análises do nosso sistema, o empréstimo poderá ser relizado!
Visto que o valor da prestação mensal não ultrapassa 30% do seu salário!''')
print('Obrigado por nos escolher!')
