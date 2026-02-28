print('\nPEÇA UM NÚMERO E CALCULE A SOMA DE TODOS OS NÚMEROS ATÉ ELE.')

contador = 1
soma = 0

escolha = int(input('\nDigite um número de sua escolha a seguir: '))

while contador <= escolha:
    soma = soma + contador
    
    contador = contador + 1

print(f'\nA soma de todos os números de 1 até {escolha} é: {soma}.')
