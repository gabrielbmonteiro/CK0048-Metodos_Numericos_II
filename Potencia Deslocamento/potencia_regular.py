from math import sqrt
   
def Potencia_Regular(matriz, vetor, epson): # step 1
    """
    Função que implementa o método da potência regular para encontrar o maior autovalor
    e o autovetor associado de uma matriz.
    
    Parâmetros:
    - matriz: matriz quadrada cujos autovalores/autovetores queremos encontrar.
    - vetor: vetor inicial que será iterativamente ajustado para encontrar o autovetor dominante.
    - epson: critério de convergência (erro máximo permitido entre iterações sucessivas).
    
    Retorna:
    - lambda1_novo: autovalor dominante da matriz.
    - x1_velho: autovetor dominante associado ao autovalor.
    """

    tam = len(vetor) # Tamanho da matriz (assume-se que a matriz seja quadrada)
    vk_novo = [] # Vetor da iteração atual
    vk_velho = [] # Vetor da iteração anterior
    erro = 10  # Inicia com um valor arbitrariamente grande para começar o loop
    lambda1_novo = 0   # step 2 - Inicializa o autovalor dominante como zero
    
    # step 3 - Inicializa os vetores vk_novo com o vetor inicial e vk_velho com zeros
    for i in range(tam):
        vk_novo.append(vetor[i])
        vk_velho.append(0)

    # Itera até que o erro seja menor que o valor de tolerância (epson)
    while(erro > epson):
        lambda1_velho = lambda1_novo # step 4 - Armazena o autovalor anterior
        vk_velho = vk_novo # step 5 - Armazena o vetor da iteração anterior
        x1_velho = normalizacao(vk_velho, tam) # step 6 - Normaliza o vetor anterior
        vk_novo = matriz_x_vetor(x1_velho, matriz) # step 7 - Multiplica a matriz pelo vetor normalizado
        lambda1_novo = vetor_x_vetor(x1_velho, vk_novo, tam) # step 8 - Calcula o novo autovalor como produto escalar
        erro = abs((lambda1_novo-lambda1_velho)/lambda1_novo) # step 9 - Calcula o erro relativo entre as iterações

    # Retorna o autovalor dominante e o autovetor associado
    return [lambda1_novo, x1_velho]

def normalizacao(v, tam):
    """
    Função para normalizar um vetor. A normalização é feita dividindo cada componente do vetor
    pela sua norma (comprimento).
    
    Parâmetros:
    - v: vetor a ser normalizado.
    - tam: tamanho do vetor.
    
    Retorna:
    - Vetor normalizado.
    """

    aux = []
    s = sqrt(vetor_x_vetor(v, v, tam)) # Norma do vetor: sqrt(soma dos quadrados dos componentes)
    for i in range(tam):
        aux.append(v[i]/s) # Divide cada componente pela norma
    return aux # Retorna o vetor normalizado

def matriz_x_vetor(v, matriz):
    """
    Função que multiplica uma matriz por um vetor.
    
    Parâmetros:
    - v: vetor a ser multiplicado pela matriz.
    - matriz: matriz com a qual o vetor será multiplicado.
    
    Retorna:
    - O resultado da multiplicação da matriz pelo vetor.
    """

    x = []
    tam = len(matriz) # Tamanho da matriz (assume-se quadrada)
  
    for i in range(tam):
        s = vetor_x_vetor(matriz[i], v, tam) # Multiplica a i-ésima linha da matriz pelo vetor
        x.append(s) # Adiciona o resultado ao vetor resultante
    return x # Retorna o vetor resultante da multiplicação

def vetor_x_vetor(v1, v2, tam):
    """
    Função que calcula o produto escalar de dois vetores.
    
    Parâmetros:
    - v1: primeiro vetor.
    - v2: segundo vetor.
    - tam: tamanho dos vetores.
    
    Retorna:
    - O produto escalar de v1 e v2.
    """

    s = 0
    for i in range(tam):
        s = s + v1[i]*v2[i] # Soma o produto dos componentes correspondentes
    return s # Retorna o valor do produto escalar