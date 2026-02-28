print('='*5, 'DESAFIO 21', '='*5)
print('Olá, Seja muito bem vindo ao nosso programa!')
print('Aqui você poderá verificar se existe alguma multa pendente em sua carteira de motorista.')
velocidade = int(input("""Para continuarmos, é necessário que saiba que o limite de velocidade da via é de: 80km/h
Além do mais, caso exceda o limite de velocidade, será aplicada uma multa de R$7,00 para cada km além do limite.
Para saber se há alguma multa pendente, digite a sua velocidade a seguir: """))
if velocidade > 80:
    print(f"""Você atingiu o limite de velocidade da via! A velocidade atingida por você foi de: {velocidade}km/h.
Isso implica em uma multa de: R${(velocidade-80)*7},00
Acesse o portal do condutor para obter mais informações para prosseguir com o pagamento.""")
else:
    print("""Não foi identificada nenhuma infração em nosso sistema!
Continue respeitando os limites das nossas vias!""")
print('Sessão finalizada!')
