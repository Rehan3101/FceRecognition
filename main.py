from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
import os
from studentdetails import Student
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1400x650+0+0")
                self.root.title("Face Recognition System")  


       #bgcolor
                bg_color=Label(self.root,bg="lightgreen")
                bg_color.place(x=0,y=0,width=1400,height=650)           


        #centre image
                img1=Image.open(r"Images\image1.png")
                img1=img1.resize((400,120), Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=450,y=0,width=400,height=120)



        #ryt corner image
                img2=Image.open(r"Images\image2.png")
                img2=img2.resize((450,120), Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=850,y=0,width=450,height=120)



        #left corner logos

                #tkinter
                img3=Image.open(r"Images\tkinter1.png")
                img3=img3.resize((300,40), Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                f_lbl=Label(self.root,image=self.photoimg3)
                f_lbl.place(x=150,y=0,width=300,height=40)

                #logo
                logo=Image.open(r"Images\face1.jpg")
                logo=logo.resize((150,120), Image.ANTIALIAS)
                self.photologo=ImageTk.PhotoImage(logo)

                f_lbl=Label(self.root,image=self.photologo)
                f_lbl.place(x=0,y=0,width=150,height=120)
        
       
                #opencv
                img4=Image.open(r"Images\opencv1.jpg")
                img4=img4.resize((300,40), Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                f_lbl=Label(self.root,image=self.photoimg4)
                f_lbl.place(x=150,y=40,width=300,height=40)


                #mysql
                img5=Image.open(r"Images\mysql.png")
                img5=img5.resize((300,40), Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                f_lbl=Label(self.root,image=self.photoimg5)
                f_lbl.place(x=150,y=80,width=300,height=40)


                #Title
                title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",25,"bold" ),fg="red")
                title_lbl.place(x=75,y=130,width=1080,height=50)

                #Student Button
                B1=Image.open(r"Images\student.png")
                B1=B1.resize((150,150), Image.ANTIALIAS)
                self.photoB1=ImageTk.PhotoImage(B1)

                b1=Button(self.root,image=self.photoB1,command=self.student_details,cursor="hand2")
                b1.place(x=150,y=200,width=150,height=150)

                b1_text=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold" ))
                b1_text.place(x=150,y=350,width=150,height=30)

                #Detect Face
                B2=Image.open(r"Images\Face3.png")
                B2=B2.resize((150,150), Image.ANTIALIAS)
                self.photoB2=ImageTk.PhotoImage(B2)

                b2=Button(self.root,command=self.face_recognition,image=self.photoB2,cursor="hand2")
                b2.place(x=400,y=200,width=150,height=150)

                b2_text=Button(self.root,command=self.face_recognition,text="Face Recognition",cursor="hand2",font=("times new roman",12,"bold" ))
                b2_text.place(x=400,y=350,width=150,height=30)

                #Attendance Report
                B3=Image.open(r"Images\attendance.jpg")
                B3=B3.resize((150,150), Image.ANTIALIAS)
                self.photoB3=ImageTk.PhotoImage(B3)

                b3=Button(self.root,image=self.photoB3,cursor="hand2")
                b3.place(x=650,y=200,width=150,height=150)

                b3_text=Button(self.root,text="Attendance Details",cursor="hand2",font=("times new roman",12,"bold" ))
                b3_text.place(x=650,y=350,width=150,height=30)

                #Help Desk
                B4=Image.open(r"Images\helpdesk.jpg")
                B4=B4.resize((150,150), Image.ANTIALIAS)
                self.photoB4=ImageTk.PhotoImage(B4)

                b4=Button(self.root,image=self.photoB4,cursor="hand2")
                b4.place(x=900,y=200,width=150,height=150)

                b4_text=Button(self.root,text="Help Desk",cursor="hand2",font=("times new roman",12,"bold" ))
                b4_text.place(x=900,y=350,width=150,height=30)




                #Train Data
                B5=Image.open(r"Images\data.jpg")
                B5=B5.resize((150,150), Image.ANTIALIAS)
                self.photoB5=ImageTk.PhotoImage(B5)

                b5=Button(self.root,command=self.train_data,image=self.photoB5,cursor="hand2")
                b5.place(x=150,y=400,width=150,height=150)

                b5_text=Button(self.root,command=self.train_data,text="Train Data",cursor="hand2",font=("times new roman",12,"bold" ))
                b5_text.place(x=150,y=550,width=150,height=30)

                #Sample Photos
                B6=Image.open(r"Images\sample2.jpg")
                B6=B6.resize((150,150), Image.ANTIALIAS)
                self.photoB6=ImageTk.PhotoImage(B6)

                b6=Button(self.root,command=self.open_img,image=self.photoB6,cursor="hand2")
                b6.place(x=400,y=400,width=150,height=150)

                b6_text=Button(self.root,command=self.open_img,text="Sample Photos",cursor="hand2",font=("times new roman",12,"bold" ))
                b6_text.place(x=400,y=550,width=150,height=30)

                #Developer
                B7=Image.open(r"Images\dev.jpg")
                B7=B7.resize((150,150), Image.ANTIALIAS)
                self.photoB7=ImageTk.PhotoImage(B7)

                b7=Button(self.root,image=self.photoB7,cursor="hand2")
                b7.place(x=650,y=400,width=150,height=150)

                b7_text=Button(self.root,text="About Developer",cursor="hand2",font=("times new roman",12,"bold" ))
                b7_text.place(x=650,y=550,width=150,height=30)

                #exit
                B8=Image.open(r"Images\Exit.png")
                B8=B8.resize((150,150), Image.ANTIALIAS)
                self.photoB8=ImageTk.PhotoImage(B8)

                b8=Button(self.root,image=self.photoB8,cursor="hand2")
                b8.place(x=900,y=400,width=150,height=150)

                b8_text=Button(self.root,text="Exit",cursor="hand2",font=("times new roman",12,"bold" ))
                b8_text.place(x=900,y=550,width=150,height=30)

        def open_img(self):
                os.startfile("Data")


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












if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        

