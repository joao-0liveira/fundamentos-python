print('\nPEÇA 5 NÚMEROS AO USUÁRIO E MOSTRE A SOMA TOTAL NO FINAL.')

soma = 0
contador = 1

while contador <= 5:
    número = int(input('\nDigite um número a seguir: '))
    soma = soma + número
    contador = contador + 1     #SEMPRE QUE FOR TRABALHAR COM UMA CONTAGEM EM 'WHILE', DEVE-SE UTILIZAR UM CONTADOR

print(f'\nA soma dos cinco números é igual a: {soma}.')
