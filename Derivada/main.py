from polinomio import polinomio, derivada

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                     Derivada")
print("---------------------------------------------------\n")

grau = int(input("Insira o grau do polinômio >> "))
f = gerarfuncao() 
x_par = int(input("Insira o valor de x >> "))

z = 1 
while(z <5):
  print("Derivada de %d° ordem:"%z)
  print("forward >> %.5f"%derivada(f, x_par, 0.1, 'f', z))
  print("backward >> %.5f"%derivada(f, x_par, 0.1, 'b', z))
  print("cenral >> %.5f"%derivada(f, x_par, 0.1, 'c', z))
  z +=1