import cv2 as cv
import numpy as np
import func as fc

img = cv.imread('lena.jpg', 0)

#Filtragem 

img2 = fc.gaussian_filter(img)

cv.imshow('Imagem - Lena 2', img)
cv.waitKey(0)

img3 = fc.laplacian_filter(img, 4)

cv.imshow('Imagem - Lena 3', img3)
cv.waitKey(0)

soma = fc.soma_img(img,img3)
cv.imshow('Imagem - Lena SOMA', soma)
cv.waitKey(0)