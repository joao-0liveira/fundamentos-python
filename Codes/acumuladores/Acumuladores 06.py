print('\nPeça vários números até digitar 0. Mostre a soma apenas dos números ímpares.')

soma = 0
numero = int(input('Digite um número a seguir [Digite 0 para parar]: '))

while numero != 0:
    if numero % 2 != 0:
        soma = soma + numero
    numero = int(input('Digite um número a seguir [Digite 0 para parar]: '))

print(f'A soma de todos os números ímpares digitados é de: {soma}.')
