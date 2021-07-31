import numpy as np
import cv2 
import matplotlib.pyplot as plt
from keras.models import load_model

print('model loading...')
model = load_model('face_CET.h5')
print('model loaded')

def preprocess(img):
    img = cv2.resize(img,(200,200))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = img.reshape(1,200,200,1)
    img = img/255
    return img


face_data = "haarcascade_frontalface_default.xml"
classifier =  cv2.CascadeClassifier(cv2.data.haarcascades + face_data)

label_map = ['bishal', 'debashish' ,'deepak', 'hitesh', 'sambid']

video_capture = cv2.VideoCapture(0)
ret = True
while ret:
    ret, frame = video_capture.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(image,1.2,5)
    for x,y,w,h in faces:
        face_img = frame[y:y+h,x:x+w].copy()
        # face_img = np.array(face_img)
        # face_img = np.expand_dims(face_img, axis=0)
        face_img = preprocess(face_img)
        pred = np.argmax(model.predict(face_img), axis=-1) # model.predict_classes(face_img)[0]
        # print(pred)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        cv2.putText(frame,label_map[pred[0]],(x,y),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)   
    cv2.imshow('live video',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
