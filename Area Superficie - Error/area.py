from math import sqrt, pi
import numpy as np

class AreaDeSuperficie:
    
    def funcao(self, x, y):                     # Função que define a superfície do problema
        z_x = 0.4 * x
        z_y = -0.4 * y
        result = sqrt(1 + z_x**2 + z_y**2)
        return result

    def gauss_legendre(self, region):                   # Quadratura de 3 pontos para o cálculo da área da superfície
        a = [-sqrt(3/5), 0, sqrt(3/5)]          # Vetor com os parâmetros para funcao(self, a, b)
        w = [5/9, 8/9, 5/9]                     # Vetor com os pesos
        
        # Limites de integração
        x_limits, y_limits = region
        
        # Transformação para o intervalo [-1, 1] dos limites reais
        def transform(t, a, b):
            return 0.5 * ((b - a) * t + (b + a))
        
        soma = 0
        for i in range(3):
            for j in range(3):
                x = transform(a[i], x_limits[0], x_limits[1])
                y = transform(a[j], y_limits[0], y_limits[1])
                soma += w[i] * w[j] * self.funcao(x, y)
        
        # Ajuste final com o tamanho dos intervalos de integração
        resultado = 0.25 * (x_limits[1] - x_limits[0]) * (y_limits[1] - y_limits[0]) * soma
        return resultado

# Definição das regiões
regiao1 = ((-40, 40), (-20, 20))
regiao2 = ((-40, 40), (-20, 20)) # Usar os limites corretos após transformar a elipse para coordenadas

# Cálculo da área para cada região
area_superficie = AreaDeSuperficie()
#area1 = area_superficie.gauss_legendre(regiao1)
# Para a segunda região, seria necessário ajustar a transformação para coordenadas elípticas
area2 = area_superficie.gauss_legendre(regiao2)

#print(f"Área da superfície para a região 1: {area1} m²")
print(f"Área da superfície para a região 2: {area2} m²")
