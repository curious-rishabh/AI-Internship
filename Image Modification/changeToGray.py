import cv2 
img = cv2.imread("rb3.jpeg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color to grey image
cv2.imwrite("grayImage.png", grayImg)

cv2.imshow("Original", img)
cv2.imshow("Gray", grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()