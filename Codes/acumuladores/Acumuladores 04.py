print('\nPeça 10 números e mostre a SOMA TOTAL - QUANTOS SÃO PARES e ÍMPARES - QUAL O MAIOR NÚMERO.')

contador = 1
soma = 0
numero = 0
pares = 0
impares = 0
maior = None

while contador <= 10:
    numero = int(input('Digite um número a seguir: '))
    soma = soma + numero
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if maior is None:
        maior = numero
    elif numero > maior:
        maior = numero
    contador = contador + 1

print(f'\nA soma total dos números inseridos é de: {soma}.')
print(f'O número total de valores pares digitados foi de: {pares} números.')
print(f'E o total de ímpares foi de: {impares} números.')
print(f'O maior número digitado foi: {maior}.')
