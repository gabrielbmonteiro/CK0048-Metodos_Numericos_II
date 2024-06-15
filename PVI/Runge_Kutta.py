class Runge_Kutta:

    # Construtor da classe: inicializa os parâmetros do problema
    def __init__(self, delta_t):
        self.v0 = 5.0       # Velocidade inicial (m/s)
        self.y0 = 200.0     # Altura inicial (m)
        self.k = 0.25       # Constante de proporcionalidade (kg/s)
        self.m = 2          # Massa (kg)
        self.g = 10         # Aceleração gravitacional (m/s²)
        self.delta_t = delta_t  # Passo temporal para o método de Runge-Kutta

    # Método que encontra os pontos críticos da trajetória, como altura máxima e tempo de impacto
    def pontos_criticos(self):
        tempo = 0.0         # Tempo inicial (s)
        v_ant = self.v0     # Velocidade anterior, inicialmente v0
        y_ant = self.y0     # Altura anterior, inicialmente y0
        y_atual = y_ant     # Altura atual, inicialmente a mesma que y_ant

        # Laço para calcular a trajetória até que a altura chegue ao nível do mar (y = 0)
        while(y_atual > 0):
            # Atualiza a velocidade e altura aproximadas com base no método de Runge-Kutta
            v_atual, y_atual = self.sol_aproximada(v_ant, y_ant)
            tempo = tempo + self.delta_t  # Incrementa o tempo com o passo delta_t

            # Verifica se a velocidade cruza zero, indicando a altura máxima (v(t) = 0)
            if(v_atual * v_ant < 0):  # Mudança de sinal indica que passou pelo ponto crítico
                if(y_ant > y_atual):
                    y_alt_max = y_ant  # Altura máxima da trajetória
                    t_alt_max = tempo - self.delta_t  # Tempo em que a altura máxima foi atingida
                else:
                    y_alt_max = y_atual  # Altura máxima da trajetória
                    t_alt_max = tempo  # Tempo em que a altura máxima foi atingida

            # Verifica se a altura cruza zero, indicando o fim da trajetória (y(t) = 0)
            if(y_atual * y_ant < 0):  # Mudança de sinal indica que passou pelo nível do mar
                v_mar = v_ant  # Velocidade ao chegar ao mar
                t_mar = tempo - self.delta_t  # Tempo total da trajetória

            # Atualiza as variáveis para a próxima iteração
            v_ant = v_atual
            y_ant = y_atual

        # Retorna os pontos críticos: altura máxima, tempo da altura máxima, velocidade ao atingir o mar e tempo total da trajetória
        return y_alt_max, t_alt_max, v_mar, t_mar

    # Função auxiliar 1: calcula a derivada da velocidade e da altura
    def auxiliar1(self, v_ant):
        result1 = [0] * 2  # Vetor de retorno: posição 0 é a aceleração, posição 1 é a velocidade (v_ant)

        # Equação da aceleração resultante (considerando resistência do ar e gravidade)
        result1[0] = -self.g - ((self.k / self.m) * v_ant)  # Aceleração
        result1[1] = v_ant  # A velocidade atual é a própria derivada da altura

        return result1

    # Função auxiliar 2: calcula uma correção intermediária usando um passo de metade do delta_t
    def auxiliar2(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)

        # Calcula a velocidade aproximada no ponto intermediário (Equação 48)
        v_aux2 = v_ant + (self.delta_t / 2) * auxiliar1[0]

        # Usa a nova velocidade intermediária para calcular novamente a derivada
        result2 = self.auxiliar1(v_aux2)

        return result2

    # Função auxiliar 3: calcula outra correção intermediária mais refinada
    def auxiliar3(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)

        # Calcula a velocidade aproximada usando uma combinação dos resultados anteriores (Equação 50)
        v_aux3 = v_ant + self.delta_t * (-auxiliar1[0] + 2 * auxiliar2[0])

        # Usa essa nova velocidade para calcular a derivada final
        result3 = self.auxiliar1(v_aux3)

        return result3

    # Método principal que calcula a solução aproximada usando o método de Runge-Kutta
    def sol_aproximada(self, v_ant, y_ant):
        auxiliar1 = self.auxiliar1(v_ant)
        auxiliar2 = self.auxiliar2(v_ant)
        auxiliar3 = self.auxiliar3(v_ant)

        result = [0] * 2  # Vetor de resultados: posição 0 é a nova velocidade, posição 1 é a nova altura

        # Aplica o método de Runge-Kutta para calcular a nova velocidade (Equação 52)
        result[0] = v_ant + self.delta_t * ((auxiliar1[0] + 4 * auxiliar2[0] + auxiliar3[0]) / 6)

        # Aplica o método de Runge-Kutta para calcular a nova altura (Equação 52)
        result[1] = y_ant + self.delta_t * ((auxiliar1[1] + 4 * auxiliar2[1] + auxiliar3[1]) / 6)

        return result[0], result[1]  # Retorna a nova velocidade e altura
