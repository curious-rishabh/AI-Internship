# pip install pyautogui

import imutils
import cv2

redLower = (25, 52, 72)
redUpper = (50, 255, 255)

camera = cv2.VideoCapture(0)

while True:
    # reading frame from camera
    (grabbed, frame) = camera.read()
    # resizing the frame
    frame = imutils.resize(frame, width = 600)
    # smoothing
    blurred =cv2.GaussianBlur(frame,(11,11),0)
    # convert bgr to hsv color format
    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    
    # mask green color
    mask = cv2.inRange(hsv,redLower, redUpper)
    mask = cv2.erode(mask,None,iterations= 2)
    mask = cv2.dilate(mask,None,iterations=2)
    
    # find neighbourhood pixels around place
    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            # outer circle
            cv2.circle(frame, (int (x), int(y)), int(radius), (0,255,255), 2)
            # inner circle which is dot
            cv2.circle(frame,center,5,[0,0,255],-1)
            print(center,radius)
            
            if radius >250:
                print("Stop")
            else:
                if(center[0] <150):
                    print('Left')
                elif (center[0]>450):
                    print ('Right')
                elif (radius<240):
                    print("Front")
                else:
                    print("Stop")
                    
    cv2.imshow("Object Tracking By Color", frame)
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()    