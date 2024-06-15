class Euler_Implicito:
    
    # Construtor da classe: inicializa os parâmetros do problema
    def __init__(self, delta_t):
        self.v0 = 5.0       # Velocidade inicial (m/s)
        self.y0 = 200.0     # Altura inicial (m)
        self.k = 0.25       # Constante de proporcionalidade (kg/s)
        self.m = 2          # Massa (kg)
        self.g = 10         # Aceleração gravitacional (m/s²)
        self.delta_t = delta_t  # Passo temporal para o método de Euler Implícito

    # Método que encontra os pontos críticos da trajetória, como altura máxima e tempo de impacto
    def pontos_criticos1(self):
        tempo = 0.0         # Tempo inicial (s)
        v_ant = self.v0     # Velocidade anterior, inicialmente v0
        y_ant = self.y0     # Altura anterior, inicialmente y0
        y_atual = y_ant     # Altura atual, inicialmente a mesma que y_ant

        # Laço para calcular a trajetória até que a altura chegue ao nível do mar (y = 0)
        while y_atual > 0:
            # Atualiza a velocidade e a altura usando o método de Euler Implícito
            v_atual, y_atual = self.euler_implicito(v_ant, y_ant)
            tempo += self.delta_t  # Incrementa o tempo com o passo delta_t

            # Verifica se a velocidade cruza zero, indicando a altura máxima (v(t) = 0)
            if v_atual * v_ant < 0:  # Mudança de sinal indica passagem pelo ponto crítico
                if y_ant > y_atual:
                    y_alt_max = y_ant  # Altura máxima da trajetória
                    t_alt_max = tempo - self.delta_t  # Tempo em que a altura máxima foi atingida
                else:
                    y_alt_max = y_atual  # Altura máxima da trajetória
                    t_alt_max = tempo  # Tempo em que a altura máxima foi atingida
            
            # Verifica se a altura cruza zero, indicando o fim da trajetória (y(t) = 0)
            if y_atual * y_ant < 0:  # Mudança de sinal indica que passou pelo nível do mar
                v_mar = v_ant  # Velocidade ao chegar ao mar
                t_mar = tempo - self.delta_t  # Tempo total da trajetória

            # Atualiza as variáveis para a próxima iteração
            v_ant = v_atual  # Atualiza a velocidade
            y_ant = y_atual  # Atualiza a altura
        
        # Retorna os pontos críticos: altura máxima, tempo da altura máxima, velocidade ao atingir o mar e tempo total da trajetória
        return y_alt_max, t_alt_max, v_mar, t_mar
    
    # Método que resolve a equação diferencial usando o método de Euler Implícito
    def euler_implicito(self, v_antigo, y_antigo):
        # Atualiza a velocidade utilizando o método de Euler Implícito
        v_atual = (self.m * (v_antigo - self.g * self.delta_t)) / (self.m + self.k * self.delta_t)

        # Atualiza a altura utilizando o método de Euler Implícito
        y_atual = y_antigo + (self.m * self.delta_t * (v_antigo - self.g * self.delta_t)) / (self.m + self.k * self.delta_t)

        # Retorna a nova velocidade e altura
        return v_atual, y_atual
