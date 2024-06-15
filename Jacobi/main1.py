from jacobi1 import Jacobi1
import numpy as np

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                  Método de Jacobi")
print("---------------------------------------------------\n")


A = [[40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5]]

obj = Jacobi1(A, 5, 0.0000001)
P, lamb, A_nova = obj.metodo()

print("----------------------------------------------------------------------------------------\n")

print("Matriz Diagonal:")
print("------------------")
print(A_nova)
print("\n")

print("Matriz P:")
print("----------")
print(P)
print("\n")

P = np.transpose(P)

print("Pares Autovalor-Autovetor:")
print("---------------------------")
for i in range(obj.tam):
    print("Autovalor: {} \nAutovetor: {}\n".format(lamb[i], P[i]))

        