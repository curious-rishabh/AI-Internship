import cv2
import time
import imutils

# initialise camera
cam = cv2.VideoCapture(0)
# giving 1 second delay
time.sleep(1)

firstFrame = None
# Threshold for how much change can be noticed in moving object
area = 800

while True:
    # reading frame from camera
    _,img = cam.read()
    # No movement detected
    text = "Normal"
    # resizing frame 
    img = imutils.resize(img, width=900)
    # convert color to grayscale image
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Blur Image
    gaussianImg = cv2.GaussianBlur(grayImg,(21,21), 0)
    
    # save first frame int firstFrame variable
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    # difference between first background frame with current frame
    imgDiff = cv2.absdiff(firstFrame,gaussianImg)
    # detected region is converted into binary
    thresholdImg = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    thresholdImg = cv2.dilate(thresholdImg,None,iterations=2)
    
    cnts = cv2.findContours(thresholdImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        # drawing rectangle
                        # startPoint, endPoint, GreenColor
        cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0))
        text = "Moving Object Detected"
    print(text)
    # putting text on image
                    # text, position of text, Font, Font Size, Font Color, thickness of font
    cv2.putText(img,text,(10,20),
                cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("Camera Feed", img)
    key = cv2.waitKey(1) & 0xff
    if key == ord("q"):
        break
    
cam.release()
cv2.destroyAllWindows()

    
    