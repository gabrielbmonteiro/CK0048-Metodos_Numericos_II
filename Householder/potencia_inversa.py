from potencia_regular import Potencia_Regular
import numpy as np


# Metodo da potencia inversa é o metodo da potencia regular aplicada em cima da matriz inversa
def Potencia_Inversa(matriz, vetor, epson):
    """
    Implementa o método da potência inversa, que é o método da potência regular aplicado à matriz inversa.
    Esse método é utilizado para encontrar o autovalor de menor magnitude de uma matriz.
    
    Parâmetros:
    - matriz: matriz quadrada da qual queremos encontrar o autovalor de menor magnitude.
    - vetor: vetor inicial para a iteração.
    - epson: critério de convergência (erro máximo permitido entre iterações sucessivas).
    
    Retorna:
    - lambda_n_a1: o autovalor inverso, ou seja, o menor autovalor em magnitude da matriz original.
    - x_n: o autovetor correspondente.
    """
    
    # Calcula a matriz inversa de A
    a1_inversa = np.linalg.inv(matriz)

    # Aplica o método da potência regular à matriz inversa
    lambda1_a1, x_dominante = Potencia_Regular(a1_inversa, vetor, epson) # Vai devolver o autovalor dominante da matriz inversa (lambda)
    x_n = x_dominante
    
    # O autovalor da matriz original é o inverso do autovalor dominante da matriz inversa
    lambda_n_a1 = 1 / lambda1_a1

    # Retorna o autovalor e o autovetor correspondentes
    return [lambda_n_a1, x_n]