import cv2
img=cv2.imread("boy.jpg")
grayimg=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
cascade=cv2.CascadeClassifier("/Users/natarajan_velayutham/Desktop/python classes/PRO-C106-Student-Boilerplate/haarcascade_frontalface_default.xml")
faces=cascade.detectmultiScale(grayimg,1.1,5)
for (x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("img",img)
cv2.WaitKey(0)
