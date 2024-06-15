from math import sin, cos, atan, fabs, degrees, pi
import numpy as np

class Jacobi1:
    def __init__(self, matriz, n, erro):
        """
        Inicializa a classe com a matriz a ser diagonalizada, o tamanho da matriz e o erro tolerado.
        
        Parâmetros:
        - matriz: A matriz a ser diagonalizada.
        - n: O tamanho da matriz (n x n).
        - erro: O valor de tolerância para a convergência do método.
        """

        self.a = matriz
        self.tam = n
        self.erro = erro


    def metodo(self):
        """
        Aplica o método de Jacobi para diagonalizar a matriz.
        
        Retorna:
        - P: Matriz ortogonal de transformação.
        - lamb: Lista contendo os autovalores resultantes.
        - A_nova: Matriz tridiagonal resultante após a convergência.
        """
        # Inicializa a matriz de transformação ortogonal P e a matriz J (identidade)
        P = np.identity(self.tam, dtype=float)
        J = np.identity(self.tam, dtype=float)
        np.set_printoptions(suppress=True) # Configura a impressão para não usar notação científica
        
        A_velha = self.a
        A_nova = self.a
        lamb = [0] * self.tam # Lista para armazenar os autovalores
        val = 100 # Inicializa o critério de convergência

        # Loop até que a soma dos quadrados dos elementos fora da diagonal seja menor que o erro tolerado
        while(val > self.erro):
            A_nova, J = self.varreduraJacobi(A_velha) # Aplica a varredura de Jacobi
            A_velha = A_nova
            P = P.dot(J) # Atualiza a matriz de transformação
            val = self.soma_quadrados(A_nova) # Atualiza o valor da soma dos quadrados

        # Extrai os autovalores da diagonal da matriz tridiagonal
        for i in range(self.tam):
            lamb[i] = A_nova[i][i]

        return P, lamb, A_nova

    
    def varreduraJacobi(self, A):
        """
        Aplica a varredura de Jacobi para encontrar os autovalores e autovetores.
        
        Parâmetros:
        - A: A matriz atual a ser diagonalizada.
        
        Retorna:
        - A_nova: A matriz atualizada após a varredura.
        - J: A matriz acumulada de transformação.
        """

        J = np.identity(self.tam, dtype=float) # Inicializa a matriz identidade
        A_velha = A
        A_nova = A
        
        # Percorre os pares de índices para aplicar as rotações de Jacobi
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                J_ij = self.matrizJacobi(A_velha, i, j) # Calcula a matriz de rotação de Jacobi
                aux1 = np.transpose(J_ij).dot(A_velha) # Calcula A' = J_ij^T * A
                A_nova = aux1.dot(J_ij) # Atualiza A_nova = A' * J_ij
                A_velha = A_nova
                aux2 = J
                J = aux2.dot(J_ij) # Atualiza a matriz de transformação acumulada
                
                # Impressão das matrizes intermediárias (para depuração)
                print("Matriz A_nova da iteração ({},{}):".format(i, j))
                print("---------------------------------")
                print(A_nova)
                print("\n")
                print("Matriz J da iteração ({},{}):".format(i, j))
                print("----------------------------")
                print(J)
                print("\n")
        
        return A_nova, J


    def matrizJacobi(self, A, i, j):
        """
        Calcula a matriz de rotação de Jacobi para eliminar o elemento A[i][j].
        
        Parâmetros:
        - A: A matriz atual.
        - i: Índice da linha.
        - j: Índice da coluna.
        
        Retorna:
        - J_ij: A matriz de rotação de Jacobi.
        """

        J_ij = np.identity(self.tam, dtype=float) # Inicializa a matriz identidade
        ang = 0
        erro = 10**(-6) # Tolerância para precisão numérica

        # Se o elemento a ser eliminado é muito pequeno, retorna a matriz identidade
        if(fabs(A[i][j]) <= erro):
            return J_ij
        
        # Calcula o ângulo de rotação para eliminar o elemento A[i][j]
        if(fabs(A[i][i] - A[j][j]) <= erro):
            ang = pi/4
        else:
            ang = (1/2)*atan((-2*A[i][j])/(A[i][i]-A[j][j]))
        
        # Define os elementos da matriz de rotação J_ij
        J_ij[i][i] = cos(ang)
        J_ij[j][j] = cos(ang)
        J_ij[i][j] = sin(ang)        
        J_ij[j][i] = -sin(ang)

        return J_ij


    def soma_quadrados(self, A):
        """
        Calcula a soma dos quadrados dos elementos fora da diagonal da matriz.
        
        Parâmetros:
        - A: A matriz a ser analisada.
        
        Retorna:
        - soma: A soma dos quadrados dos elementos fora da diagonal.
        """

        soma = 0
        # Percorre os elementos fora da diagonal para calcular a soma dos quadrados
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                soma = soma + (A[i][j]*A[i][j])
        
        return soma