from pvc1 import Diferencas_Finitas_PVC1

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("           Método de Diferenças Finitas")
print("---------------------------------------------------\n")

pontos = [0.2, 0.3, 0.4, 0.5]
sol = Diferencas_Finitas_PVC1(3, pontos)

sol_aprox, sol_exata = sol.metodo()

print("PVC1\n")
print("------------------------------------------------------------------------------")
print("|      |   Solução aproximada    |    Solução exata    |    Erro relativo    |")
print("------------------------------------------------------------------------------")
for i in range(7):
    print("|  y{}  |   {:.8f}            |    {:.8f}       |    {:.2f}%            |"
    .format(i+1, sol_aprox[i], sol_exata[i], ((sol_aprox[i]-sol_exata[i])/sol_exata[i])*100))
    print("------------------------------------------------------------------------------")
