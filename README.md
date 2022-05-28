# FceRecognition

#Introduction

1. It is basically an attendance system project which uses **"Face Recognition"** to record attendance.
2. It also consist **Student Management** System using MYsql database connected with aws cloud.
3. It is developed by python3.10 using vscode.


#Requirements
1. High Speed Internet Connectivity(login system is cloud database based)
2. RAM=8Gb
3. screen size= 1400x650(size greater than it can cause changes in UI as it is a desktop application(have a fixed geometry))
4. Take Sample from the camera in laptop(not webcam).
changes to do use web cam:
1. studentdetails.py line 536         //{cap=cv2.VideoCapture(0)} change 0 to 1 to use webcam     
2. face_recognition.py line 160


#Recomended Modules
1. tkinter, tkcalender
2. Face Recognition Module,  //git clone https://github.com/ageitgey/face_recognition.git
3. OpenCV// if errors shows for cv2 attribute face use **pip install opencv-contrib-python** and restart system.
4. Pillow 
5. MySQL connector


#Installation

clone the full folder and just run the login.py file.


#Configuration

Login by first registering yourself in new user register button and using Email and password to login.


![Login_Page](https://user-images.githubusercontent.com/105501094/170836843-5af7f1b0-8081-4d8f-b68d-6132531e8990.jpg)



the home screen will be available with 8 buttons. Follow the steps to start your app experience:


![Screenshot 2022-05-25 005303](https://user-images.githubusercontent.com/105501094/170267800-a07c15d7-e381-4943-85bc-4db36b9ba0d8.jpg)





Steps:

1. Click on "student details button", Fill all the details and click on **save** button, then click on **Take sample photo** to take sample.



![studentdetailspage](https://user-images.githubusercontent.com/105501094/170836975-ea9b45a6-5b0e-4f4a-8162-b442e627ac56.jpg)



2. **Proper light should be there while camera takes sample**, close the window after sample is taken aur return to home window.
3. Click on **train data** button and train the sample. close the window and click on **Face Recognition button**.
4. click on Recognize face and wait till camera opens and recognize you on the details you mentioned earlier.
5. close the camera window using **enter**. Close and return to home window.
6. Open the **Attendance details** window and click on **import csv**, then import the **"Attendance.csv"** file.

 

![attendance details](https://user-images.githubusercontent.com/105501094/170837132-12b532fc-4be1-4d80-b471-9a7664e42387.jpg)



7. your attendance is visible, you can also export the details and make a new csv file by export button.
8. you can update and delete database in **"Student Details"** by the given buttons.
9. Can access the other buttons for **About developer, support and a exit button**.



