from funcoes import funcao_geral_integracao
import math

def gauss_Chebyshev_2pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Chebyshev com 2 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 2 pontos de Chebyshev.
    """

    # Raízes do polinômio de Chebyshev de 1ª espécie para 2 pontos
    raizes_s = [-1/math.sqrt(2), 1/math.sqrt(2)]
    # Pesos de integração associados a essas raízes
    pesos_w = [math.pi/2, math.pi/2]

    # Chama a função de integração geral com os parâmetros específicos para 2 pontos
    return funcao_geral_integracao(2, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Chebyshev_3pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Chebyshev com 3 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 3 pontos de Chebyshev.
    """
    # Raízes do polinômio de Chebyshev de 1ª espécie para 3 pontos
    raizes_s = [-math.sqrt(3)/2, 0, math.sqrt(3)/2]
    # Pesos de integração associados a essas raízes
    pesos_w = [math.pi/3, math.pi/3, math.pi/3]

    # Chama a função de integração geral com os parâmetros específicos para 3 pontos
    return funcao_geral_integracao(3, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)


def gauss_Chebyshev_4pontos(a_inicio, b_fim, erro_estimado):
    """
    Realiza a integração numérica usando o método de Gauss-Chebyshev com 4 pontos.

    Parâmetros:
    - a_inicio: O início do intervalo de integração.
    - b_fim: O fim do intervalo de integração.
    - erro_estimado: A tolerância para o erro na integração.

    Retorna:
    - O resultado da integração utilizando 4 pontos de Chebyshev.
    """
    # Raízes do polinômio de Chebyshev de 1ª espécie para 4 pontos
    raizes_s = [-0.92387953251, -0.38268343236, 0.38268343236, 0.92387953251]
    # Pesos de integração associados a essas raízes
    pesos_w = [math.pi/4, math.pi/4, math.pi/4, math.pi/4]

    # Chama a função de integração geral com os parâmetros específicos para 4 pontos
    return funcao_geral_integracao(4, pesos_w, raizes_s, erro_estimado, a_inicio, b_fim)