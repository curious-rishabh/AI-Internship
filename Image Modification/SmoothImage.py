import cv2
img = cv2.imread("rb3.jpeg")

gaussianBlurImg = cv2.GaussianBlur(img,(25,25),0)

cv2.imwrite("gaussianImage2.jpg", gaussianBlurImg)