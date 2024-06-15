from math import sin, cos, atan, fabs, pi
import numpy as np

# Classe para implementar o método QR para decomposição de matrizes e cálculo de autovalores e autovetores
class QR:
    def __init__(self, matriz, n, erro):
        self.a = matriz   # Matriz que será fatorada
        self.tam = n      # Tamanho da matriz (número de linhas/colunas)
        self.erro = erro  # Critério de erro para a convergência do método

    # Método principal que aplica a decomposição QR para encontrar os autovalores e autovetores
    def metodo(self):
        P = np.identity(self.tam, dtype=float)  # Matriz identidade que armazenará os autovetores
        np.set_printoptions(suppress=True)  # Define a impressão dos números para evitar notação científica
        val = 100  # Inicializa uma variável para o critério de convergência
        A_velha = self.a  # Inicializa A_velha como a matriz original
        A_nova = self.a   # Inicializa A_nova como a matriz original
        lamb = [0] * self.tam  # Vetor para armazenar os autovalores

        # Itera até que a soma dos quadrados dos termos abaixo da diagonal seja menor que o erro
        while val > self.erro:
            Q, R = self.decomposicaoQR(A_velha)  # Realiza a decomposição QR da matriz A_velha
            A_nova = R.dot(Q)  # Calcula A_nova como o produto R * Q
            A_velha = A_nova   # Atualiza A_velha para a próxima iteração
            P = P.dot(Q)       # Atualiza a matriz de autovetores
            val = self.somaDosQuadradosDosTermosAbaixoDaDiagonal(A_nova)  # Verifica o critério de convergência

        lamb = np.diag(A_nova)  # Extrai os autovalores da diagonal da matriz A_nova
        return P, lamb, A_nova  # Retorna a matriz de autovetores, os autovalores e a matriz final A_nova

    # Função que realiza a decomposição QR usando rotações de Jacobi
    def decomposicaoQR(self, A):
        QT = np.identity(self.tam, dtype=float)  # Inicializa QT como a matriz identidade
        R_velha = A  # Inicializa R_velha como a matriz original
        R_nova = A   # Inicializa R_nova como a matriz original
        
        # Laço para percorrer as colunas da matriz
        for j in range(0, self.tam-1):
            # Laço para percorrer as linhas abaixo da diagonal
            for i in range(j+1, self.tam):
                # Gera a matriz de rotação de Jacobi para zerar os elementos abaixo da diagonal
                J_ij = self.matrizJacobi(R_velha, i, j)
                R_nova = J_ij.dot(R_velha)  # Aplica a rotação de Jacobi
                R_velha = R_nova  # Atualiza R_velha para a próxima iteração
                QT = J_ij.dot(QT)  # Acumula as rotações de Jacobi em QT (transposta de Q)
                
                # Exibe a matriz R_nova em cada iteração
                print(f"Matriz R_nova da iteração ({i},{j})\n")
                print(R_nova)
                print("\n")

        Q = np.transpose(QT)  # Calcula Q como a transposta de QT
        return Q, R_nova  # Retorna Q e R da decomposição QR

    # Função que gera a matriz de rotação de Jacobi para azerar os elementos abaixo da diagonal
    def matrizJacobi(self, A, i, j):
        J_ij = np.identity(self.tam, dtype=float)  # Inicializa a matriz de rotação Jacobi como identidade
        ang = 0  # Ângulo de rotação
        erro = 10**(-6)  # Critério de erro para verificar valores próximos de zero

        # Se o elemento a[i,j] for muito pequeno, considera-se nulo e não aplica rotação
        if fabs(A[i][j]) <= erro:
            return J_ij
        
        # Se o elemento a[j,j] for pequeno, aplica-se uma rotação de ±pi/2 para zerar a[i,j]
        if fabs(A[j][j]) <= erro:
            if A[i][j] < 0:
                ang = pi/2
            else:
                ang = -pi/2
        else:
            # Calcula o ângulo de rotação com base nos elementos da matriz A
            ang = atan(-A[i][j] / A[j][j])
        
        # Preenche a matriz de rotação Jacobi J_ij com os valores de seno e cosseno do ângulo calculado
        J_ij[i][i] = cos(ang)
        J_ij[j][j] = cos(ang)
        J_ij[i][j] = sin(ang)
        J_ij[j][i] = -sin(ang)

        return J_ij  # Retorna a matriz de rotação Jacobi

    # Função que calcula a soma dos quadrados dos termos abaixo da diagonal para verificar a convergência
    def somaDosQuadradosDosTermosAbaixoDaDiagonal(self, A):
        soma = 0
        # Itera sobre os elementos abaixo da diagonal da matriz A
        for j in range(0, self.tam-1):
            for i in range(j+1, self.tam):
                soma += (A[i][j] * A[i][j])  # Soma os quadrados dos elementos
        return soma  # Retorna a soma dos quadrados
