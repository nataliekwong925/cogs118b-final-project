import cv2 as cv
import numpy as np
import os 

#convert images to gray
def convert_to_gray(folder):
    for filename in os.listdir(folder):
        img = cv.imread(folder+filename)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(folder+filename, gray)

# image = cv.imread('/test/ISIC_0024306.jpg')
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
convert_to_gray('/test/')

