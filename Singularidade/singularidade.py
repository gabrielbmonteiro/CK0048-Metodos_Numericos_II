import math
from newtoncotes import boolin  # Importa a função `boolin` do módulo `newtoncotes`, utilizada para resolver a integração numérica

# Função que retorna as fórmulas para mapeamento e derivada usando a transformação simples de variáveis
def derivada_simples():
    # Mapeia o intervalo [a, b] para o intervalo (-∞, ∞) usando a função tanh (hiperbólica)
    def xs(a, b):
        return lambda z: (a+b)/2 + (b-a) * math.tanh(z) / 2  # Transforma z usando tanh para suavizar a variação entre os limites

    # Derivada da transformação xs em relação a z
    def dxs(a, b):
        return lambda z: (b-a) / (2 * math.cosh(z) ** 2)  # Derivada de tanh(z) é 1/cosh²(z)

    return xs, dxs  # Retorna as funções xs e dxs para serem utilizadas posteriormente

# Função que retorna as fórmulas para mapeamento e derivada usando a transformação composta de variáveis
def derivada_composta():
    # Mapeia o intervalo [a, b] para o intervalo (-∞, ∞) usando uma transformação mais complexa envolvendo sinh e tanh
    def xs(a, b):
        return lambda z: (a+b)/2 + (b-a) * math.tanh(math.pi/2 * math.sinh(z)) / 2  # Mapeamento composto usando sinh e tanh

    # Derivada da transformação xs em relação a z
    def dxs(a, b):
        pi2 = math.pi / 2
        return lambda z: ((b-a)/2) * (pi2 * (math.cosh(z) / (math.cosh(pi2 * math.sinh(z)) ** 2)))  # Derivada composta de xs(z)

    return xs, dxs  # Retorna as funções xs e dxs para serem utilizadas posteriormente

# Função principal para resolver a integral, permitindo a escolha entre derivada simples e composta
def Resolver(limite, simples=True):
    # Seleciona se deve usar a transformação simples ou composta
    if simples:
        xs, dxs = derivada_simples()
    else:
        xs, dxs = derivada_composta()
    
    # Função a ser integrada, definida em termos da variável s
    def f(s):
        a = 0  # Limite inferior do intervalo [a, b]
        b = 1  # Limite superior do intervalo [a, b]
        
        # Calcula o denominador como a raiz quadrada de xs(a, b)(s)
        denominador = math.sqrt(xs(a, b)(s))

        # Condição para evitar divisão por zero
        denominador = 0.00000001 if denominador == 0 else denominador
        
        # Retorna a função a ser integrada: 1/denominador * dxs(a, b)(s)
        return (1 / denominador) * dxs(a, b)(s)
    
    # Define os limites de integração em termos do valor fornecido (limite * -1 e limite)
    a = limite * -1
    b = limite

    # Chama a função de integração numérica `boolin`, passando a função `f`, o número de pontos (2), se é infinita (False), e os limites
    return boolin(f, 2, False, limite_Inf=a, limite_Sup=b)[1]
