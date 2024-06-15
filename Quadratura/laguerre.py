from funcoes import funcao_geral_integracao
import math

def gauss_Laguerre_2pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Laguerre com 2 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 2 pontos de Laguerre.
    """
    # Raízes do polinômio de Laguerre para 2 pontos
    raizes_s = [2 - math.sqrt(2), 2 + math.sqrt(2)]
    # Pesos de integração associados a essas raízes
    pesos_w = [(1/4)*(2 + math.sqrt(2)), (1/4)*(2 - math.sqrt(2))]

    # Chama a função de integração geral com os parâmetros específicos para 2 pontos
    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Laguerre_3pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Laguerre com 3 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 3 pontos de Laguerre.
    """
    # Raízes do polinômio de Laguerre para 3 pontos
    raizes_s = [0.4157745568, 2.2942803603, 6.2899450829]
    # Pesos de integração associados a essas raízes
    pesos_w = [0.7110930099, 0.2785177336, 0.0103892565]

    # Chama a função de integração geral com os parâmetros específicos para 3 pontos
    return funcao_geral_integracao(3, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Laguerre_4pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Laguerre com 4 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 4 pontos de Laguerre.
    """
    # Raízes do polinômio de Laguerre para 4 pontos
    raizes_s = [0.323, 1.746, 4.537, 9.395]                                             
    # Pesos de integração associados a essas raízes
    pesos_w = [0.59562, 0.35697, 0.03885, 0.00053]

    # Chama a função de integração geral com os parâmetros específicos para 4 pontos
    return funcao_geral_integracao(4, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)
