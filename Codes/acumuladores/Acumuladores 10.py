print('\nPeça um número e quantos divisores ele possui.')

numero = int(input('Digite um número a seguir: '))
contador = 0

for c in range (1, numero+1):
    if numero % c == 0:
        contador = contador + 1

print(f'\nO total de divisores que o número {numero} possui é de: {contador} divisores.')
