from tkinter import*
from tkinter import ttk
import cv2
from turtle import bgcolor
from PIL import Image,ImageTk
from cv2 import IMREAD_REDUCED_GRAYSCALE_2
from tkinter import messagebox
from django.db import DatabaseError
import mysql.connector


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x650+0+0")
        self.root.title("Attendance Details")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()        