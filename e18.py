# Aplicar un filtro de desenfoque Gaussiano a una imagen. Mostrar la imagen original y la filtrada . Hacer la convolución manual desde la celda(1,1) hasta la (n-1, n-1). Usar el kernel.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pollo_pelado.jpg', cv2.IMREAD_GRAYSCALE)
if img is None: raise FileNotFoundError


# 2. Definir el Kernel Gaussiano de 3x3 estándar y normalizarlo (suma de elementos = 1)
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32)
kernel /= 16.0  # Se divide entre 16 porque 1+2+1+2+4+2+1+2+1 = 16

# 3. Crear matriz de salida del mismo tamaño (preservamos los bordes originales)
alto, ancho = img.shape
img_filtrada = img.copy().astype(np.float32)

# 4. Convolución manual desde (1,1) hasta (n-1, n-1)
# En Python (indexación base 0), el rango va desde 1 hasta alto-1 y ancho-1
for i in range(1, alto - 1):
    for j in range(1, ancho - 1):
        # Extraer la submatriz (vecindario de 3x3) centrada en el píxel (i, j)
        sub_matriz = img[i-1 : i+2, j-1 : j+2].astype(np.float32)

        # Multiplicar elemento a elemento y sumar todos los valores resultantes
        valor_convolucionado = np.sum(sub_matriz * kernel)

        # Asignar el nuevo valor a la imagen de salida
        img_filtrada[i, j] = valor_convolucionado

# Convertir la imagen filtrada de vuelta a formato de 8 bits (0-255)
img_filtrada = np.clip(img_filtrada, 0, 255).astype(np.uint8)

# 5. Mostrar la imagen original y la filtrada
plt.figure(figsize=(10, 5))

# Imagen Original
plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

# Imagen Filtrada (Desenfoque Gaussiano)
plt.subplot(1, 2, 2)
plt.title("Imagen con Desenfoque Gaussiano")
plt.imshow(img_filtrada, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
