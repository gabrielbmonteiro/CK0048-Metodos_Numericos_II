from forward import f_forward
from backward import f_backward
from central import f_central
import math

def derivada(f, x, delta, filosofia, ordem =1):
    """
    Calcula a derivada de uma função `f` no ponto `x` usando o método especificado pela filosofia
    (forward, backward, ou central).
    
    Parâmetros:
    - f: função a ser diferenciada
    - x: ponto onde a derivada será avaliada
    - delta: espaçamento entre os pontos
    - filosofia: string que indica o método de diferenciação ('forward', 'backward' ou 'central')
    - ordem: ordem da derivada (1 por padrão)
    
    Retorna:
    - Aproximação da derivada de `f` em `x` usando o método escolhido.
    """

    if filosofia[0] == 'f':  # Se for forward (progressiva)
        return f_forward(f, x, delta, ordem)
    if filosofia[0] == 'b':  # Se for backward (regressiva)
        return f_backward(f, x, delta, ordem)
    if filosofia[0] == 'c':  # Se for central
        return f_central(f, x, delta, ordem)
    
def polinomio(x):
    """
    Avalia um polinômio em um ponto `x` dado os coeficientes do polinômio.
    
    Parâmetros:
    - x: ponto onde o polinômio será avaliado
    - poli: lista de coeficientes do polinômio (do termo de maior grau ao de menor grau)
    
    Retorna:
    - Valor do polinômio no ponto `x`.
    """
    y = math.exp(-4) * math.cos(x)
    '''
    y = 0
    a  = len(poli)-1 # Grau do polinômio (é a posição do maior coeficiente)
    for i in range(0,len(poli)): # Itera pelos coeficientes do polinômio
        y+= poli[i]*pow(x,a) # Calcula o termo poli[i] * x^a
        a -= 1  # Decrementa o expoente
    '''
    return y


def gerarpolinomio(grau):
    """
    Gera uma lista de coeficientes de um polinômio de um dado grau com base na entrada do usuário.
    
    Parâmetros:
    - grau: grau do polinômio que o usuário deseja criar
    
    Retorna:
    - Lista de coeficientes do polinômio.
    """

    poli = []
    flag = True
    flag2 = False
    while flag:
        # Solicita ao usuário os coeficientes separados por vírgulas
        lista = input("Insira os coeficientes, separados por vírgulas(,) >> " )      
        cont = lista.count(',')

        # Verifica se o número de coeficientes está correto
        if (cont != (grau)):
            print("Entrada inválida, por favor confira os valores e digite novamente")
        else:
            # Verifica se a entrada contém apenas números e vírgulas
            for i in lista:
                if ((ord(i)>75)or(ord(i)<48)):
                    if (i != ','):
                        flag2 = True
                        print("Entrada inválida, por favor confira os valores e digite novamente")
                        i = lista[len(lista)-1]

            if flag2 == False:
                flag = False
   
    # Converte a string de entrada em uma lista de inteiros
    lista = lista.split(',')
    for i in lista:
        if(i != ','):
            poli.append(int(i)) 
    return  poli

def gerarfuncao(poli):
    """
    Gera uma função lambda que representa um polinômio dado seus coeficientes.
    
    Parâmetros:
    - poli: lista de coeficientes do polinômio
    
    Retorna:
    - Função lambda que calcula o valor do polinômio para um dado `x`.
    """

    return lambda x : polinomio(x)