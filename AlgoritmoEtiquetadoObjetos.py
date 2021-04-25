# Etiquetado de Objetos

# Algoritmo de Etiquetado de Objetos

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Nombre: Roberto Sánchez Olguín
# Expediente: 268247 

# Fecha de entrega: 26 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen Original
imagenOriginal = cv2.imread('img/EtiquetadoObjetos.PNG', 2)
# Imagen de Entrada 
ime = cv2.imread('img/EtiquetadoObjetos.PNG', 2)
# Imagen de Salida
ims = np.zeros(ime.shape, np.uint8)

# Se inicializa lista FIFO 
fifo = []

# Función de Etiquetado de Imagen 
def etiquetadoImagen(ime, ims):
    # Se obtienen las dimensiones de la imagen de entrada 
    dimensionesIME = ime.shape
    r1 = dimensionesIME[0]
    c1 = dimensionesIME[1]

    # Inicializa etiquetado 
    k = 0
    # Detecta componente
    for i in range(r1):
        for j in range(c1):
            if(ime[i][j] != 0):
                # Incrementa valor de la etiqueta 
                k+=1
                # Inicializa FIFO 
                fifo.append((i, j))
                # Borra pixel de Imagen de Entrada 
                ime[i][j] = 0
                # Enciende pixel de Imagen de Salida 
                ims[i][j] = k
                # Mientras FIFO no está vacía, se obtiene la última coordenada y se revisa la vecindad de ese pixel.
                while(len(fifo)>0):                  
                    coordenada = fifo.pop(0)  
                    m = coordenada[0]
                    n = coordenada[1]

                    # Revisa la vecindad del pixel 
                    if ((ime[m-1, n-1]) != 0):                                   
                        fifo.append([m-1, n-1])
                        ime[m-1, n-1] = 0
                        ims[m-1, n-1] = k

                    if ((ime[m-1, n+1]) != 0):                                   
                        fifo.append([m-1, n+1])
                        ime[m-1, n+1] = 0
                        ims[m-1, n+1] = k

                    if ((ime[m+1, n-1]) != 0):                                   
                        fifo.append([m+1, n-1])
                        ime[m+1, n-1] = 0
                        ims[m+1, n-1] = k

                    if ((ime[m+1, n+1]) != 0):                                   
                        fifo.append([m+1, n+1])
                        ime[m+1, n+1] = 0
                        ims[m+1, n+1] = k

                    if ((ime[m, n-1]) != 0):                                   
                        fifo.append([m, n-1])
                        ime[m, n-1] = 0
                        ims[m, n-1] = k

                    if ((ime[m, n+1]) != 0):                                   
                        fifo.append([m, n+1])
                        ime[m, n+1] = 0
                        ims[m, n+1] = k

                    if ((ime[m-1, n]) != 0):                                   
                        fifo.append([m-1, n])
                        ime[m-1, n] = 0
                        ims[m-1, n] = k

                    if ((ime[m+1, n]) != 0):                                   
                        fifo.append([m+1, n])
                        ime[m+1, n] = 0
                        ims[m+1, n] = k  
    print("Número total de objetos: ", k)

    return ims

# Llamada a la función Etiquetado de Imagen 
etiquetadoImagen(ime, ims)

# Se despliega la imagen original 
plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

# Se despliega la imagen etiquetada 
plt.subplot(1, 2, 2)
plt.imshow(ims, 'gray')
plt.title('Imagen Etiquetada')
plt.xticks([]), plt.yticks([])

plt.show()