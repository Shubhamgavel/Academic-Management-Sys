from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os
from adminlogin import loginadmin
from studentlogin import loginstudent


class mainpage1:
    def  __init__(self,root):

      self.root=root
      self.root.title("Students Academic Record")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")
      lbltitle=Label(self.root,relief=RIDGE,text="WELCOME  TO  MY PROJECT ",font=("courier new",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1530,height=60)

      img=Image.open(r"images\itm6.jpg")  
      img=img.resize((1550,830),Image.Resampling.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)
      lbl_bg1=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
      lbl_bg1.place(x=0,y=61,relwidth=1,relheight=1)
      
      
      
      btn_course=Button(lbl_bg1,command=self.add_home,text="Admin  Login",font=("times new roman",18,"bold"),bg="skyblue",fg="black",cursor="hand2",activebackground="skyblue",activeforeground="black")
      btn_course.place(x=1070,y=25,width=200,height=40)
      btn_student=Button(lbl_bg1,command=self.student,text="Student  Login",font=("Times new roman",18,"bold"),bg="skyblue",fg="black",cursor="hand2",activebackground="skyblue",activeforeground="black")
      btn_student.place(x=1300,y=25,width=200,height=40)
      btn_exit=Button(lbl_bg1,command=self.exit,text="Exit",font=("Times new roman",18,"bold"),bg="skyblue",fg="black",cursor="hand2",activebackground="skyblue",activeforeground="black")
      btn_exit.place(x=1235,y=75,width=100,height=40)

    def exit(self):
      self.root.destroy()


    def add_home(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=loginadmin(self.new_win)

    def student(self):
      
        self.new_win=Toplevel(self.root)
        self.new_obj=loginstudent(self.new_win)
 


      

    
 
 


if __name__ == "__main__":
    root=Tk()
    obj=mainpage1(root)
    root.mainloop()