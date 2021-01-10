# Extracting text from images using EasyOCR library

#Import the required libraries
import cv2
import easyocr
#import matplotlib.pyplot as plt

# Text reader
reader = easyocr.Reader(['en'])         # Specify the language of the text

image = cv2.imread('sample3.jpg')

# Read the text in the image
result = reader.readtext('sample3.jpg')
print(result[:][1])

cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)      # WINDOW_NORMAL or WINDOW_AUTOSIZE
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()