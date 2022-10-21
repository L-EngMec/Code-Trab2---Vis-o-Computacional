import cv2 as cv
import numpy as np
import func as fc

img = cv.imread('lena.jpg', 0)
cv.imshow('lena original', img)
cv.waitKey(0)


cv.imshow('Invertida', fc.inverter(img))
cv.waitKey(0)


#Filtragem 


img2 = fc.gaussian_filter(img,5)
cv.imshow('Lena - gaussian_filter', img)
cv.waitKey(0)

cv.imshow('Lena Invertida - gaussian_filter', fc.inverter(img))
cv.waitKey(0)


img3 = fc.laplacian_filter(img, 3)
cv.imshow('Lena - laplacian_filter', img3)
cv.waitKey(0)


cv.imshow('Lena - laplacian_filter2', fc.inverter(img3))
cv.waitKey(0)


soma = fc.soma_img(img,img3)
cv.imshow('Lena SOMA', fc.inverter(soma))
cv.waitKey(0)

'''

'''