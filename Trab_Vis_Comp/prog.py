import cv2 as cv
import numpy as np

#FILTRAGEM

img = cv.imread('dog.jpg', 0)
#cv.imshow('dog - original', img)
#cv.waitKey(0)

DFT = cv.dft(np.float32(img), flags = cv.DFT_COMPLEX_OUTPUT)

'''cv.imshow('Filtro Fourier', DFT)
cv.waitKey(0)'''

print(DFT[0,2,5])


for y in range(0, DFT.shape[0]):
    for x in range(0, DFT.shape[1]):
        if DFT[y,x] < 0:
            DFT[y,x] = DFT[y,x]*(-1)

print(DFT)