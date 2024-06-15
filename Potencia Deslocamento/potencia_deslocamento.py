from potencia_inversa import Potencia_Inversa
import numpy


def Potencia_Deslocamento(matriz, vetor, epson, deslocamento):
    """
    Implementa o método da potência com deslocamento (ou deslocamento espectral) para encontrar autovalores
    e autovetores próximos a um valor de deslocamento fornecido.
    
    Parâmetros:
    - matriz: matriz quadrada para a qual queremos encontrar autovalores/autovetores.
    - vetor: vetor inicial, usado para a iteração.
    - epson: critério de convergência (erro máximo permitido entre iterações sucessivas).
    - deslocamento: valor de deslocamento aplicado ao espectro da matriz, permitindo encontrar autovalores
      próximos desse valor.
    
    Retorna:
    - autovalor: autovalor ajustado pelo método de deslocamento.
    - autovetor: autovetor associado ao autovalor.
    """

    # Subtrai o valor de deslocamento da matriz (A - μI), onde μ é o deslocamento
    novo_A = matriz - deslocamento * numpy.identity(len(matriz), dtype = int)
    
    # Aplica o método da potência inversa à matriz deslocada
    [novo_autovalor, novo_autovetor] = Potencia_Inversa(novo_A, vetor, epson)
    
    # O autovalor da matriz original é ajustado adicionando o deslocamento de volta
    autovalor = novo_autovalor + deslocamento
    autovetor = novo_autovetor

    # Retorna o autovalor corrigido e o autovetor correspondente
    return [autovalor, autovetor]