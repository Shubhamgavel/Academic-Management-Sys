from codeop import CommandCompiler
from symtable import Class
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os


class viewresults:

   def  __init__(self,root):

      self.root=root
      self.root.title("Students Academic Record")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")
      self.varroll=StringVar()

      

      

      img4=Image.open(r"images\47.jpg")
      img4=img4.resize((1530,830),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=0,width=1530,height=830)
      

      lbltitle=Label(bg_lbl,relief=RIDGE,text="VIEW  RESULT ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1530,height=60)

      
      dataleftframe=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=2,bg="white")

    
      dataleftframe.place(x=400,y=75,width=800,height=50)
        #ROLL     #############################
      lblroll=Label(dataleftframe,text=" Enter  Roll  no.   :",font=("times new roman",18,"bold"),bg="white",fg="blue")
      lblroll.grid(row=0,column=0,padx=4,pady=3,sticky=W)

      lblroll.place(x=40,y=5)

      rollentry=ttk.Entry(dataleftframe,textvariable=self.varroll,font=("times new roman",18,"bold"),width=18)

      rollentry.grid(row=0,column=1,padx=2,pady=3,sticky=W)
   
      rollentry.place(x=250,y=5)
      btnsearch=Button(dataleftframe,command=self.fetchresult,text="Search",font=("times new roman",13,"bold"),width=10,fg="black",bg="skyblue",activebackground="skyblue",activeforeground="black")
      btnsearch.grid(row=0,column=2,sticky=W,padx=8,pady=3)
      btnsearch.place(x=500,y=5)

      lbltitle2=Button(dataleftframe,command=self.logout,text="Exit",font=("courier new",13,"bold"),width=10,fg="black",bg="skyblue",activebackground="skyblue",activeforeground="black")
     
      lbltitle2.grid(row=0,column=3,sticky=W,padx=8,pady=3)
      lbltitle2.place(x=640,y=5)

   def fetchresult(self):
        if self.varroll.get()=="":
            messagebox.showerror("Error","Please Enter Roll no.",parent=self.root)
        else:
          conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
          mycursor=conn.cursor()
          query=("select name from  result where roll=%s")
          value=(self.varroll.get(),)
          mycursor.execute(query,value)
          row=mycursor.fetchone()

          if row==None:
             messagebox.showerror("Error","Roll no. is not valid",parent=self.root)
          else:
             conn.commit()
             conn.close()

             showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2,bg="skyblue")
             showdataframe.place(x=400,y=136,width=800,height=690)

             lblname=Label(showdataframe,text="Name      :",font=("times new roman",22,"bold"),bg="skyblue")
             lblname.place(x=15,y=5)
             lbl=Label(showdataframe,text=row,font=("times new roman",19,"bold"),bg="skyblue",fg="brown")
             lbl.place(x=155,y=8)
             ####2############################## ####2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select roll from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Roll  No.       :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=500,y=5)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=5)
             
              ####3##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select uniqueid from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Unique I'd  :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=15,y=50)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=160,y=50)
             
              ####4##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select gender from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Gender         :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=500,y=50)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=50)
             
              ####5##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select dob from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="D.O.B         :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=15,y=90)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=160,y=90)
             
              ####6##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select courseid from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Course I'd    :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=500,y=90)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=90)
              ####7##############################
             
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select mobile from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Mobile        :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=15,y=130)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=160,y=130)
             
              ####8            ##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select course from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Course          :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=500,y=130)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=130)
              ####9##############################
             
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select address from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Address      :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=15,y=170)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=160,y=170)
             
              ####10##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select year from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Year              :",font=("times new roman",17,"bold"),bg="skyblue")
             lblroll.place(x=500,y=170)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=170)

             lblsubjects=Label(showdataframe,text="Subjects ",font=("times new roman",18,"bold"),bg="skyblue",fg="red")
             lblsubjects.place(x=60,y=230)
             lblmarks=Label(showdataframe,text=" Obtained Marks",font=("times new roman",18,"bold"),bg="skyblue",fg="red")
             lblmarks.place(x=390,y=230)
             lblmarks=Label(showdataframe,text=" Full  Marks",font=("times new roman",18,"bold"),bg="skyblue",fg="red")
             lblmarks.place(x=620,y=230)
              ####subject 1##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject1 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=290)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m1 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=290)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=290)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject2 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=330)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m2 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=330)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=330)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject3 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=370)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m3 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=370)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=370)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject4 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=410)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m4 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=410)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=410)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject5 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=450)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m5 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=450)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=450)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select subject6 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=15,y=490)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select m6 from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=470,y=490)
             ####marks##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select totalmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=660,y=490)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select fullmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Total  Marks                     : ",font=("times new roman",17,"bold"),bg="skyblue",fg="red")
             lblroll.place(x=5,y=540)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=280,y=540)
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select obtainedmarks from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Total Obtained Marks     : ",font=("times new roman",17,"bold"),bg="skyblue",fg="red")
             lblroll.place(x=5,y=580)
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=280,y=580)

            
             ####subject 2##############################
             conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
             mycursor=conn.cursor()
             query=("select percentage from  result where roll=%s")
             value=(self.varroll.get(),)
             mycursor.execute(query,value)
             row=mycursor.fetchone()
             lblroll=Label(showdataframe,text="Percentage                       : ",font=("times new roman",17,"bold"),bg="skyblue",fg="red")
             lblroll.place(x=5,y=620) 
             lblroll=Label(showdataframe,text="%",font=("times new roman",17),bg="skyblue")
             lblroll.place(x=315,y=620) 
             lbl1=Label(showdataframe,text=row,font=("times new roman",18,),bg="skyblue")
             lbl1.place(x=280,y=620)
             





   
        
                
   def logout(self):
        self.root.destroy()
      
if __name__ == "__main__":
   root=Tk()
   obj=viewresults(root)
   root.mainloop()
