from tkinter import*
from tkinter import ttk
import cv2
from turtle import bgcolor
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
from django.db import DatabaseError
import mysql.connector


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Student Details")

        #=========Variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stdid=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_dep=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
 #bgcolor
        bg_color=Label(self.root,bg="lightpink")
        bg_color.place(x=0,y=0,width=1400,height=650)

#centre image
        img1=Image.open(r"Images\sms2.jpg")
        img1=img1.resize((400,140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=425,y=0,width=400,height=140)



#ryt corner image
        img2=Image.open(r"Images\sms7.png")
        img2=img2.resize((450,140), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=825,y=0,width=450,height=140)



#left corner image

        
        img3=Image.open(r"Images\sms6.jpg")
        img3=img3.resize((450,140), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=440,height=140)

       

 #Title
        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSYTEM",font=("times new roman",25,"bold" ),fg="darkgreen")
        title_lbl.place(x=40,y=145,width=1200,height=40)

 #Frames

        #mainframe
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=10,y=190,width=1255,height=450)

    #leftframe
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=610,height=435)

    #currentcourse
        curr_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        curr_frame.place(x=5,y=2,width=590,height=100)

        #department
        dep_label=Label(curr_frame,text='Department:',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(curr_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=15)
        dep_combo["values"]=("Select Department","CSE","IT","ECE","Mechanical","Electrical","EN")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #course
        course_label=Label(curr_frame,text='Course:',font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(curr_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=15)
        course_combo["values"]=("Select Course","B.tech","M.tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Year
        year_label=Label(curr_frame,text='Year:',font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(curr_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=15)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(curr_frame,text='Semester:',font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(curr_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=15)
        sem_combo["values"]=("Select Semester","Sem-1","Sem-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


    #Student Class information
        cs_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Class Information",font=("times new roman",12,"bold"))
        cs_frame.place(x=5,y=112,width=590,height=295)

        #Student ID
        id_label=Label(cs_frame,text='Student ID:',font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(cs_frame,textvariable=self.var_stdid,width="17",font=("times new roman",12,))
        id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        name_label=Label(cs_frame,text='Student Name:',font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(cs_frame,textvariable=self.var_stdname,width="17",font=("times new roman",12,))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class div
        class_label=Label(cs_frame,text='Class Division:',font=("times new roman",12,"bold"),bg="white")
        class_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_combo=ttk.Combobox(cs_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=15)
        class_combo["values"]=("A","B","C","D")
        class_combo.current(0)
        class_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        roll_label=Label(cs_frame,text='Roll No:',font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(cs_frame,textvariable=self.var_roll,width="17",font=("times new roman",12,))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(cs_frame,text='Gender:',font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(cs_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(cs_frame,text='DOB:',font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(cs_frame,textvariable=self.var_dob,width="17",font=("times new roman",12,))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(cs_frame,text='Email:',font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(cs_frame,textvariable=self.var_email,width="17",font=("times new roman",12,))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        no_label=Label(cs_frame,text='Phone No:',font=("times new roman",12,"bold"),bg="white")
        no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        no_entry=ttk.Entry(cs_frame,textvariable=self.var_phone,width="17",font=("times new roman",12,))
        no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        add_label=Label(cs_frame,text='Address:',font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(cs_frame,textvariable=self.var_address,width="17",font=("times new roman",12,))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        Tname_label=Label(cs_frame,text='Teacher Name:',font=("times new roman",12,"bold"),bg="white")
        Tname_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Tname_entry=ttk.Entry(cs_frame,textvariable=self.var_teacher,width="17",font=("times new roman",12,))
        Tname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiob1=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiob1.grid(row=5,column=0)

        radiob2=ttk.Radiobutton(cs_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiob2.grid(row=5,column=1)

        #buttonframe1
        b_frame=Frame(cs_frame,bd=2,relief=RIDGE)
        b_frame.place(x=5,y=200,width=578,height=33)

        #Save
        save_btn=Button(b_frame,command=self.add_data,text="Save",width=15,font=("times new roman",12,"bold"),bg="lightblue",fg="Black")
        save_btn.grid(row=0,column=0)

        #Update
        Update_btn=Button(b_frame,command=self.update_data,text="Update",width=15,font=("times new roman",12,"bold"),bg="lightblue",fg="Black")
        Update_btn.grid(row=0,column=1)

        #Delete
        del_btn=Button(b_frame,command=self.delete_data,text="Delete",width=15,font=("times new roman",12,"bold"),bg="Lightblue",fg="Black")
        del_btn.grid(row=0,column=2)

        #reset
        reset_btn=Button(b_frame,command=self.reset_data,text="Reset",width=15,font=("times new roman",12,"bold"),bg="lightblue",fg="Black")
        reset_btn.grid(row=0,column=3)


        #buttonFrame2
        b_frame2=Frame(cs_frame,bd=2,relief=RIDGE)
        b_frame2.place(x=5,y=233,width=578,height=33)

        #take photo sample
        sam1_btn=Button(b_frame2,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman",12,"bold"),bg="orange",fg="Black")
        sam1_btn.grid(row=0,column=0)

        #Update photo Sample
        up_btn=Button(b_frame2,text="Update Photo Sample",width=31,font=("times new roman",12,"bold"),bg="orange",fg="Black")
        up_btn.grid(row=0,column=1)



#rightframe
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=5,width=610,height=430)

#Search System
        ss_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        ss_frame.place(x=5,y=2,width=590,height=70)


        #search
        search_label=Label(ss_frame,text='Search By:',font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(ss_frame,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_entry=ttk.Entry(ss_frame,width="15",font=("times new roman",12,))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(ss_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="Lightblue",fg="Black")
        search_btn.grid(row=0,column=3,padx=5)

        show_btn=Button(ss_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="Lightblue",fg="Black")
        show_btn.grid(row=0,column=4,padx=5)

    #Table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=80,width=590,height=320)

        #scrollbars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","ID","Name","Div","Roll","Gender","DOB","email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("Roll",text="Roll NO")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)
    


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #===============Function Declaration===============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rehan@2002",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stdid.get(),
                                                                                                        self.var_stdname.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        
                
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)    
   
   
    #===============Data Fetch Function===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rehan@2002",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 


    #=====================Get Cursor=====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stdid.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #========Update Function==========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rehan@2002",database="face_recogniser")
                    my_cursor=conn.cursor()  
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                                 
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stdname.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_stdid.get()
                                                                                                        ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data
                conn.close()                                                                                                  
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #====Delete Function=======
    def delete_data(self):
        if self.var_stdid.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete page","Do you want to delete this Student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rehan@2002",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_stdid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)            

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #===Reset Data====
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stdid.set("")
        self.var_stdname.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #==============Generate data Set or Take Photo Sample========
    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_stdname.get()=="" or self.var_stdid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
         else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rehan@2002",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                                 
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_stdname.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_stdid.get()==id+1
                                                                                                                            ))    
                conn.commit()
                self.fetch_data()
                self.reset_data
                conn.close()
# ============ Load Predefined Data on Face frontals from OpenCV============

                face_classfier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classfier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbour=5
                     
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data seys Completed!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

               










if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()