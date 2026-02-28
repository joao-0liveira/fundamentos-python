print('\nPEÇA UM NÚMERO INTEIRO E MOSTRE O RESULTADO DA MULTIPLICAÇÃO DELE POR 1 ATÉ 10 USANDO ACUMULADOR DE SOMA.')

contador = 1
acumulador = 0
resultado = 0
expressão = ''

número = int(input('\nDigite um número a seguir: '))

while contador < 10:
    resultado = número * contador
    acumulador = acumulador + resultado
    expressão = expressão + f' {resultado} +'
    contador = contador + 1

expressão = expressão + f' {número*10}'

print(f'o valor da expressão {expressão} é igual a: {acumulador+número*10}.')
