from qr import QR
from householder import metodo_house_holder
import numpy as np

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("                     QR")
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

qr = QR(MatrizT, 5, 0.0000001)
P_barra, lamb, A_nova = qr.metodo()

print("----------------------------------------------------------------------------------------\n")

print("Matriz P antes de P = H*P:")
print("---------------------------")
print(P_barra)
print("\n")

P = MatrizH.dot(P_barra)

print("Matriz P depois de P = H*P:")
print("---------------------------")
print(P)
print("\n")
    
P = np.transpose(P)

print("Pares Autovalor-Autovetor:")
print("---------------------------")
for i in range(qr.tam):
    print("Autovalor: {} \nAutovetor: {}\n".format(lamb[i], P[i]))
