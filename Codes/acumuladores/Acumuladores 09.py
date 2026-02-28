print('\nPeça números até digitar 0. Mostre a média dos valores digitados.')

numeros = int(input('Digite um valor a seguir [Digite 0 para parar]: '))
soma = 0
contador = 0

while numeros != 0:
    soma = soma + numeros
    contador = contador + 1
    numeros = int(input('Digite um valor a seguir [Digite 0 para parar]: '))

if contador != 0:
    print(f'\nA média dos {contador} números digitados é igual a: {soma/contador}.')
else:
    print('\nNão podemos realizar uma divisão por zero! Reinicie o programa!')
