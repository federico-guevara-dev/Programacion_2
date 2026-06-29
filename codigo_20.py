#Importar en Py una img y almacenarla en una matriz. Implementar(crear) una función para rotar la imagen. Preguntar al usuario si quiere rotar a 90 grados a la izquierda o a la derecha o 180 grados. Mostrar la imagen original y rotarla
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def rotar_img(ruta_imagen):
    imagen_original = Image.open(ruta_imagen).convert("L")
    arr = np.array(imagen_original)
    alto, ancho = arr.shape

    print("1. 90° Derecha\n2. 90° Izquierda\n3. 180°")
    opcion = input("Seleccione rotación: ")

    def transponer(m):
        h, w = m.shape
        res = []
        for i in range(w):
            n_row = []
            for j in range(h):
                n_row.append(m[j][i])
            res.append(n_row)
        return np.array(res)

    def voltear_h(m):
        res = m.copy()
        for i in range(len(res)):
            for j in range(len(res[i]) // 2):
                aux = res[i][j]
                idx_f = len(res[i]) - 1 - j
                res[i][j] = res[i][idx_f]
                res[i][idx_f] = aux
        return res

    def voltear_v(m):
        res = m.copy()
        for i in range(len(res) // 2):
            aux = res[i].copy()
            res[i] = res[len(res)-1-i]
            res[len(res)-1-i] = auxvc
        return res

    if opcion == '1': # 90 Der: Transponer + Voltear H
        resultado = voltear_h(transponer(arr))
    elif opcion == '2': # 90 Izq: Transponer + Voltear V
        resultado = voltear_v(transponer(arr))
    elif opcion == '3': # 180: Voltear H + Voltear V
        resultado = voltear_v(voltear_h(arr))
    else:
        resultado = arr

    fig, ejes = plt.subplots(1, 2, figsize=(12, 6))
    ejes[0].imshow(arr, cmap='gray')
    ejes[0].set_title("Original")
    ejes[1].imshow(resultado, cmap='gray')
    ejes[1].set_title("Resultado")
    plt.show()

rotar_img("pollo_quispe.jpg")
