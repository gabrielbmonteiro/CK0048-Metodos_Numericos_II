import math

# Função a ser integrada
def F(x):
    """
    Função F(x) que será usada nas fórmulas de integração.
    É uma função específica que retorna o quadrado de (sen(2x) + 4x^2 + 3x).
    """

    return math.exp(6) * math.cos(x)

# Função geral para realizar a integração numérica
def funcao_geral_integracao(a, b, epson, tipo):
    """
    Realiza a integração numérica da função F(x) no intervalo [a, b] com controle de erro.
    Utiliza diferentes métodos de integração numérica com subdivisão do intervalo.

    Parâmetros:
    - a: limite inferior de integração
    - b: limite superior de integração
    - epson: tolerância de erro para o critério de parada
    - tipo: tipo de fórmula de Newton-Cotes a ser usada (fechada ou aberta, de 1ª a 4ª ordem)

    Retorna:
    - iter: número de iterações necessárias até a convergência
    - result: valor aproximado da integral
    """

    delta  = 0       # Espaçamento entre pontos de integração
    Xi     = 0       # Ponto inicial do subintervalo
    err    = 0       # Erro de integração
    result = 0       # Resultado atual da integral
    iter   = 0       # Número de iterações
    N      = 2       # Número inicial de subdivisões do intervalo
    before_result = 0 # Resultado anterior da integral

    while True:
        iter += 1
        delta = (b-a)/N # Calcula o espaçamento entre os pontos de integração
        integral = 0
        # Loop para aplicar a fórmula de integração em cada subdivisão do intervalo
        for i in range(N): 
            Xi = a + i*delta # Início do subintervalo
            Xf = Xi + delta # Final do subintervalo
            # Verifica o tipo de método de integração e aplica a fórmula correspondente
            if(tipo=="fechada1"):
                integral += fechada1(Xi, Xf)
            elif(tipo=="fechada2"):
                integral += fechada2(Xi, Xf)
            elif(tipo=="fechada3"):
                integral += fechada3(Xi, Xf)
            elif(tipo=="fechada4"):
                integral += fechada4(Xi, Xf)
            elif(tipo=="aberta1"):
                integral += aberta1(Xi, Xf)
            elif(tipo=="aberta2"):
                integral += aberta2(Xi, Xf)
            elif(tipo=="aberta3"):
                integral += aberta3(Xi, Xf)
            elif(tipo=="aberta4"):
                integral += aberta4(Xi, Xf)

        N = N * 2 # Dobra o número de subdivisões a cada iteração para refinar a integral
        before_result = result # Armazena o resultado anterior
        result = integral # Atualiza o resultado da integral
        err = abs((result-before_result)/result) # Calcula o erro relativo entre as iterações
        
         # Se o erro for menor que o valor de epson, a integração converge e o loop é interrompido
        if (err < epson): 
            break
    
    return iter, result

# Fórmulas de Newton-Cotes fechadas
def fechada1(Xi, Xf): # Método do Trapézio (N = 1)
    return (Xf-Xi)/2*(F(Xi)+F(Xf))
    
def fechada2(Xi, Xf): # Regra de Simpson (N = 2)
    h = (Xf-Xi)/2
    return (h)/3*(F(Xi) + 4*F(Xi+h) + F(Xi+2*h))

def fechada3(Xi, Xf): # Regra de Simpson 3/8 (N = 3)
    h = (Xf-Xi)/3
    return (3*(h)/8)*(F(Xi) + 3*F(Xi+h) + 3*F(Xi+2*h) +F(Xi+3*h))

def fechada4(Xi, Xf): # Fórmula fechada de 4ª ordem (N = 4)
    h = (Xf-Xi)/4
    return (2*(h)/45)*(7*F(Xi) + 32*F(Xi+h) + 12*F(Xi+2*h) +32*F(Xi+3*h)+7*F(Xi+4*h))
        
# Fórmulas de Newton-Cotes abertas
def aberta1(Xi, Xf): # Fórmula aberta de 1ª ordem (N = 1)
    h = (Xf-Xi)/3
    return (Xf-Xi)/2*(F(Xi+h)+F(Xi+2*h))

def aberta2(Xi, Xf): # Fórmula aberta de 2ª ordem (N = 2)
    h = (Xf-Xi)/4
    return ((4*h)/3)*(2*F(Xi+h) - F(Xi+2*h) + 2*F(Xi+3*h))   

def aberta3(Xi, Xf): # Fórmula aberta de 3ª ordem (N = 3)
    h = (Xf-Xi)/5
    return ((5*(Xf-Xi)/5)/24)*(11*F(Xi+h) + F(Xi+2*h) + F(Xi+3*h) + 11*F(Xi+4*h))

def aberta4(Xi, Xf): # Fórmula aberta de 4ª ordem (N = 4)
    h = (Xf-Xi)/6
    return ((6*h)/20)*(11*F(Xi+h) - 14*F(Xi+2*h) + 26*F(Xi+3*h) - 14*F(Xi+4*h)+ 11*F(Xi+5*h))