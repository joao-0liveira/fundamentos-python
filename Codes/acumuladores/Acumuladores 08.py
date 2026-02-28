print('\nPeça números até digitar 0. Mostre o maior número digitado.')

numeros = int(input('Digite um número a seguir: '))
maior = None

while numeros != 0:
    if maior is None:
        maior = numeros
    elif numeros > maior:
        maior = numeros
    numeros = int(input('Digite um número a seguir: '))
    
print(f'\nO maior número digitado foi: {maior}.')
