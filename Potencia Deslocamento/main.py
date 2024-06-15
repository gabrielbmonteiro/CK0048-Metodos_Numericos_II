from potencia_deslocamento import Potencia_Deslocamento

print("\n-------------- BEM VINDO AO PROGRAMA --------------")
print("        Método da Potência com Deslocamento")
print("---------------------------------------------------\n")


print("Matriz A3: ")
print("----------")
A3 = [
[9, 3, -4, 11],
[3, 33, -8, -4],
[-4, -8, 28, 25],
[11, -4, 25, 73]]

## autovalor e auto_vetor da matriz tridiagonal
autovalor, auv = Potencia_Deslocamento(A3, [1, 1, 1, 1], 0.00001, 120)

print("Autovalor: {} \nAutovetor: [{}, {}, {}, {}]\n\n\n".format(autovalor, auv[0], auv[1], auv[2], auv[3]))