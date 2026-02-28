print('\nPeça um número e calcule o produto de todos os números pares entre 1 e ele.')

numero = int(input('Digite um número de sua escolha a seguir: '))
produto = 1
for c in range (2, numero+1, 2):
    produto = produto * c

print(f'\nO produto dos números requeridos é igual a: {produto}.')
