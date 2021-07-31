import numpy as np
import cv2 
import pickle

# def preprocess(img):
#     img = cv2.resize(img,(200,200))
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     img = img.reshape(1,200,200,1)
#     img = img/255
#     return img


face_data = "haarcascade_frontalface_default.xml"
classifier =  cv2.CascadeClassifier(cv2.data.haarcascades + face_data)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}
with open("labels.pickle", 'rb') as f:
    labels = pickle.load(f)
    labels = {v:k for k,v in labels.items()}

video_capture = cv2.VideoCapture(0)
ret = True
while ret:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray,1.2,5)
    for x,y,w,h in faces:
        gray_img = gray[y:y+h,x:x+w].copy()
        id_, conf = recognizer.predict(gray_img) 
        # print(conf)
        if conf >= 45:
            cv2.putText(frame,labels[id_],(x,y),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
        else:
            cv2.putText(frame,"none",(x,y),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
            
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),5) 

    cv2.imshow('live video',frame)
    if cv2.waitKey(1)==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
