class Preditor_Corretor:

    # Construtor da classe: inicializa os parâmetros do problema
    def __init__(self, delta_t):
        self.v0 = 5.0       # Velocidade inicial (m/s)
        self.y0 = 200.0     # Altura inicial (m)
        self.k = 0.25       # Constante de proporcionalidade (kg/s)
        self.m = 2          # Massa (kg)
        self.g = 10         # Aceleração gravitacional (m/s²)
        self.delta_t = delta_t  # Passo temporal

    # Método que encontra os pontos críticos da trajetória, como altura máxima e tempo de impacto
    def pontos_criticos(self):
        tempo = 0.0         # Tempo inicial (s)
        v_ant = self.v0     # Velocidade anterior, inicialmente v0
        y_ant = self.y0     # Altura anterior, inicialmente y0
        y_atual = y_ant     # Altura atual, inicialmente a mesma que y_ant

        # Inicializa os estados iniciais pelo método de Runge-Kutta de terceira ordem
        estados_ant = self.inicializacao()

        # Laço para calcular a trajetória até que a altura chegue ao nível do mar (y = 0)
        while(y_atual > 0):
            # Atualiza a velocidade e altura usando o método Preditor-Corretor
            v_atual, y_atual = self.PredicaoCorrecao(estados_ant)
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

            # Atualiza os estados antigos para a próxima iteração
            aux  = estados_ant[2:]
            aux.append(v_atual)
            aux.append(y_atual)
            estados_ant = aux

            # Atualiza as variáveis para a próxima iteração
            v_ant = v_atual
            y_ant = y_atual

        # Retorna os pontos críticos: altura máxima, tempo da altura máxima, velocidade ao atingir o mar e tempo total da trajetória
        return y_alt_max, t_alt_max, v_mar, t_mar

    # Método Preditor-Corretor para calcular as novas velocidade e altura
    def PredicaoCorrecao(self, estados_ant):
        # Calcula as aproximações anteriores (Fi-3, Fi-2, Fi-1, Fi)
        auxiliar1 = self.auxiliar1(estados_ant[0])  # Fi-3
        auxiliar2 = self.auxiliar1(estados_ant[2])  # Fi-2
        auxiliar3 = self.auxiliar1(estados_ant[4])  # Fi-1
        auxiliar4 = self.auxiliar1(estados_ant[6])  # Fi

        predicao = [0] * 2  # Vetor de predição para velocidade e altura

        # Fórmula de predição de quarta ordem
        predicao[0] = estados_ant[6] + (self.delta_t / 24) * (-9 * auxiliar1[0] + 33 * auxiliar2[0] - 59 * auxiliar3[0] + 55 * auxiliar4[0])
        predicao[1] = estados_ant[7] + (self.delta_t / 24) * (-9 * auxiliar1[1] + 33 * auxiliar2[1] - 59 * auxiliar3[1] + 55 * auxiliar4[1])

        correcao = [0] * 2  # Vetor de correção para velocidade e altura
        auxiliar_pred = self.auxiliar1(predicao[0])  # Fi da predição

        # Fórmula de correção de quarta ordem
        correcao[0] = estados_ant[6] + (self.delta_t / 24) * (auxiliar2[0] - 5 * auxiliar3[0] + 19 * auxiliar4[0] + 9 * auxiliar_pred[0])
        correcao[1] = estados_ant[7] + (self.delta_t / 24) * (auxiliar2[1] - 5 * auxiliar3[1] + 19 * auxiliar4[1] + 9 * auxiliar_pred[1])

        return correcao[0], correcao[1]  # Retorna a velocidade e altura corrigidas

    # Inicializa os estados S0, S1, S2 e S3 usando o método de Runge-Kutta de terceira ordem
    def inicializacao(self):
        v_ant = self.v0  # Velocidade inicial
        y_ant = self.y0  # Altura inicial

        # Calcula os estados iniciais com Runge-Kutta
        estados = self.sol_aproximada(v_ant, y_ant)

        return estados  # Retorna o vetor de estados

    # Função auxiliar que retorna as derivadas da velocidade e altura para um dado valor de velocidade
    def auxiliar1(self, v_ant):
        result1 = [0] * 2  # Vetor: posição 0 é a derivada da velocidade (aceleração), posição 1 é a própria velocidade

        # Calcula a aceleração (-g - k/m * v_ant)
        result1[0] = -self.g - ((self.k / self.m) * v_ant)
        result1[1] = v_ant  # A derivada da altura é a própria velocidade

        return result1

    # Função auxiliar que calcula a velocidade e altura intermediárias
    def auxiliar2(self, v_ant):
        auxiliar1 = self.auxiliar1(v_ant)

        # Calcula a velocidade intermediária no ponto médio
        v_aux2 = v_ant + (self.delta_t / 2) * auxiliar1[0]

        # Calcula a nova aceleração e velocidade para essa velocidade intermediária
        result2 = self.auxiliar1(v_aux2)

        return result2

    # Função auxiliar que refina a estimativa da velocidade e altura intermediárias
    def auxiliar3(self, v_ant):
        auxiliar2 = self.auxiliar2(v_ant)

        # Calcula uma nova velocidade intermediária mais refinada
        v_aux3 = v_ant + (self.delta_t / 2) * auxiliar2[0]

        # Calcula a nova aceleração e velocidade para essa nova estimativa
        result3 = self.auxiliar1(v_aux3)

        return result3

    # Função auxiliar final para a correção completa das estimativas
    def auxiliar4(self, v_ant):
        auxiliar3 = self.auxiliar3(v_ant)

        # Calcula a estimativa final de velocidade e aceleração
        v_aux4 = v_ant + self.delta_t * auxiliar3[0]

        # Calcula a nova aceleração e velocidade
        result4 = self.auxiliar1(v_aux4)

        return result4

    # Método que calcula a solução aproximada usando Runge-Kutta de terceira ordem
    def sol_aproximada(self, v_ant, y_ant):
        estados = [0] * 8  # Vetor de estados: S0, S1, S2, S3

        # Armazena o estado inicial S0 (velocidade e altura iniciais)
        estados[0] = v_ant
        estados[1] = y_ant

        i = 1
        while(i < 4):
            # Aplica Runge-Kutta para calcular os estados S1, S2 e S3
            auxiliar1 = self.auxiliar1(v_ant)
            auxiliar2 = self.auxiliar2(v_ant)
            auxiliar3 = self.auxiliar3(v_ant)
            auxiliar4 = self.auxiliar4(v_ant)

            # Calcula a nova velocidade e altura usando Runge-Kutta
            estados[i * 2] = v_ant + (self.delta_t / 6) * (auxiliar1[0] + 2 * auxiliar2[0] + 2 * auxiliar3[0] + auxiliar4[0])
            estados[(i * 2) + 1] = y_ant + (self.delta_t / 6) * (auxiliar1[1] + 2 * auxiliar2[1] + 2 * auxiliar3[1] + auxiliar4[1])

            # Atualiza os valores para a próxima iteração
            v_ant = estados[i*2]
            y_ant = estados[(i*2)+1]
            
            i = i + 1

        return estados