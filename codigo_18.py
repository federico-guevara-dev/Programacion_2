#Importar en PY una imagen a color y mostrarla. Definir una función para convertir imagenes a escala de grises u mostrar el resultado. No usar funciones integradas, en su lugar usar la fórmula.
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def convertir_a_grises_con_for(ruta_imagen):
    # 1. Abro la foto
    imagen_color = Image.open(ruta_imagen)
    array_color = np.array(imagen_color)# Hace que el array sea compatible con shape

    # Saco el tamaño de la foto: cuántos píxeles de alto y de ancho tiene
    alto = array_color.shape[0]
    ancho = array_color.shape[1]

    # Creo un lienzo vacío (en negro) del mismo tamaño para dibujar la foto gris
    array_grises = np.zeros((alto, ancho))

    # El for recorre la imagen de arriba a abajo (fila por fila)
    # y el de adentro recorre de izquierda a derecha (columna por columna).
    for i in range(alto):
        for j in range(ancho):

            # Sacamos el color del píxel exacto en esa posición
            R = array_color[i, j, 0] # Cuánto rojo tiene
            G = array_color[i, j, 1] # Cuánto verde tiene
            B = array_color[i, j, 2] # Cuánto azul tiene

            # No podemos sumar los colores y dividirlos por 3 porque nuestros ojos
            # son muy sensibles al verde y poco al azul. Usamos estos números:
            gris = (R * 0.2989) + (G * 0.5870) + (B * 0.1140)

            # Guardamos ese nuevo valor gris en nuestro lienzo vacío
            array_grises[i, j] = gris

    # 2. --- MOSTRAR EL RESULTADO EN PANTALLA ---
    fig, ejes = plt.subplots(1, 2, figsize=(10, 5))

    # Imagen original
    ejes[0].imshow(array_color)
    ejes[0].set_title("Original (Color)")
    ejes[0].axis('off')

    # Nueva imagen en gris
    ejes[1].imshow(array_grises, cmap='gray')
    ejes[1].set_title("Gris")
    ejes[1].axis('off')

    plt.tight_layout()
    plt.show()

# Ejecución de la conversión pollo rapado:
convertir_a_grises_con_for('pollo_rapado.jpg')
