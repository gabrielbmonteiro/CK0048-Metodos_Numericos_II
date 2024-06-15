from funcoes import funcao_geral_integracao
import math

def gauss_Legendre_2pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Legendre com 2 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 2 pontos de Gauss-Legendre.
    """
    s = math.sqrt(1/3)
    # Raízes do polinômio de Legendre para 2 pontos
    raizes_s = [s, -s]
    # Pesos de integração associados a essas raízes
    w = 1
    pesos_w = [w, w]

    # Chama a função de integração geral com os parâmetros específicos para 2 pontos
    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)

def gauss_Legendre_3pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Legendre com 3 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 3 pontos de Gauss-Legendre.
    """
    s = math.sqrt(3/5)
    # Raízes do polinômio de Legendre para 3 pontos
    raizes_s = [s, 0, -s]
    # Pesos de integração associados a essas raízes
    w = 5/9
    w_2 = 8/9
    pesos_w = [w, w_2, w]

    # Chama a função de integração geral com os parâmetros específicos para 3 pontos
    return funcao_geral_integracao(3, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)

def gauss_Legendre_4pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Legendre com 4 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 4 pontos de Gauss-Legendre.
    """
    # Raízes do polinômio de Legendre para 4 pontos
    raizes_s = [0.861136, -0.861136, 0.339981, -0.339981]
    # Pesos de integração associados a essas raízes
    w = 0.34785
    w_3 = 0.65214 
    pesos_w = [w, w, w_3, w_3]

    # Chama a função de integração geral com os parâmetros específicos para 4 pontos
    return funcao_geral_integracao(4, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)
