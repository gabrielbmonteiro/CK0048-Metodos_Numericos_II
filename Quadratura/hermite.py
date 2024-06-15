from funcoes import funcao_geral_integracao
import math

def gauss_Hermite_2pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Hermite com 2 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 2 pontos de Hermite.
    """
    # Raízes do polinômio de Hermite para 2 pontos
    raizes_s = [-1/math.sqrt(2), 1/math.sqrt(2)]
    # Pesos de integração associados a essas raízes
    pesos_w = [math.sqrt(math.pi)/2, math.sqrt(math.pi)/2]

    # Chama a função de integração geral com os parâmetros específicos para 2 pontos
    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Hermite_3pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Hermite com 3 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 3 pontos de Hermite.
    """
    # Raízes do polinômio de Hermite para 3 pontos
    raizes_s = [-math.sqrt(3/2), 0, math.sqrt(3/2)]
    # Pesos de integração associados a essas raízes
    pesos_w = [math.sqrt(math.pi)/6, 2*math.sqrt(math.pi)/3, math.sqrt(math.pi)/6]

    # Chama a função de integração geral com os parâmetros específicos para 3 pontos
    return funcao_geral_integracao(3, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Hermite_4pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Hermite com 4 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 4 pontos de Hermite.
    """
    # Raízes do polinômio de Hermite para 4 pontos
    raizes_s = [-1.651, -0.525, 0.525, 1.1651]
    # Pesos de integração associados a essas raízes
    pesos_w = [0.0813128354472452, 0.8049140900055128, 0.8049140900055128, 0.0813128354472452]

    # Chama a função de integração geral com os parâmetros específicos para 4 pontos
    return funcao_geral_integracao(4, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)
