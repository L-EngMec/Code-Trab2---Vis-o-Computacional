import cv2 as cv
import numpy as np


def gaussian_filter(img):
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            A = x + 1
            B = x - 1
            C = y + 1
            D = y - 1
        
            if A > img.shape[0] - 1:
                A = 0
            if B < 0:
                B = 0
            if C > img.shape[1] - 1:
                C = 0
            if D < 0:
                D = 0
        
            img[y,x] = (img[D,B]*1/16 + img[D,x]*2/16 + img[D,A]*1/16 + img[y,B]*2/16 + img[y,x]*4/16 + img[y,A]*2/16+ img[C,B]*1/16 + img[C,x]*2/16 + img[C,A]*1/16)
            
    return img

def laplacian_filter(img, R):

    img = np.array(img, float)

    for i in range(0, R):
        for y in range(0, img.shape[0]):
            for x in range(0, img.shape[1]):
                A = x + 1
                B = x - 1
                C = y + 1
                D = y - 1
        
                if A > img.shape[1] - 1:
                    A = 0
                if B < 0:
                    B = 0
                if C > img.shape[0] - 1:
                    C = 0
                if D < 0:
                    D = 0

                img[y,x] = ((img[D,B]*(-1) + img[D,x]*(-1) + img[D,A]*(-1) + img[y,B]*(-1) + img[y,x]*(8) + img[y,A]*(-1) + img[C,B]*(-1) + img[C,x]*(-1) + img[C,A]*(-1)))/(9)
                
    return img

def soma_img(img1,img2):
    imgRes = img1 + img2
    
    lista = []
    
    for y in range(0, imgRes.shape[0]):
        for x in range(0, imgRes.shape[1]):
            lista.append(imgRes[y,x])
    minimo = lista[0]
    maximo = lista[-1]
    
    for y in range(0, imgRes.shape[0]):
        for x in range(0, imgRes.shape[1]):
            imgRes[y,x] = 255*(imgRes[y,x] - minimo)/(maximo - minimo)
    
    return imgRes
    
