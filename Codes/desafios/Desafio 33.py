print('-=-'*6)
print(' '*2, 'DESAFIO 33')
print('-=-'*6)
print('''Olá! Seja muito bem-vindo ao nosso programa de calculadora de IMC.
Aqui você poderá consultar a sua situação de um adulto acordo com o seu peso e altura.''')
weight = float(input('Para iniciarmos, digite a seguir, o seu peso, em quilogramas: '))
height = float(input('Ótimo! Agora, digite a sua altora a seguir, em metros: '))
print(f'''O nosso sistema já captou os seus dados:
Massa: {weight}kg.
Altura: {height}m.''')
imc = weight/(height**2)
if imc < 18.5:
    print(f'''De acordo com as nossas análises, o seu IMC é de: {imc:.2f} kg/m².
Logo, você está ABAIXO DO PESO.''')
elif 18.5 < imc < 25:
    print(f'''De acordo com nossas análises, o seu IMC é de: {imc:.2f} kg/m².
Logo, você tem um PESO IDEAL!''')
elif 25 < imc < 30:
    print(f'''De acordo com nossas análises, o seu IMC é de: {imc:.2f} kg/m².
Logo, você está em SOBREPESO.''')
elif 30 < imc < 40:
    print(f'''De acordo com nossas análises, o seu IMC é de {imc:.2f} kg/m².
Logo, você se encontra em OBESIDADE.''')
else:
    print(f'''De acordo com nossas análises, o seu IMC é de {imc:.2f} kg/m².
Logo, você se encontra em OBESIDADE MÓRBITA.''')
