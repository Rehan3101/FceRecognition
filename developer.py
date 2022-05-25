from tkinter import*
from tkinter import ttk
import cv2
from time import strftime
from datetime import datetime
from turtle import bgcolor
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
import mysql.connector

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("About Developer")

       

#bgimg
        img1=Image.open(r"Images\bgw.jpg")
        img1=img1.resize((1280,650), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1280,height=650)

#Title
        title_lbl=Label(self.root,text="ABOUT DEVELOPER",font=("Monaco",40,"bold","bold" ),bg="darkslategray",fg="azure1")
        title_lbl.place(x=0,y=0,width=1400,height=40) 

 #======Time=======

        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text= string)
                lbl.after(1000,time)   

        lbl=Label(self.root,font=('times new roman',14,'bold'),bg="white",fg='black')
        lbl.place(x=1150,y=20,width=110,height=30)
        time()    

        




#Developer Info
        id_label=Label(self.root,text='Hello! I am Rehan Ali.',font=("times new roman",12,"bold"))
        id_label.place(x=450,y=100)

        id_label=Label(self.root,text='Currently pursuing Bachelors of Technology in Information Technology',font=("times new roman",12,"bold"))
        id_label.place(x=450,y=130)
        
        id_label=Label(self.root,text='from ABES Engineering College, Ghaziabad.',font=("times new roman",12,"bold"))
        id_label.place(x=450,y=160)

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







if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()