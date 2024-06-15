from qr import QR
import numpy as np

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                     QR")
print("---------------------------------------------------\n")


A = [
[9, 3, -4, 11],
[3, 33, -8, -4],
[-4, -8, 28, 25],
[11, -4, 25, 73]]

obj = QR(A, 4, 0.0000001)
P, lamb, A_nova = obj.metodo()

print("----------------------------------------------------------------------------------------\n")

print("Matriz Diagonal:")
print("-----------------")
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
       