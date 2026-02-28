print('='*5, 'DESAFIO 23', '='*5)
print("""Olá! Seja bem-vindo ao nosso programa!
Aqui, você conseguirá realizar a pesquisa do valor da passagem da sua viagem!
Para isso, basta nos informar a distância total que será a sua viagem.
Para viagens de até 200km de distância, são cobrados R$0,50 por km,
E R$0,45 para viagens mais longas.""")
distância = float(input('A seguir, digite a distância total de sua viagem em km: '))
if distância <= 200:
    print(f"""Ótimo! Sua viagem será de: {distância}km,
E sua passagem custará: R${distância*0.5:.2f}.""")
else:
    print(f"""Ótimo! Sua viagem será de: {distância}km,
E sua passagem custará: R${distância*0.45:.2f}.""")
print("Faça uma boa viagem!")
