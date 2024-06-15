import numpy as np

class Elementos_Finitos:

    # Construtor da classe, inicializa o número de pontos (n) e os pontos a serem utilizados
    def __init__(self, n: int, pontos):
        self.n = n  # Número de pontos
        self.pontos = pontos  # Lista de pontos no domínio do problema

    # Método principal que realiza a montagem e resolução do sistema usando o método dos elementos finitos
    def metodo(self):
        Li = 1.0/self.n  # Tamanho de cada elemento no domínio, variando de 0 a 1, dividido em n subintervalos
        tam = self.n-1  # Tamanho da matriz será n-1, pois trata-se de um problema com n-1 incógnitas

        # Inicializa a matriz de coeficientes K (n-1)x(n-1) com zeros
        K = np.zeros((tam, tam), dtype=float)

        # Valores das funções de interpolação nos extremos dos elementos (N_in = -1/2, N_fim = 1/2)
        N_in = -1/2
        N_fim = 1/2

        # Matriz auxiliar k_aux1 para o termo de rigidez (derivada das funções de forma)
        k_aux1 = [[(N_in**2) * (2/Li) * 2, (N_in) * (2/Li) * (N_fim) * 2],
                  [(N_fim) * (2/Li) * (N_in) * 2, (N_fim**2) * (2/Li) * 2]]
        k_aux1 = np.matrix(k_aux1)

        # Matriz auxiliar k_aux2 para o termo de massa (função de forma normal)
        k_aux2 = [[(Li/2) * (2/3), (Li/2) * (1/3)],
                  [(Li/2) * (1/3), (Li/2) * (2/3)]]
        k_aux2 = np.matrix(k_aux2)

        # Matriz elementar K_i obtida somando os dois termos (rigidez e massa)
        K_i = k_aux1 + k_aux2

        # Montagem da matriz de coeficientes K
        for i in range(tam):
            if i > 0:
                K[i][i-1] = K_i[0, 1]  # Termo fora da diagonal (contribuição entre elementos adjacentes)
            
            K[i][i] = 2 * K_i[0, 0]  # Termo na diagonal principal (contribuição do próprio elemento)

            if i < tam-1:
                K[i][i+1] = K_i[0, 1]  # Termo fora da diagonal (para elementos adjacentes à direita)

        # Vetor do lado direito B (representa as condições de contorno ou forças aplicadas)
        B = np.zeros(tam)
        B[tam-1] = -K_i[0, 1]  # Ajuste do valor em função das condições de contorno no final do domínio

        # Resolução do sistema de equações K * U = B para obter a solução aproximada (U)
        sol_aprox = np.linalg.solve(K, B)

        # Obtém a solução exata para comparação
        sol_exata = self.sol_exata()

        return sol_aprox, sol_exata

    # Método que calcula a solução exata do problema, baseada em uma expressão analítica conhecida
    def sol_exata(self):
        sol_exata = [0] * (self.n-1)  # Inicializa o vetor da solução exata com zeros
        for i in range(self.n-1):
            x = self.pontos[i]  # Para cada ponto, calcula a solução exata
            sol_exata[i] = (np.exp(-x) - np.exp(x)) / (np.exp(-1) - np.exp(1))  # Expressão analítica da solução

        return sol_exata  # Retorna a solução exata
