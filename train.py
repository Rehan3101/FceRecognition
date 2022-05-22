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


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Train Data")


    #bgcolor
        bg_color=Label(self.root,bg="lightblue")
        bg_color.place(x=0,y=0,width=1400,height=650)



    #Title
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold" ),bg="white",fg="purple")
        title_lbl.place(x=40,y=10,width=1200,height=50)


    #Images


        #1
        img1=Image.open(r"Images\sms3.jpg")
        img1=img1.resize((550,250), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=75,y=70,width=550,height=250)

        #2
        img2=Image.open(r"Images\train.jpg")
        img2=img2.resize((550,250), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=650,y=70,width=550,height=250)

        #text
        text_lbl=Label(self.root,text="Click here to Train Data:",font=("times new roman",20,"bold" ),fg="Black")
        text_lbl.place(x=450,y=370,width=400,height=20)


    #Train Button
        Train_text=Button(self.root,command=self.train_classifier,text="TRAIN DATA",cursor="hand2",font=("times new roman",24,"bold" ),bg="lightgreen",fg="Black")
        Train_text.place(x=515,y=400,width=300,height=50)  

#===========Train Function
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  #list comprehensing      
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L")   #Gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13

        ids=np.array(ids)

#=============================Train the Classifier And Save=================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets in completed!!",parent=self.root)






if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        