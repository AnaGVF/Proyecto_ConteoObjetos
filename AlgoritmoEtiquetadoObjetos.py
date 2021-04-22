# Etiquetado de Objetos

# Algoritmo de Etiquetado de Objetos

# Nombre: Ana Graciela Vassallo Fedotkin
# Expediente: 278775
# Nombre: 
# Expediente: 

# Fecha de entrega: 26 de Abril 2021.

import cv2
from matplotlib import pyplot as plt
import numpy as np

# Imagen de Entrada
imagenOriginal = cv2.imread('img/EtiquetadoObjetos.PNG', 2)
ime = cv2.imread('img/EtiquetadoObjetos.PNG', 2)
ims = np.zeros(ime.shape, np.uint8)

fifo = []

def etiquetadoImagen(ime, ims):
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
                ims[i][j] = k
                while(len(fifo)>0):                  #5MIENTRAS fifo no está vacía hacer     
                    coordenada=fifo.pop(0)  #3,3            #usar POP para sacar la coordenada del valor que vamos a utilizar y buscar sus vecinos
                    m=coordenada[0]
                    n=coordenada[1]
                
                    #print("R: ",m)         #Para comprobar que haya pasado la coordenada m
                    #print("C: ",n)         #Para comprobar que haya pasado la coordenada n
                    #print(coordenada)      #Lo usamos para saber cómo se comportaba
                    if ((ime[m-1,n-1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m-1,n-1])
                        ime[m-1,n-1]=0
                        ims[m-1,n-1]=k

                    if ((ime[m-1,n+1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m-1,n+1])
                        ime[m-1,n+1]=0
                        ims[m-1,n+1]=k

                    if ((ime[m+1,n-1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m+1,n-1])
                        ime[m+1,n-1]=0
                        ims[m+1,n-1]=k

                    if ((ime[m+1,n+1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m+1,n+1])
                        ime[m+1,n+1]=0
                        ims[m+1,n+1]=k

                    if ((ime[m,n-1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m,n-1])
                        ime[m,n-1]=0
                        ims[m,n-1]=k

                    if ((ime[m,n+1])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m,n+1])
                        ime[m,n+1]=0
                        ims[m,n+1]=k


                    if ((ime[m-1,n])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m-1,n])
                        ime[m-1,n]=0
                        ims[m-1,n]=k

                    if ((ime[m+1,n])!=0):                                   #Con esa cordenada, haremos los IF
                        fifo.append([m+1,n])
                        ime[m+1,n]=0
                        ims[m+1,n]=k  
    print(k)
    return ims


etiquetadoImagen(ime, ims)

plt.subplot(1, 2, 1)
plt.imshow(imagenOriginal, 'gray')
plt.title('Imagen Original')
plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(ims, 'gray')
plt.title('Imagen Etiquetada')
plt.xticks([]), plt.yticks([])

plt.show()