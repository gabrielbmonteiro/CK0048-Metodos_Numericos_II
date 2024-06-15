import numpy as np
from PIL import Image

def apply_filter(image, filter):

  #Aplica um filtro 3x3 a uma imagem utilizando convolução 2D.
  width, height = image.shape

  # Cria uma imagem com borda de zeros para evitar problemas na borda da imagem original.
  image_pad = np.pad(image, 1, mode='constant', constant_values=0)
  output = np.zeros(image.shape)

  for i in range(width):
    for j in range(height):
      # Extrai a região 3x3 da imagem com padding
      mask = np.array([
        [image_pad[i][j], image_pad[i][j+1], image_pad[i][j+2]],
        [image_pad[i+1][j], image_pad[i+1][j+1], image_pad[i+1][j+2]],
        [image_pad[i+2][j], image_pad[i+2][j+1], image_pad[i+2][j+2]]
      ])
      # Calcula o valor do pixel resultante
      output[i, j] = np.sum(filter * mask)

  return output

# Definição dos filtros
gaussian = (1.0 / 16.0) * np.array([
    [1.0, 2.0, 1.0],
    [2.0, 4.0, 2.0],
    [1.0, 2.0, 1.0]
])

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

laplacian = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

# Carregamento da imagem
image_path = 'imagem.jpg'
input_img = np.array(Image.open(image_path).convert('L')) / 255.0  # Normaliza a imagem para o intervalo [0, 1]

# Aplica o filtro gaussiano à imagem
blurred_img = apply_filter(input_img, gaussian)

# Algoritmo 1: Detecção de bordas usando Sobel
threshold = 0.17
A = apply_filter(blurred_img, sobel_x)
B = apply_filter(blurred_img, sobel_y)
C = np.sqrt(A**2 + B**2)
D = np.where(C < threshold, 0, 1)
output_img_alg1 = Image.fromarray((D * 255).astype(np.uint8), mode='L')
output_img_alg1.save('alg1.png')
print("Resultado Alg1 pronto")

# Algoritmo 2: Detecção de bordas usando Laplaciano
tolerance = 0.0295
laplacian_result = apply_filter(blurred_img, laplacian)
edge_detected_img = np.where(np.abs(laplacian_result) > tolerance, 1, 0)
output_img_alg2 = Image.fromarray((edge_detected_img * 255).astype(np.uint8), mode='L')
output_img_alg2.save('alg2.png')
print("Resultado Alg2 pronto")