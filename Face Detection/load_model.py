import pickle 
import numpy as np
import cv2
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop   #RMSprop is same as Adam but it calculates the root means square error
from keras.utils.np_utils import to_categorical

with open('face_images_/images.p','rb') as f:
  images=pickle.load(f)
with open('face_images_/labels.p','rb') as f:
  labels=pickle.load(f)

# plt.imshow(images[0])
# plt.title(labels[0],color='w')
# plt.show()

#preparing the data

images=images.reshape(images.shape[0],200,200,1)
images=images/255

# print(labels)
#first label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
labels=le.fit_transform(labels)
# print(labels)
label_mapping=le.inverse_transform(list(set(labels)))

with open('label_map.p','wb') as f:
  images=pickle.dump(label_mapping,f)

#now one hot encoding
labels=to_categorical(labels,len(set(labels)))

model=Sequential()
model.add(Conv2D(16,(5,5),input_shape=(200,200,1),activation='relu'))
model.add(Conv2D(16,(5,5),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3),activation='relu'))
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())

#classification part
model.add(Dense(512,activation='relu'))
model.add(Dense(256,activation='relu'))
model.add(Dense(len(label_mapping),activation='softmax'))
model.compile(RMSprop(lr=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

print(model.summary())
model.save('face_CET.h5')