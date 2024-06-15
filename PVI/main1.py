from Euler_Explicito import Euler_Explicito

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("          Método de Diferenças Infinitas")
print("---------------------------------------------------\n")

print("Solução aproximada do PVI utilizando o método de Euler Explícito\n")
print("--------------------------------------------------------------------------------------------------")
print("|   delta_t(s)   |   alt_max(m)   |   temp_alt_max(s)   |   vel_final(m/s)   |   temp_final(s)   |")
print("--------------------------------------------------------------------------------------------------")

for i in range(1, 5):
    sol = Euler_Explicito(10**(-i))
    y_alt_max, t_alt_max, v_mar, t_mar = sol.pontos_criticos1()
    print("    {}              {:.4f}         {:.4f}                {:.4f}                 {:.4f}"
    .format(10**(-i), y_alt_max, t_alt_max, v_mar, t_mar))
    print("--------------------------------------------------------------------------------------------------")