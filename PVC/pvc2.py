import numpy as np

class Diferencas_Finitas_PVC2:

    # Construtor da classe: inicializa o número de pontos (n) e a função f(x, y)
    def __init__(self, n: int, fxy):
        self.n = n  # Número de subdivisões no domínio
        self.fxy = fxy  # Função que descreve o comportamento do problema no domínio

    # Método principal que resolve o sistema usando o método de diferenças finitas
    def metodo(self):
        # Discretização do domínio: delta_x e delta_y representam o tamanho das divisões em x e y
        delta_x = 1.0 / self.n  # Passo no eixo x
        delta_y = 1.0 / self.n  # Passo no eixo y
        tam = (self.n-1)**2  # Tamanho da matriz (n-1)x(n-1) para as equações lineares

        # Coeficientes usados para construir a matriz de diferenças finitas
        borda_x = 1 / (delta_x**2)  # Termo associado às diferenças na direção x
        centro = -2 * (1/(delta_x**2) + 1/(delta_y**2))  # Termo central que soma as contribuições de x e y
        borda_y = 1 / (delta_y**2)  # Termo associado às diferenças na direção y

        # Inicializa a matriz de coeficientes (matriz_A) com zeros
        matrix_A = np.zeros((tam, tam), dtype=float)

        # Variáveis auxiliares para montagem da matriz
        k = 0  # Contador para os elementos da matriz
        y = 0  # Contador para controle das bordas no eixo y

        # Loop para preencher a matriz de coeficientes com base nas condições de diferenças finitas
        for i in range(tam):
            # Preenche os coeficientes associados aos pontos vizinhos
            if i > 0:  # Termo da borda à esquerda
                k = k + 1
                if k % (self.n-1) != 0:  # Verifica se o ponto não está na borda
                    matrix_A[i][i-1] = borda_y  # Coloca o coeficiente da borda y
                else:
                    matrix_A[i][i-1] = 0  # Na borda, o valor é zero

            if i > (self.n-2):  # Termo da borda inferior
                matrix_A[i][i-(self.n-1)] = borda_x

            matrix_A[i][i] = centro  # Termo central (diagonal principal)

            if i < tam-(self.n-1):  # Termo da borda superior
                matrix_A[i][i+(self.n-1)] = borda_x

            if i < tam-1:  # Termo da borda à direita
                y = y + 1
                if y % (self.n-1) != 0:  # Verifica se o ponto não está na borda
                    matrix_A[i][i+1] = borda_y  # Coloca o coeficiente da borda y
                else:
                    matrix_A[i][i+1] = 0  # Na borda, o valor é zero

        # Vetor B à direita, preenchido com o valor da função f(x, y) fornecida
        matrix_B = np.empty((tam), dtype=float)
        matrix_B.fill(self.fxy)  # Preenche o vetor com o valor constante de fxy
        
        # Resolve o sistema de equações lineares A*x = B
        matrix_A_inv = np.linalg.inv(matrix_A)  # Calcula a inversa da matriz A
        result = np.dot(matrix_A_inv, matrix_B)  # Multiplica a inversa de A pelo vetor B para obter a solução

        return result  # Retorna o resultado do sistema
