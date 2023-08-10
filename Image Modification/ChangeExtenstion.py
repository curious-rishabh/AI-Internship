import cv2
img = cv2.imread("rb3.jpeg") # read an image
cv2.imwrite("SampleCopy.png", img) # save an image
cv2.imshow("AI_Master_Class",img)

cv2.waitKey(0)
cv2.destroyAllWindows()