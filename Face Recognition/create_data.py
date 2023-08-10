import cv2, os
haar_file = "haarcascade_frontalface_default.xml"
datasets = "Opencv/Face Recognition/datasets"
sub_data = "Rishabh"

path = os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
    
(width,height) = (130,100)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_file)
webcam = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    # read frame from camera
    _ , im = webcam.read()
    # convert into gray scale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,4)
    for (x,y,w,h) in faces:
        # draw rectangle
        cv2.rectangle(im, (x,y), (x+w,y+h), (255,0,0),2)
        # crop rectangle
        face = gray[y:y +h, x:x+w]
        # resize to frame size
        face_resize = cv2.resize(face, (width,height))
        # save image
        cv2.imwrite("%s/%s.png" % (path,count), face_resize)
    count +=1
    
    cv2.imshow("Face Data", im)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()
    