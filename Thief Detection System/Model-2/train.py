import os
import cv2
import pickle
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_data = "haarcascade_frontalface_default.xml"
face_cascade =  cv2.CascadeClassifier(cv2.data.haarcascades + face_data)

recognizer = cv2.face.LBPHFaceRecognizer_create()

y_labels = []
x_train = []

curr_id = 0
label_ids = {}

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            # print(label, path)
            if not label in label_ids:
                label_ids[label] = curr_id
                curr_id += 1
            # print(label_ids)
            id_ = label_ids[label]
            
            pil_img = Image.open(path).convert("L")    #'L' for gray
            # pil_img = pil_img.resize((200, 200), Image.ANTIALIAS)
            img_array = np.array(pil_img, "uint8")
            # print(len(img_array))
            faces = face_cascade.detectMultiScale(img_array,1.2,5)
            # print(len(faces))
            for x,y,w,h in faces:
                roi = img_array[y:y+h, x:x+h]
                x_train.append(roi)
                # print(id_)
                y_labels.append(id_)
            

# print(label_ids)
# print(y_labels)
# print(len(x_train))
with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)


recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")