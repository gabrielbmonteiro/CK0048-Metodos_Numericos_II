def f_backward(f, x, delta, ordem):
    """
    Calcula a derivada de uma função `f` no ponto `x` usando o método de diferenças finitas regressivas
    (backward difference), até a ordem especificada (1ª a 4ª ordem).

    Parâmetros:
    - f: função a ser diferenciada
    - x: ponto onde a derivada será avaliada
    - delta: espaçamento (diferença pequena) entre os pontos
    - ordem: ordem da derivada (1, 2, 3 ou 4)

    Retorna:
    - Aproximação da derivada de `f` no ponto `x` de acordo com a ordem escolhida.
    
    Exceção:
    - Levanta um ValueError se a ordem não for entre 1 e 4.
    """
    
    if ordem == 1:
        # Calcula a derivada de 1ª ordem usando a fórmula de diferença regressiva
        return f_backward1(f, x, delta)
    elif ordem == 2:
        # Calcula a derivada de 2ª ordem usando a fórmula de diferença regressiva
        return f_backward2(f, x, delta)
    elif ordem == 3:
        # Calcula a derivada de 3ª ordem usando a fórmula de diferença regressiva
        return f_backward3(f, x, delta)
    elif ordem == 4:
        # Calcula a derivada de 4ª ordem usando a fórmula de diferença regressiva
        return f_backward4(f, x, delta)
    else:
        # Levanta um erro se a ordem não for suportada
        raise ValueError("Ordem não suportada. Apenas ordens 1 a 4 são suportadas.")

def f_backward1(f, x, delta):
    # Derivada de 1ª ordem usando diferença regressiva.
    return (f(x) - f(x - delta)) / delta

def f_backward2(f, x, delta):
    # Derivada de 2ª ordem usando diferença regressiva.
    return (f(x) - 2 * f(x - delta) + f(x - 2 * delta)) / (delta * delta)

def f_backward3(f, x, delta):
    # Derivada de 3ª ordem usando diferença regressiva.
    return (f(x) - 3 * f(x - delta) + 3 * f(x - 2 * delta) - f(x - 3 * delta)) / (delta ** 3)

def f_backward4(f, x, delta):
    # Derivada de 4ª ordem usando diferença regressiva.
    return (f(x) - 4 * f(x - delta) + 6 * f(x - 2 * delta) - 4 * f(x - 3 * delta) + f(x - 4 * delta)) / (delta ** 4)
