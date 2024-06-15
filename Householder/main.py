from householder import metodo_house_holder
from potencia_regular import Potencia_Regular
from potencia_inversa import Potencia_Inversa
from potencia_deslocamento import Potencia_Deslocamento

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("               Método de Householder")
print("---------------------------------------------------\n")


A = [[-40, 8,  4,  2,  1],
    [8,  -30, 12, 6,  2],
    [4,  12, 20, 1,  2],
    [2,  6,  1,  25, 4],
    [1,  2,  2,  4,  5]]
v0 = [1, 0, 0, 0, 0]

hh = metodo_house_holder(A, 5)

tridiagonal, H = hh.metodo()

print("Matriz Tridiagonal:")
print("------------------")
print(tridiagonal)

print("\nMatriz H acumulada:")
print("-------------------")
print(H)

print("\n----------------------------------------------------------------------------------------\n")

lambda1_PR, x1_PR = Potencia_Regular(tridiagonal, v0, 0.00001)

lambda1_PD1, x1_PD1 = Potencia_Deslocamento(tridiagonal, v0, 0.00001, 30)
lambda1_PD2, x1_PD2 = Potencia_Deslocamento(tridiagonal, v0, 0.00001, 20)
lambda1_PD3, x1_PD3 = Potencia_Deslocamento(tridiagonal, v0, 0.00001, 8)

lambda1_PI, x1_PI = Potencia_Inversa(tridiagonal, v0, 0.00001)

print("Matriz Tridiagonal:")
print("------------------")
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PR, x1_PR))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD1, x1_PD1))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD2, x1_PD2))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD3, x1_PD3))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PI, x1_PI))

print("\n----------------------------------------------------------------------------------------\n")

lambda1_PR_A1, x1_PR_A1 = Potencia_Regular(A, v0, 0.00001)

lambda1_PD1_A1, x1_PD1_A1 = Potencia_Deslocamento(A, v0, 0.00001, 30)
lambda1_PD2_A1, x1_PD2_A1 = Potencia_Deslocamento(A, v0, 0.00001, 20)
lambda1_PD3_A1, x1_PD3_A1 = Potencia_Deslocamento(A, v0, 0.00001, 8)

lambda1_PI_A1, x1_PI_A1 = Potencia_Inversa(A, v0, 0.00001)

print("Matriz A:")
print("----------")
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PR_A1, x1_PR_A1))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD1_A1, x1_PD1_A1))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD2_A1, x1_PD2_A1))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PD3_A1, x1_PD3_A1))
print("Autovalor: {} \nAutovetor: {}\n".format(lambda1_PI_A1, x1_PI_A1))
