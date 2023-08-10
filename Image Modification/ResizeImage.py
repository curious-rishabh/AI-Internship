import cv2
import imutils

img = cv2.imread("rb3.jpeg")

resizeImg = imutils.resize(img,width=50)
cv2.imwrite("resizedImage.jpg", resizeImg)