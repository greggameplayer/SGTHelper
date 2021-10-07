import numpy as np 
import cv2
from win10toast import ToastNotifier
import time
from tkinter import *
import subprocess


window = Tk()

window.title("SGT Helper")
window.geometry("1080x720")
window.minsize(480,360)
window.config(background='#f4f6c8')


label_title = Label(window, text="Bienvenue sur SGT Helper", font=("Courrier",40), bg='#f4f6c8', fg='#101f7a')
label_title.pack()

label_subtitle = Label(window, text="Voici les fonctionnalité a savoir pour utiliser l'application :", font=("Courrier",30), bg='#f4f6c8', fg='#101f7a')
label_subtitle.pack()

label_subtitle = Label(window, text="- Appuyer sur la touche A pour activé l'application", font=("Courrier",20), bg='#f4f6c8', fg='#101f7a')
label_subtitle.pack()

label_subtitle = Label(window, text="- Appuyer sur la touche E pour éteindre l'application", font=("Courrier",20), bg='#f4f6c8', fg='#101f7a')
label_subtitle.pack()

label_subtitle = Label(window, text="- Au bout de 8 clignement de yeux, l'application s'eteindra au bout de 5 secondes", font=("Courrier",20), bg='#f4f6c8', fg='#101f7a')
label_subtitle.pack()

label_subtitle = Label(window, text="si vous ne voulez pas que l'application s'éteigne appuyé sur la touche B ", font=("Courrier",20), bg='#f4f6c8', fg='#101f7a')
label_subtitle.pack()

window.mainloop()  


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

first_read = True
  
count=0

cap = cv2.VideoCapture(0) 
ret,img = cap.read() 
  
while(ret): 
    ret,img = cap.read() 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    gray = cv2.bilateralFilter(gray,5,1,1) 
  
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200)) 
    if(len(faces)>0): 
        for (x,y,w,h) in faces: 
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
  
            
            roi_face = gray[y:y+h,x:x+w] 
            roi_face_clr = img[y:y+h,x:x+w] 
            eyes = eye_cascade.detectMultiScale(roi_face,1.3,5,minSize=(50,50)) 
  
            
            if(len(eyes)>=2): 
                if(first_read): 
                    cv2.putText(img,  
                    "No eyes detected", (70,70), 
                    cv2.FONT_HERSHEY_PLAIN, 3, 
                    (0,0,255),2) 
                else: 
                    print("Blink detected--------------")
                    count=count + 1
                    
            if (count == 8):
                toaster = ToastNotifier()
                toaster.show_toast(
                "Début de crise",
                "Le logiciel a detecté un début de crise, la caméra va s'éteindre au bout de 5 secondes, sinon appuyé sur la touche b",
                duration=10)
                time.sleep(5)
            elif (a==ord('b')):
                count=0

  
    
    cv2.imshow('img',img) 
    a = cv2.waitKey(1) 

    if(a==ord('a') and first_read):
        toaster = ToastNotifier()
        toaster.show_toast(
        "Mode Activé",
        "La caméra est acctivé",
        duration=10)
        first_read = False
    elif (a==ord('e')or count ==8):
        toaster = ToastNotifier()
        toaster.show_toast(
        "Mode Arret",
        "La caméra va s'éteindre",
        duration=10)
        break
cap.release()
cv2.destroyAllWindows() 
