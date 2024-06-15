import numpy as np

class Diferencas_Finitas_PVC1:

    # Construtor da classe: inicializa o número de pontos (n) e os pontos discretos no intervalo [0, 1]
    def __init__(self, n: int, pontos):
        self.n = n  # Número de subdivisões no domínio
        self.pontos = pontos  # n-1 pontos discretos no intervalo [0, 1]

    # Método principal que resolve o sistema usando o método de diferenças finitas
    def metodo(self):
        delta_x = 1.0 / self.n  # Passo no eixo x, discretizando o intervalo [0, 1]
        tam = self.n - 1  # Número de pontos discretos no intervalo (n-1)

        # Coeficientes da equação de diferenças finitas
        centro = -(2/(delta_x**2) + 1)  # Coeficiente central
        borda = 1 / (delta_x**2)  # Coeficiente das bordas (vizinhos)

        # Inicializa a matriz de coeficientes (matrix_A) com zeros
        matrix_A = np.zeros((tam, tam))

        # Loop para preencher a matriz de coeficientes com base nas condições de diferenças finitas
        for i in range(tam):
            if i > 0:  # Preenche a borda à esquerda (termo da diagonal inferior)
                matrix_A[i][i-1] = borda
            
            matrix_A[i][i] = centro  # Preenche o termo central (diagonal principal)

            if i < tam-1:  # Preenche a borda à direita (termo da diagonal superior)
                matrix_A[i][i+1] = borda

        # Vetor de termos independentes (matrix_b), que representa o lado direito do sistema
        matrix_b = [0] * tam  # Inicializa o vetor com zeros
        matrix_b[tam-1] = -borda  # Condição de contorno no último ponto

        # Resolve o sistema linear matrix_A * x = matrix_b
        sol_aprox = np.linalg.solve(matrix_A, matrix_b)  # Solução aproximada do sistema
        sol_exata = self.sol_exata()  # Calcula a solução exata para comparação

        return sol_aprox, sol_exata  # Retorna a solução aproximada e a solução exata

    # Método para calcular a solução exata da equação diferencial no intervalo [0, 1]
    def sol_exata(self):
        sol_exata = [0] * (self.n-1)  # Inicializa a lista para a solução exata
        for i in range(self.n-1):
            x = self.pontos[i]  # Pega o ponto no intervalo
            # Calcula a solução exata no ponto x usando a fórmula analítica
            sol_exata[i] = (np.exp(-x) - np.exp(x)) / (np.exp(-1) - np.exp(1))

        return sol_exata  # Retorna a solução exata
