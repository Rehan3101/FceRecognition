from operator import imod
from tkinter import*
from tkinter import ttk
import cv2
from time import strftime
import webbrowser
from datetime import datetime
from turtle import bgcolor, bgpic, right
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
from django.db import DatabaseError
import mysql.connector
import  os
import csv
from tkinter import filedialog


class Support:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x300+400+200")
        self.root.title("Support")

#bgimg        

        img1=Image.open(r"Images\support.jpg")
        img1=img1.resize((500,300), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=300)

        def callback(url):
                webbrowser.open_new_tab(url)

#=============Gmail link=======
        
        text_lbl=Label(self.root,text="Email: rehanali4397@gmail.com",font=("Monaco",14,"bold" ),bg="azure1",fg="Black")
        text_lbl.place(x=0,y=175,width=350,height=20)
        Email_me="https://mail.google.com/mail/mu/mp/663/#co"
        text_lbl=Label(self.root,text="Email:",font=("Monaco",14,"bold" ),bg="lightgreen",fg="Black")
        text_lbl.place(x=10,y=200,width=100,height=20)
        link = Label(self.root, text="Email_me",font=('Helveticabold', 14), fg="blue", cursor="hand2")
        link.pack()
        link.place(x=120,y=200)
        link.bind("<Button-1>", lambda e:
        callback("https://mail.google.com/mail/mu/mp/663/#co"))

#Create a Label to display the link

        Rehan_Ali="https://www.instagram.com/_____rehan.ali/"
        text_lbl=Label(self.root,text="Instagram:",font=("Monaco",13,"bold" ),bg="lightgreen",fg="Black")
        text_lbl.place(x=10,y=250,width=100,height=20)
        link = Label(self.root, text="Rehan_Ali",font=('Helveticabold', 13), fg="blue", cursor="hand2")
        link.pack()
        link.place(x=120,y=250)
        link.bind("<Button-1>", lambda e:
        callback("https://www.instagram.com/_____rehan.ali/"))





if __name__ == "__main__":
    root=Tk()
    obj=Support(root)
    root.mainloop()  