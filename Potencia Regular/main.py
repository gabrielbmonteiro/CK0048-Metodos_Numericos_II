from potencia_regular import Potencia_Regular

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("            Método da Potência Regular")
print("---------------------------------------------------\n")

print("Matriz A1: ")
print("----------")
A1 = [
[5, 2, 1],
[2, 3, 1],
[1, 1, 2]]

## autovalor e auto_vetor da matriz tridiagonal
autovalor, auv = Potencia_Regular(A1, [1, 1, 1], 0.00001)

print("Autovalor: {} \nAutovetor: [{}, {}, {}]\n\n".format(autovalor, auv[0], auv[1], auv[2]))

print("---------------------------------------------------")

print("Matriz A2: ")
print("----------")
A2 = [
[-40, 8, 4, 2, 1],
[8, -30, 12, 6, 2],
[4, 12, 20, 1, 2],
[2, 6, 1, 25, 4],
[1, 2, 2, 4, 5]]

## autovalor e auto_vetor da matriz tridiagonal
autovalor, auv = Potencia_Regular(A2, [1, 1, 1, 1, 1], 0.00001)

print("Autovalor: {} \nAutovetor: [{}, {}, {}, {}, {}]\n\n\n".format(autovalor, auv[0], auv[1], auv[2], auv[3], auv[4]))