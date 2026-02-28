print('\nPeça números até o usúario digitar 0. Mostre a soma total e quantos números foram digitados (sem contar o 0).')

soma = 0 
contador = 0

numeros = int(input('Digite um número a seguir [Digite "0" para parar]: '))

while numeros != 0:
    soma = soma + numeros
    numeros = int(input('Digite um número a seguir [Digite "0" para parar]: '))
    contador = contador + 1

print(f'\nA soma total dos números digitados foi de: {soma}.')
print(f'A quantidade de números digitados foi de: {contador} números.')
