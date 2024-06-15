from math import sqrt
import numpy as np

class metodo_house_holder:
    def __init__(self, matriz, tam):
        """
        Inicializa a classe com a matriz de entrada 'matriz' e o tamanho 'tam'.
        """

        self.a = matriz  # A matriz original que será tridiagonalizada
        self.tam = tam   # O tamanho da matriz (número de linhas/colunas)

    def metodo(self):
        """
        Aplica o método de Householder para transformar a matriz simétrica
        em uma matriz tridiagonal.
        """

        H = np.identity(self.tam, dtype=float) # Inicializa a matriz identidade H
        np.set_printoptions(suppress=True) # Desativa a notação científica para impressões menores que 1e-4
        A_ant = self.a  # Armazena a matriz original, que será modificada
        A_barra = self.a  # Inicializa a matriz tridiagonal que será gerada

        # Itera até a penúltima coluna, pois não há necessidade de zerar a última coluna
        for i in range(self.tam - 2): 
            H_i = self.matriz_householder(A_ant, i) # Calcula a matriz de Householder H_i
            aux1 = np.transpose(H_i).dot(A_ant) # Aplica a transformação de similaridade: H_i^T * A
            A_barra = aux1.dot(H_i) # H_i^T * A * H_i (zera os elementos abaixo da diagonal da coluna i)
            A_ant = A_barra # Atualiza A_ant para a próxima iteração
            H = H.dot(H_i) # Acumula as matrizes H_i (H_final = H_1 * H_2 * ... * H_n)

        # Ao final, A_barra será a matriz tridiagonal e H é a matriz acumulada das transformações
        return A_barra, H  # usaremos H para conseguir os autovetores da matriz inicial (A), que é h*autovaloresMatrizT 

    def matriz_householder(self, matriz, i):
        """
        Calcula a matriz de Householder para zerar os elementos abaixo da diagonal
        na i-ésima coluna da matriz simétrica.
        """

        w = [0] * self.tam  # Vetor auxiliar para armazenar os elementos abaixo da diagonal
        w2 = [0] * self.tam  # Vetor para armazenar o comprimento do vetor w
        n = [0] * self.tam  # Vetor normalizado N 
        
        # Copia os elementos abaixo da diagonal da coluna i para o vetor w
        for indice in range(i + 1, self.tam):
            w[indice] = matriz[indice][i]
        
        # Calcula a norma de w e armazena o comprimento em w2
        w2[i + 1] = sqrt(self.vetor_x_vetor(w, w))

        # Subtrai w de w2 (N = w - w')
        N = np.subtract(w, w2)
        
        # Normaliza o vetor N
        comp = sqrt(self.vetor_x_vetor(N, N))
        for indice2 in range(self.tam):
            n[indice2] = N[indice2]/comp
        
        # Monta a matriz de HouseHolder H = I - 2 * n * n^T
        I = np.identity(self.tam, dtype=float)
        aux1 = self.const_x_vetor(2, n) # 2 * n
        H = np.subtract(I, self.vetor_x_vetor2(aux1, n)) # H = I - 2 * n * n^T
        
        return H
    
    def vetor_x_vetor(self, v1, v2):
        """
        Produto escalar de dois vetores.
        """

        s = 0
        for i in range(self.tam):
            s = s + v1[i]*v2[i]
        return s

    def const_x_vetor(self, n, v):
        """
        Multiplica um vetor 'v' por uma constante 'n'.
        """

        res = [0] * self.tam
        for i in range(self.tam):
            res[i] = n*v[i]
        return res

    def vetor_x_vetor2(self, v1, v2):
        """
        Calcula o produto de dois vetores v1 e v2, retornando uma matriz.
        """
        
        mat = np.identity(self.tam, dtype=float)
        for i in range(self.tam):
            for j in range(self.tam):
                mat[i][j] = v1[i]*v2[j]
        return mat