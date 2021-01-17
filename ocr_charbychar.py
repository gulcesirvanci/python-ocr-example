import cv2
import pytesseract
from PIL import ImageOps, Image

#bounding box 1

img = cv2.imread('fotoo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

resized = cv2.resize(img, (0,0), fx=5, fy=5)

# Detecting Characters
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(" ")
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0,250,0), 3)
    cv2.putText(img, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 250, 50), 2 )

cv2.imshow('original', resized)
cv2.waitKey()