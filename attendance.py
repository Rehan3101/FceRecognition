from operator import imod
from tkinter import*
from tkinter import ttk
import cv2
from time import strftime
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


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Attendance Details")

 #==================Variables=================
        self.var_stdntid=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar() 
        self.var_dep=StringVar()
        self.var_time=StringVar() 
        self.var_date=StringVar() 
        self.var_att=StringVar()         

 #background image

        bgimg=Image.open(r"Images\att4.jpg")
        bgimg=bgimg.resize((1400,650), Image.ANTIALIAS)
        self.photobgimg=ImageTk.PhotoImage(bgimg)

        f_lbl=Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=0,width=1400,height=650)

#Title
        title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Monaco",25,"bold" ),bg="lightgreen",fg="Black")
        title_lbl.place(x=40,y=0,width=1200,height=40) 

 #======Time=======

        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text= string)
                lbl.after(1000,time)   

        lbl=Label(self.root,font=('times new roman',14,'bold'),bg="white",fg='black')
        lbl.place(x=1150,y=20,width=110,height=30)
        time()    




    #leftframe
        left_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"),bg="lightblue")
        left_frame.place(x=50,y=230,width=550,height=380) 

        #Student ID
        id_label=Label(left_frame,text='Student ID:',font=("times new roman",12,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,pady=15,sticky=W)

        id_entry=ttk.Entry(left_frame,textvariable=self.var_stdntid,width="17",font=("times new roman",12,))
        id_entry.grid(row=0,column=1,padx=10,pady=15,sticky=W)

        #student Roll
        roll_label=Label(left_frame,text='Student Roll:',font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=15,sticky=W)

        roll_entry=ttk.Entry(left_frame,textvariable=self.var_roll,width="17",font=("times new roman",12,))
        roll_entry.grid(row=0,column=3,padx=10,pady=15,sticky=W)

        #Name
        name_label=Label(left_frame,text='Name:',font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=15,sticky=W)

        name_entry=ttk.Entry(left_frame,textvariable=self.var_name,width="17",font=("times new roman",12,))
        name_entry.grid(row=1,column=1,padx=10,pady=15,sticky=W)

        #department
        dep_label=Label(left_frame,text='Department:',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=15,sticky=W)

        dep_entry=ttk.Entry(left_frame,textvariable=self.var_dep,width="17",font=("times new roman",12,))
        dep_entry.grid(row=1,column=3,padx=10,pady=15,sticky=W)

        #Time
        time_label=Label(left_frame,text='Time:',font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=15,sticky=W)

        time_entry=ttk.Entry(left_frame,textvariable=self.var_time,width="17",font=("times new roman",12,))
        time_entry.grid(row=2,column=1,padx=10,pady=15,sticky=W)

        #Date
        date_label=Label(left_frame,text='Date:',font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=15,sticky=W)

        date_entry=ttk.Entry(left_frame,textvariable=self.var_date,width="17",font=("times new roman",12,))
        date_entry.grid(row=2,column=3,padx=10,pady=15,sticky=W)

        #Attendance Status
        status_label=Label(left_frame,text='Status:',font=("times new roman",12,"bold"),bg="white")
        status_label.grid(row=3,column=0,padx=10,pady=15,sticky=W)
        
        status_entry=ttk.Entry(left_frame,textvariable=self.var_att,width="17",font=("times new roman",12,))
        status_entry.grid(row=3,column=1,padx=10,pady=15,sticky=W)

        #buttonframe1
        b_frame=Frame(left_frame,bd=2,relief=RIDGE)
        b_frame.place(x=55,y=250,width=410,height=33)

        #Import CSV
        import_btn=Button(b_frame,command=self.importCsv,text="Import csv",width=14,font=("times new roman",12,"bold"),bg="orange",fg="Black")
        import_btn.grid(row=0,column=0)

        #Export CSV
        export_btn=Button(b_frame,command=self.exportCsv,text="Export csv",width=14,font=("times new roman",12,"bold"),bg="orange",fg="Black")
        export_btn.grid(row=0,column=1)

  

        #reset
        reset_btn=Button(b_frame,command=self.reset_data,text="Reset",width=14,font=("times new roman",12,"bold"),bg="orange",fg="Black")
        reset_btn.grid(row=0,column=2)




    #rightframe
        right_frame=LabelFrame(self.root,text="Attendance Details",bd=2,relief=RIDGE,font=("times new roman",12,"bold"),bg="white")
        right_frame.place(x=650,y=230,width=550,height=380)

      


    #Table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=538,height=353) 

        #scrollbars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

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

    #=======================Fetch Data Function============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    
    #import csv function
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 


    #export csv function
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False

            file_name=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Success","Your Data is exported to" +os.path.basename(file_name)+ "successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)

    #=======Get cursor============
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_stdntid.set(rows[0])   
        self.var_roll.set(rows[1])  
        self.var_name.set(rows[2])  
        self.var_dep.set(rows[3])  
        self.var_time.set(rows[4])  
        self.var_date.set(rows[5])  
        self.var_att.set(rows[6]) 


    #reset function
    def reset_data(self):
        self.var_stdntid.set("")   
        self.var_roll.set("")  
        self.var_name.set("")  
        self.var_dep.set("")  
        self.var_time.set("")  
        self.var_date.set("")  
        self.var_att.set("")

        
               

        






if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        