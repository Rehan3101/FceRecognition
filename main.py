import imp
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from time import strftime, time
from datetime import datetime
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
import os
from studentdetails import Student
from support import Support
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from support import Support


class Face_Recognition_System:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1400x650+0+0")
                self.root.title("Face Recognition System") 

#bgcolor
                bg_color=Label(self.root,bg="azure1")
                bg_color.place(x=0,y=0,width=1400,height=650) 


                  


#Upper image
                img1=Image.open(r"Images\facial1.jpg")
                img1=img1.resize((1400,250), Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=-100,y=0,width=1400,height=250)

# image
                img2=Image.open(r"Images\bgg1.jpg")
                img2=img2.resize((1400,420), Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=0,y=250,width=1400,height=420)





        #Title
                title_lbl=Label(self.root,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("Monaco",30,"bold" ),bg="azure1",fg="darkslategray")
                title_lbl.place(x=100,y=255,width=1100,height=50)

        #======Time=======

                def time():
                        string = strftime('%H:%M:%S %p')
                        lbl.config(text= string)
                        lbl.after(1000,time)   

                lbl=Label(self.root,font=('times new roman',14,'bold'),bg="white",fg='black')
                lbl.place(x=1150,y=20,width=110,height=30)
                time()             

        #Student Button
                B1=Image.open(r"Images\student.jpg")
                B1=B1.resize((116,116), Image.ANTIALIAS)
                self.photoB1=ImageTk.PhotoImage(B1)

                b1=Button(self.root,image=self.photoB1,command=self.student_details,cursor="hand2",bg="grey")
                b1.place(x=320,y=330,width=116,height=116)

                b1_text=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b1_text.place(x=320,y=430,width=116,height=20)

        #Detect Face
                B2=Image.open(r"Images\rec.jpg")
                B2=B2.resize((116,116), Image.ANTIALIAS)
                self.photoB2=ImageTk.PhotoImage(B2)

                b2=Button(self.root,command=self.face_recognition,image=self.photoB2,cursor="hand2",bg="grey")
                b2.place(x=570,y=330,width=116,height=116)

                b2_text=Button(self.root,command=self.face_recognition,text="Face Recognition",cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b2_text.place(x=570,y=430,width=116,height=20)

        #Attendance Report
                B3=Image.open(r"Images\attendance.jpg")
                B3=B3.resize((116,116), Image.ANTIALIAS)
                self.photoB3=ImageTk.PhotoImage(B3)

                b3=Button(self.root,command=self.attendance,image=self.photoB3,cursor="hand2",bg="grey")
                b3.place(x=820,y=330,width=116,height=116)

                b3_text=Button(self.root,command=self.attendance,text="Attendance CSV",cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b3_text.place(x=820,y=430,width=116,height=20)

        




        #Train Data
                B5=Image.open(r"Images\datatrain.png")
                B5=B5.resize((116,116), Image.ANTIALIAS)
                self.photoB5=ImageTk.PhotoImage(B5)

                b5=Button(self.root,command=self.train_data,image=self.photoB5,cursor="hand2",bg="grey")
                b5.place(x=320,y=480,width=116,height=116)

                b5_text=Button(self.root,command=self.train_data,text="Train Data",cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b5_text.place(x=320,y=580,width=116,height=20)

        #Sample Photos
                B6=Image.open(r"Images\sample2.jpg")
                B6=B6.resize((116,116), Image.ANTIALIAS)
                self.photoB6=ImageTk.PhotoImage(B6)

                b6=Button(self.root,command=self.open_img,image=self.photoB6,cursor="hand2",bg="grey")
                b6.place(x=570,y=480,width=116,height=116)

                b6_text=Button(self.root,command=self.open_img,text="Sample Photos",cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b6_text.place(x=570,y=580,width=116,height=20)

        #Developer
                B7=Image.open(r"Images\deve.jpg")
                B7=B7.resize((116,116), Image.ANTIALIAS)
                self.photoB7=ImageTk.PhotoImage(B7)

                b7=Button(self.root,command=self.developer,image=self.photoB7,cursor="hand2",bg="grey")
                b7.place(x=820,y=480,width=116,height=116)

                b7_text=Button(self.root,command=self.developer,text="About Developer",cursor="hand2",font=("times new roman",11,"bold" ),bg="antiquewhite3")
                b7_text.place(x=820,y=580,width=116,height=20)

        #Support
                B4=Image.open(r"Images\helpdesk.jpg")
                B4=B4.resize((70,70), Image.ANTIALIAS)
                self.photoB4=ImageTk.PhotoImage(B4)

                b4=Button(self.root,command=self.support,image=self.photoB4,cursor="hand2",bg="green")
                b4.place(x=1110,y=550,width=70,height=70)

                

        #exit
                B8=Image.open(r"Images\exit.jpg")
                B8=B8.resize((70,70), Image.ANTIALIAS)
                self.photoB8=ImageTk.PhotoImage(B8)

                b8=Button(self.root,command=self.iExit,image=self.photoB8,cursor="hand2",bg="black")
                b8.place(x=1180,y=550,width=70,height=70)

               

        def open_img(self):
                os.startfile("Data")

        def iExit(self):
                self.iExit=messagebox.askyesno("Exit Window","Are you sure, you want to exit",parent=self.root)
                if self.iExit >0:
                        self.root.destroy()
                else:
                        return        



#=================FUNCTION BUTTONS=============

        #Student details button function
        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)


    
        #Train Data Button function

        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)


        #Face Recognition button function   
        def face_recognition(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

        #attendance details button function   
        def attendance(self):
                self.new_window=Toplevel(self.root)
                self.app=Attendance(self.new_window)

        #About Developer button function
        def developer(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)

        #Support button function
        def support(self):
                self.new_window=Toplevel(self.root)
                self.app=Support(self.new_window)
                            


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        

