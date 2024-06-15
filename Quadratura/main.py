from legendre import gauss_Legendre_2pontos, gauss_Legendre_3pontos, gauss_Legendre_4pontos
from hermite import gauss_Hermite_2pontos, gauss_Hermite_3pontos, gauss_Hermite_4pontos
from laguerre import gauss_Laguerre_2pontos, gauss_Laguerre_3pontos, gauss_Laguerre_4pontos
from chebyshev import gauss_Chebyshev_2pontos, gauss_Chebyshev_3pontos, gauss_Chebyshev_4pontos

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                   Quadraturas")
print("---------------------------------------------------\n")

print("Qual Quadratura você deseja utilizar?")
print("1 - Quadratura de Gauss-Legendre")
print("2 - Quadratura de Gauss-Hermite")
print("3 - Quadratura de Gauss-Laguerre")
print("4 - Quadratura de Gauss-Chebyshev")
response1 = input('Resposta: ')
response1 = int(response1)


print("Quantos pontos você deseja utilizar?")
print("1 - Dois pontos")
print("2 - Três pontos")
print("3 - Quatro pontos")
response2 = input('Resposta: ')
response2 = int(response2)

a = input('Qual será o intervalo [a]? ')
a = int(a)
b = input('Qual será o intervalo [b]? ')
b = int(b)

epson = input('Qual será o erro aproximado? ex: 0.000001\n')
epson = float(epson)


if response1==1:
    if response2==1:
        result_grau2 = gauss_Legendre_2pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau2[1])
        print("      Interações: " , result_grau2[0])
        print("     --------------------------------")
        
    elif response2==2:
        result_grau3 = gauss_Legendre_3pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau3[1])
        print("      Interações: " , result_grau3[0])
        print("     --------------------------------")

    elif response2==3:
        result_grau4 = gauss_Legendre_4pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau4[1])
        print("      Interações: " , result_grau4[0])
        print("     --------------------------------")

if response1==2:
    if response2==1:
        result_grau2 = gauss_Hermite_2pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau2[1])
        print("      Interações: " , result_grau2[0])
        print("     --------------------------------")
        
    elif response2==2:
        result_grau3 = gauss_Hermite_3pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau3[1])
        print("      Interações: " , result_grau3[0])
        print("     --------------------------------")

    elif response2==3:
        result_grau4 = gauss_Hermite_4pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau4[1])
        print("      Interações: " , result_grau4[0])
        print("     --------------------------------")

if response1==3:
    if response2==1:
        result_grau2 = gauss_Laguerre_2pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau2[1])
        print("      Interações: " , result_grau2[0])
        print("     --------------------------------")
        
    elif response2==2:
        result_grau3 = gauss_Laguerre_3pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau3[1])
        print("      Interações: " , result_grau3[0])
        print("     --------------------------------")

    elif response2==3:
        result_grau4 = gauss_Laguerre_4pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau4[1])
        print("      Interações: " , result_grau4[0])
        print("     --------------------------------")

if response1==4:
    if response2==1:
        result_grau2 = gauss_Chebyshev_2pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau2[1])
        print("      Interações: " , result_grau2[0])
        print("     --------------------------------")
        
    elif response2==2:
        result_grau3 = gauss_Chebyshev_3pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau3[1])
        print("      Interações: " , result_grau3[0])
        print("     --------------------------------")

    elif response2==3:
        result_grau4 = gauss_Chebyshev_4pontos(a, b, epson)
        print("\n     --------------------------------")
        print("      Resultado: " , result_grau4[1])
        print("      Interações: " , result_grau4[0])
        print("     --------------------------------")