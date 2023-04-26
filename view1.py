from codeop import CommandCompiler
from symtable import Class
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os


class views1:

   def  __init__(self,root):

      self.root=root
      self.root.title("Students Academic Record")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")
      self.varroll=StringVar()
      lbltitle=Label(relief=RIDGE,text="  ** *** *** **  VIEW    RESULT  ** *** *** **   ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1530,height=60)
      img4=Image.open(r"images\47.jpg")
      img4=img4.resize((1530,770),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=60,width=1530,height=770)


if __name__ == "__main__":
    root=Tk()
    obj=views1(root)
    root.mainloop()