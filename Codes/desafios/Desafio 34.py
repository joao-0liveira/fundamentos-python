print('-=-'*6)
print(' '*2, 'DESAFIO 34')
print('-=-'*6)
print('''Olá! Seja bem vindo à sessão de pagamentos da loja Fellas Cuts LTDA.
Nesra sessão, você poderá concluir a sua compra selecionando o método de pagamento que preferir.''')
valor = float(input('Para darmos início, precisamos saber o valor do produto que deseja adquirir: R$'))
método = int(input('''Ótimo! Conheça as nossas opções de pagamentos e selecione a que melhor lhe atender:
Digite 0 para pagamento À VISTA (10% de desconto).
Digite 1 para pagamento À VISTA NO CARTÃO (5% de desconto).
Digite 2 para pagamento de 2x NO CARTÃO.
Digite 3 para pagamento de 3x OU MAIS NO CARTÃO (20% de juros).
Resposta: '''))
if método == 0:
    print(f'''Perfeito, você selecionou o método de pagamento à vista!
Com isso, você receberá um desconto de 10% no valor total da sua compra, que sairá por: R${valor-(valor*0.1):.2f}.''')
elif método == 1:
    print(f'''Perfeito, você  selecionou o método de pagamento à vista no cartão!
Com isso, você receberá um desconto de 5% no valor total da sua compra, que sairá por: R${valor-(valor*0.05):.2f}.
Para finalizar a sua compra, insira os dados do seu cartão a seguir.''')
elif método == 2:
    print(f'''Perfeito, você selecionou o método de pagamento em 2x vezes no cartão!
O valor da parcela da sua compra será de: R${valor/2:.2f}.
Para continuar a sua compra, insira os dados cartão a seguir e finalize a sua compra!''')
else:
    print(f'''Perfeito, você selecionou o método de pagamento em 3x ou mais no cartão!
Com isso, haverá um juros de 20% no valor total da compra, que, no final, sairá por: R${valor*1.2:.2f}.
A seguir, insira os dados do seu cartão e finalize a sua compra!''')
