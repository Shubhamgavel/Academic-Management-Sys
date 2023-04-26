from codeop import CommandCompiler
from symtable import Class
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os


class feed:

  def  __init__(self,root):

       self.root=root
       self.root.title("Students Academic Record")
       self.root.geometry("1530x830+0+0")
       self.root.config(bg="#0b5377")
       lbltitle=Label(self.root,relief=RIDGE,text="Contact  Us ",font=("courier new",37,"bold"),fg="skyblue",bg="black")
       lbltitle.place(x=0,y=0,width=1530,height=60)

       lbltitle1=Label(self.root,relief=RIDGE,text=" ***  Thank  You  For  Visiting  Us  *** ",font=("courier new",32,"bold"),fg="skyblue",bg="black")
       lbltitle1.place(x=190,y=767,width=1130,height=50)
       lbltitle2=Button(self.root,command=self.logout,text="Exit",font=("times new roman",20,"bold"),fg="black",bg="#0b5377",activebackground="#0b5377",activeforeground="black")
       lbltitle2.place(x=1370,y=780,width=100,height=30)

       lbl1=Label(self.root,relief=RIDGE,bg="black")

       lbl1.place(x=20,y=80,width=380,height=670)
       lbl2=Label(lbl1,text="Submitted  By ",font=("times new roman",29,"bold"),fg="skyblue",bg="black")
       lbl2.place(x=65,y=20)
       img4=Image.open(r"images\IMG_20221221_231157.JPG")
       img4=img4.resize((330,400),Image.Resampling.LANCZOS)
       self.photoimg4=ImageTk.PhotoImage(img4)
       img4=Label(lbl1,image=self.photoimg4,bd=5,relief=RIDGE)
       img4.place(x=25,y=90,width=330,height=400)
       lbl5=Label(lbl1,relief=RIDGE,bg="#d9b2ff")
       lbl5.place(x=25,y=505,width=330,height=130)
       lbl6=Label(lbl5,text=" Vinayak Patel ",font=("times new roman",25,"bold"),fg="black",bg="#d9b2ff")
       lbl6.place(x=65,y=0)
       lbl7=Label(lbl5,text=" (  Bca 6th sem )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl7.place(x=65,y=40)
       lbl8=Label(lbl5,text=" ( Roll No: 130410421025 )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl8.place(x=3,y=80)
       
       lbl3=Label(self.root,relief=RIDGE,bg="black")
       lbl3.place(x=440,y=80,width=1070,height=670)
       lbl4=Label(lbl3,text="Guided  By ",font=("times new roman",30,"bold"),fg="skyblue",bg="black")
       lbl4.place(x=390,y=15)
       img5=Image.open(r"images\Dr. Satya Prakash Makhija.jpg")
       img5=img5.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg5=ImageTk.PhotoImage(img5)
       img5=Label(lbl3,image=self.photoimg5,bd=5,relief=RIDGE)
       img5.place(x=25,y=90,width=320,height=400)
       lbl12=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl12.place(x=25,y=505,width=320,height=130)
       lbl9=Label(lbl12,text="Dr. Satya Prakash Makhija",font=("times new roman",19,"bold"),fg="black",bg="#d9b2ff")
       lbl9.place(x=15,y=0)
       lbl10=Label(lbl12,text=" ( HOD  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl10.place(x=95,y=40)
       lbl11=Label(lbl12,text=" ( SER Branch )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl11.place(x=57,y=80)


       img6=Image.open(r"images\Dr. Puja Shrivastava.jpg")
       img6=img6.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg6=ImageTk.PhotoImage(img6)
       img6=Label(lbl3,image=self.photoimg6,bd=3,relief=RIDGE)
       img6.place(x=375,y=90,width=320,height=400)
       lbl13=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl13.place(x=375,y=505,width=320,height=130)
       lbl14=Label(lbl13,text="Dr. Puja Shrivastava",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl14.place(x=30,y=0)
       lbl15=Label(lbl13,text=" (  Asst.  Prof.  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl15.place(x=55,y=40)
       lbl16=Label(lbl13,text=" ( SER Branch)",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl16.place(x=57,y=80)


       img7=Image.open(r"images\Shahnawaz Ansari Mentor SER Branch.jpg")
       img7=img7.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg7=ImageTk.PhotoImage(img7)
       img7=Label(lbl3,image=self.photoimg7,bd=5,relief=RIDGE)
       img7.place(x=725,y=90,width=320,height=400)
       lbl17=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl17.place(x=725,y=505,width=320,height=130)
       lbl18=Label(lbl17,text="Shahnawaz Ansari",font=("times new roman",23,"bold"),fg="black",bg="#d9b2ff")
       lbl18.place(x=47,y=0)
       lbl19=Label(lbl17,text=" (  Mentor  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl19.place(x=95,y=40)
       lbl20=Label(lbl17,text=" ( SER Branch )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl20.place(x=67,y=80)

  def logout(self):
        self.root.destroy()
    
      

       
       
       
    
       


if __name__ == "__main__":
    root=Tk()
    obj=feed(root)
    root.mainloop()