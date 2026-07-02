#Voltear una imagen en escala gris.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# 1. Cargar la imagen original con Pillow
imagen_original = Image.open('the_black_chicken.png')

# 2. Convertir a escala de grises ('L') usando Pillow
imagen_gris_pil = imagen_original.convert('L')

# 3. Convertir a Array de NumPy para poder manipularla (opcional pero pedido)
array_gris = np.array(imagen_gris_pil)

filas=len(array_gris)
columnas=len(array_gris[0])
# 4. Voltear la imagen horizontalmente (efecto espejo) usando NumPy
for i in range(filas):
    for j in range(columnas // 2):
        # Guardamos el píxel izquierdo en una variable auxiliar
        aux = array_gris[i][j]

        indice_derecho = columnas - 1 - j

        # Intercambio los valores de los píxeles
        array_gris[i][j] = array_gris[i][indice_derecho]
        array_gris[i][indice_derecho] = aux
# 5. Convertir el array de NumPy invertido de vuelta a objeto de Pillow
imagen_final = Image.fromarray(array_gris)

# 6. Guardar el archivo final
nombre_salida = 'the_black_chicken.png'
imagen_final.save(nombre_salida)

# 7. Mostrar el resultado en la celda de Colab con Matplotlib
plt.imshow(imagen_final, cmap='gray')
plt.axis('off')  # Oculta los ejes numéricos
plt.show()

# 8. Descarga automática a tu computadora
#files.download(nombre_salida)
