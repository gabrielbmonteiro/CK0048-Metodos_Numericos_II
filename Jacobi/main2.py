from jacobi2 import Jacobi2
from householder import metodo_house_holder
import numpy as np

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                  Método de Jacobi")
print("---------------------------------------------------\n")


A = [[40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]]

houseHold = metodo_house_holder(A, 5)
MatrizT, MatrizH = houseHold.metodo()

print("Matriz T:")
print("----------")
print(MatrizT)
print("\n")

print("Matriz H:")
print("----------")
print(MatrizH)
print("\n")

print("----------------------------------------------------------------------------------------\n")

jacobi = Jacobi2(MatrizT, 5, 0.0001)
P, lamb, A_nova = jacobi.metodo()

print("----------------------------------------------------------------------------------------\n")

print("Matriz P antes de P = H*P:")
print("---------------------------")
print(P)
print("\n")

P = MatrizH.dot(P)

print("Matriz P depois de P = H*P:")
print("---------------------------")
print(P)
print("\n")
    
P = np.transpose(P)
print("Pares Autovalor-Autovetor:")
print("---------------------------")
for i in range(jacobi.tam):
    print("Autovalor: {} \nAutovetor: {}\n".format(lamb[i], P[i]))