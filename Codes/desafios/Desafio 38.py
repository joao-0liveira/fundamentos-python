print('-=-'*6)
print(' '*2, 'DESAFIO 38')
print('-=-'*6)
print('Bem vindo ao nosso programa! Aqui você poderá o somatório de todos os números ímpares múltiplos de 3 de 1 até 500!')
soma = 0
qtde = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
        qtde = qtde + 1 
print(f'A soma dos {qtde} os valores é igual a: {soma}.')
print('PROGRAMA FINALIZADO!')

#soma = 0
#for c in range(1, 6):
#    soma = soma + c
#print(soma)
