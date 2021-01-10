# Text recognition from images using Pytesseract lib

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\installations\pytesseract\inst\Tesseract-OCR\tesseract.exe'
import cv2
from PIL import Image
import tensorflow as tf

# Read and display image
image = cv2.imread('sample3.jpg')
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Some functions of tesseract
print(pytesseract.image_to_string(img_rgb))               # Prints out the text
print(pytesseract.get_languages(config=''))               # List of available languages

#--------- Prints out the letters and corresponding coordinates and create BB around them ------

print(pytesseract.image_to_boxes(img_rgb))                # Prints out the letters and corresponding coordinates
bounding_box_coordinates = pytesseract.image_to_boxes(img_rgb)
image_h, image_w, _ = img_rgb.shape
for bounding_box in bounding_box_coordinates.splitlines():
    print(type(bounding_box))          # string class
    print(bounding_box)
    bounding_box = bounding_box.split(' ')
    x1,y1,x2,y2 = int(bounding_box[1]), int(bounding_box[2]),int(bounding_box[3]),int(bounding_box[4])

    cv2.rectangle(img_rgb, (x1,image_h-y1), (x2,image_h-y2), (0,0,255), thickness=3)

cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)      # WINDOW_NORMAL or WINDOW_AUTOSIZE
cv2.imshow('image', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
