import math

def f(x):
    """
    Define a função a ser integrada.
    
    Parâmetros:
    - x: O valor de entrada para a função.
    
    Retorna:
    - O valor da função f(x) = (sin(2*x) + 4*x^2 + 3*x)^2.
    """

    return math.exp(6) * math.cos(x)

def x(sk, xi, xf):
    """
    Calcula o valor de x para um ponto específico sk dentro do intervalo [xi, xf].
    
    Parâmetros:
    - sk: O ponto específico no intervalo.
    - xi: O início do intervalo.
    - xf: O fim do intervalo.
    
    Retorna:
    - O valor de x correspondente ao ponto sk.
    """
     
    x_final = (xi + xf) / 2 + ((xf - xi) / 2) * sk
    return x_final

def funcao_geral_integracao(qtd_pontosInterpolacao, pesos_w, raizes_s, epsilon, a, b):
    """
    Realiza a integração numérica utilizando o método de Gauss por partição adaptativo.
    
    Parâmetros:
    - qtd_pontosInterpolacao: O número de pontos de interpolação a serem usados.
    - pesos_w: Os pesos de integração associados aos pontos de interpolação.
    - raizes_s: Os pontos de interpolação dentro do intervalo [-1, 1].
    - epsilon: A tolerância de erro para a convergência.
    - a: O início do intervalo de integração.
    - b: O fim do intervalo de integração.
    
    Retorna:
    - interacoes: O número de iterações realizadas.
    - resultado: O valor estimado da integral.
    """
    
    # Inicializa as variáveis
    delta = 0
    xi = 0
    xf = 0
    erro = 0 # Erro inicial para comparação com a tolerância epsilon
    resultadoAnterior = 0
    resultado = 0
    resultado_aux = 0 # Variável auxiliar para armazenar o resultado anterior
    N = 1 # Número inicial de partições

    while True:
        resultadoAnterior = resultado
        resultado_aux = resultado
        resultado = 0
        interacoes = 0
        
        delta = (b - a) / N # Calcula o tamanho de cada partição
        for i in range(N): # Realiza a integração sobre N partições
            xi = a + i*delta
            xf = xi + delta
            somatorio = 0
            for k in range(qtd_pontosInterpolacao):
                # Calcula o somatório usando os pesos e as raízes de interpolação
                somatorio += (pesos_w[k] * f(x(raizes_s[k], xi, xf)))
           
            # Atualiza o resultado da integração para esta partição
            resultado  += ((xf - xi) / 2) * somatorio 
            interacoes += 1
          
        N = N * 2 # Duplica o número de partições para a próxima iteração
        resultadoAnterior = resultado_aux
      
        erro = abs((resultadoAnterior - resultado)/ resultado) # Calcula o erro relativo

        # Verifica se o erro é menor que a tolerância
        if (erro < epsilon): 
            break

    print("\nPARTIÇÕES:", N)  # Imprime o número de partições finais usadas
    return interacoes, resultado  # Retorna o número de iterações e o resultado da integral

