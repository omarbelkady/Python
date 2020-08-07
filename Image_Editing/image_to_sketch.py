import numpy as np
import imageio
import scipy.ngimage
import cv2

#Name of image to convert
img="photo.jpg"

#Reading the image
s= imageio.imread(img)

def grayscaleConversion(rgb):
    #Convert to black and white img
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

#Convert the image into a grey
g=grayscaleConversion(s)

def dodge(the_front, the_back):
    result = the_front*255/(255-the_back)
    result[result>255]=255
    result[back==255] = 255
    return result.astype('uint8')

#Variable that will store the dimension highest number = 255(white)
#Lowest number is darkest
#If you want img to be white 255,255,255
# If you want img to be black 0,0,0
i=255-g

#Blurred image and sigma means how intense your blurred image is
b = scipy.ngimage.filters.gaussian_filer(i, sigma= 10)


r = dodge(b,g)


#Using an opencv function to create the new image
cv2.imwrite('my_new.png',r)
