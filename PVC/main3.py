from pvc1_2 import Elementos_Finitos

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("           Método de Diferenças Finitas")
print("---------------------------------------------------\n")

pontos = [0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875]
sol = Elementos_Finitos(8, pontos)

sol_aprox, sol_exata = sol.metodo()

print("PVC1\n")
print("------------------------------------------------------------------------------")
print("|      |   Solução aproximada    |    Solução exata    |    Erro relativo    |")
print("------------------------------------------------------------------------------")
for i in range(7):
    print("|  y{}  |   {:.8f}            |    {:.8f}       |    {:.2f}%            |"
    .format(i+1, sol_aprox[i], sol_exata[i], ((sol_aprox[i]-sol_exata[i])/sol_exata[i])*100))
    print("------------------------------------------------------------------------------")
