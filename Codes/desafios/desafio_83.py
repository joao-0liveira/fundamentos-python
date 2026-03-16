from colorama import Style, init

init(autoreset=False)



def area():
    calculo = a*b
    print(f'A área de um terreno {Style.BRIGHT}{a}x{b}{Style.RESET_ALL} é de: {Style.BRIGHT}{calculo}m^2{Style.RESET_ALL}.')

print()
a = float(input('Digite o valor do comprimento do terreno (m): '))
b = float(input('Digite o valor da largura do terreno (m): '))
print()
area()
