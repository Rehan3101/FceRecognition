from cgitb import text
from tkinter import*
from tkinter import ttk
import cv2
import numpy as np
from turtle import bgcolor
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
from django.db import DatabaseError
import mysql.connector
import os
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Face Recognition")


        bgimg=Image.open(r"Images\bgg.jpg")
        bgimg=bgimg.resize((1300,650), Image.ANTIALIAS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)

        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=0,width=1300,height=650)

     


        #Title
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Monaco",30,"bold" ),bg="azure2",fg="Brown")
        title_lbl.place(x=40,y=10,width=1200,height=50)

         #======Time=======

        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text= string)
                lbl.after(1000,time)   

        lbl=Label(self.root,font=('times new roman',14,'bold'),bg="white",fg='black')
        lbl.place(x=1150,y=20,width=110,height=30)
        time()    


        #Images
        

        #3 center
        img3=Image.open(r"Images\face7.jpg")
        img3=img3.resize((450,350), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=400,y=70,width=450,height=350)


        #Detect Face Button
        face_text=Button(self.root,text="RECOGNIZE FACE",command=self.face_rec,cursor="hand2",font=("times new roman",24,"bold" ),bg="green",fg="darkRed")
        face_text.place(x=400,y=430,width=450,height=50)

        #text
        text_text=Label(self.root,text="Tap Above button for face recognition:",font=("times new roman",14,"bold" ),fg="Black")
        text_text.place(x=400,y=490,width=350,height=20)

#exit
        B8=Image.open(r"Images\exit.jpg")
        B8=B8.resize((70,70), Image.ANTIALIAS)
        self.photoB8=ImageTk.PhotoImage(B8)

        b8=Button(self.root,command=self.iExit,image=self.photoB8,cursor="hand2",bg="black")
        b8.place(x=1180,y=550,width=70,height=70)

    def iExit(self):
                self.iExit=messagebox.askyesno("Exit Window","Are you sure, you want to exit",parent=self.root)
                if self.iExit >0:
                        self.root.destroy()
                else:
                        return   

 #===========================Attendance===============
    def mark_attendance(self,si,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((si not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{si},{r},{n},{d},{dtString},{d1},Present")    




    #==============Function for face recognition==========
    def face_rec(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            co_ord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="facerecognition.cylhakipgxhv.ap-south-1.rds.amazonaws.com",username="root",password="Rehan2002",database="facerecognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                si=my_cursor.fetchone()
                si="+".join(si)


                if confidence>77:
                     cv2.putText(img,f"ID:{si}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                     self.mark_attendance(si,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                co_ord=[x,y,w,h]

            return co_ord

        def recognize(img,clf,faceCascade):
            co_ord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_capture.release()
        cv2.destroyAllWindows()                


       
        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        