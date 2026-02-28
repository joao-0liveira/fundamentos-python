print('\nPeça números até digitar 0. Mostre no final: SOMA TOTAL - QUANTIDADE - MÉDIA - MAIOR - MENOR.')

numero = int(input('Digite um número a seguir: '))

soma = 0
contador = 0
maior = None
menor = None

while numero != 0:
    soma = soma + numero
    contador = contador + 1
    if maior is None:
        maior = numero
    elif numero > maior:
        maior = numero
    if menor is None:
        menor = numero
    elif numero < menor:
        menor = numero
    numero = int(input('Digite um número a seguir: '))

if contador != 0:
    print(f'''\nA soma de todos os números é igual a: {soma}.
Foram digitados: {contador} número(s).
A média dos números digitados é de: {soma/contador}.
O maior número digitado foi: {maior}.
E o menor número digitado foi: {menor}.''')
else: 
    print('\nNão é possível iniciar com zero. Reinicie o programa.')
