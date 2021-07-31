import cv2 


face_data = "haarcascade_frontalface_default.xml"
classifier =  cv2.CascadeClassifier(cv2.data.haarcascades + face_data)


video_capture = cv2.VideoCapture(0)
ret = True
c = 1
while ret:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray,1.2,5)
    for x,y,w,h in faces:
        gray_img = frame[y:y+h,x:x+w].copy()
        gray_itm = str(c) + ".jpg"
        c += 1
        cv2.imwrite(gray_itm, gray_img)  #save this gray image as 'gray-img.png' 

    cv2.imshow('live video',frame)
    if cv2.waitKey(1)==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
