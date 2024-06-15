# Função para calcular os pontos de integração e o valor de h para a regra de integração fechada (inclui limites)
def h_fechado(limite_inferior, limite_superior, grau_polinomio):
    h = (limite_superior - limite_inferior) / grau_polinomio  # Calcula o tamanho do intervalo entre os pontos
    pontos = []
    # Gera os pontos de integração distribuídos uniformemente entre os limites inferior e superior
    for i in range(grau_polinomio + 1):
        pontos.append(limite_inferior + h * i)
    return (h, pontos)

# Função para calcular os pontos de integração e o valor de h para a regra de integração aberta (não inclui limites)
def h_aberto(limite_inferior, limite_superior, grau_polinomio):
    h = (limite_superior - limite_inferior) / (grau_polinomio + 2)  # Ajusta h considerando que não inclui os limites
    pontos = []
    # Gera os pontos de integração deslocados para dentro do intervalo
    for i in range(grau_polinomio + 1):
        pontos.append(limite_inferior + h * (i + 1))
    return (h, pontos)

# Função que aproxima a integral de uma função dada, utilizando regras de integração de Newton-Cotes
def aproximador(funcao, a, b, n_divisoes, grau, fechado):
    # Verifica se é uma regra de integração fechada
    if fechado:
        # Define pesos e parâmetros para diferentes graus de polinômios na regra fechada
        if grau == 1:
            pesos = [1, 1]
            divisor = 2
            multiplicador = 1
        if grau == 2:
            pesos = [1, 4, 1]
            divisor = 3
            multiplicador = 1
        if grau == 3:
            pesos = [1, 3, 3, 1]
            divisor = 8
            multiplicador = 3
        if grau == 4:
            pesos = [14, 64, 24, 64, 14]
            divisor = 45
            multiplicador = 1
        calcularPontos = h_fechado  # Usa a função de cálculo de pontos para regra fechada
    else:
        # Define pesos e parâmetros para diferentes graus de polinômios na regra aberta
        if grau == 1:
            pesos = [1, 1]
            multiplicador = 3
            divisor = 2
        if grau == 2:
            pesos = [2, -1, 2]
            multiplicador = 4
            divisor = 3
        if grau == 3:
            pesos = [11, 1, 1, 11]
            multiplicador = 5
            divisor = 24
        if grau == 4:
            pesos = [33, -42, 78, -42, 33]
            multiplicador = 1
            divisor = 10
        calcularPontos = h_aberto  # Usa a função de cálculo de pontos para regra aberta

    soma_total = 0
    quantidade_divisoes = (2 ** n_divisoes)  # Número de divisões da integral para o método de refinamento
    Dx = (b - a) / quantidade_divisoes  # Tamanho de cada subdivisão
    
    # Itera sobre as subdivisões da integral
    for i in range(quantidade_divisoes):
        xi = a + i * Dx  # Limite inferior da subdivisão atual
        xf = xi + Dx     # Limite superior da subdivisão atual
        h, pontos = calcularPontos(xi, xf, grau)  # Calcula os pontos de integração
        
        soma_parcial = 0
        # Aplica a soma ponderada dos valores da função nos pontos de integração
        for j in range(len(pesos)):
            soma_parcial += pesos[j] * funcao(pontos[j])
            
        # Acumula o valor ponderado da integral para essa subdivisão
        soma_total += soma_parcial * ((h * multiplicador) / divisor)
    
    return soma_total  # Retorna a aproximação total da integral

# Função que realiza a integração de uma função com base no método de Newton-Cotes (com limites fechados ou abertos)
def boolin(funcao, grau, fechado, limite_Inf=0, limite_Sup=1):
    erro = 10**(-6)  # Define o critério de erro para a convergência

    # Calcula a primeira aproximação da integral com 0 subdivisões
    valor_anterior = aproximador(funcao, limite_Inf, limite_Sup, 0, grau, fechado)
    
    # Calcula a aproximação da integral com 1 subdivisão
    valor_atual = aproximador(funcao, limite_Inf, limite_Sup, 1, grau, fechado)
    
    iteracoes = 1  # Contador de iterações
    # Itera até que a diferença entre a aproximação anterior e atual seja menor que o erro permitido
    while abs(valor_anterior - valor_atual) > erro:
        if iteracoes == 10:  # Limita o número de iterações a 10 para evitar loops infinitos
            break
        iteracoes += 1
        valor_anterior = valor_atual  # Atualiza o valor anterior
        valor_atual = aproximador(funcao, limite_Inf, limite_Sup, iteracoes, grau, fechado)  # Calcula a nova aproximação
    
    return (iteracoes, valor_atual)  # Retorna o número de iterações e o valor aproximado da integral