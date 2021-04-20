# Etiquetado de Objetos

# Algoritmo de Etiquetado de Objetos

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Nombre: 
# Expediente: 

# Fecha: 19 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen de Entrada
ime = cv2.imread('img/EtiquetadoObjetos.PNG', 2)

fifo = []

def etiquetadoImagen(ime):
    dimensionesIME = ime.shape
    r1 = dimensionesIME[0]
    c1 = dimensionesIME[1]

    k = 0
    for i in range(r1):
        for j in range(c1):
            if(ime[i][j] != 0):
                k+=1
                fifo.append((i, j))
                ime[i][j] = 0

    print(fifo)



etiquetadoImagen(ime)

plt.subplot(1, 1, 1)
plt.imshow(ime, 'gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

plt.show()