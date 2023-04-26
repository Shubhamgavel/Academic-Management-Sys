from tkinter import *
from  tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class register1:
    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")

      self.varfname=StringVar()
      self.varlname=StringVar()
      self.varcontact=StringVar()
      self.varusername=StringVar()
      self.varsecurityquestion=StringVar()
      self.varsecurityanswer=StringVar()
      self.varpassword=StringVar()
      self.varconfirmpassword=StringVar()

      img4=Image.open(r"images\30.jpg")
      img4=img4.resize((1530,830),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
   

      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

      frame=Frame(self.root,bg="white")
      frame.place(x=320,y=200,width=890,height=480)

      lblregister=Label(frame,text="REGISTER  HERE",font=("times new roman",22,"bold"),bg="white",fg="green")
      lblregister.place(x=320,y=10)

      fname=Label(frame,text="First Name    : ",font=("times new roman",20,"bold"),bg="white")
      fname.place(x=10,y=60)
      self.ename=ttk.Entry(frame,textvariable=self.varfname,font=("times new roman",20))
      self.ename.place(x=190,y=60,width=200)

      lname=Label(frame,text="Last Name  : ",font=("times new roman",20,"bold"),bg="white")
      lname.place(x=10,y=120)
      self.e1name=ttk.Entry(frame,textvariable=self.varlname,font=("times new roman",20))
      self.e1name.place(x=190,y=120,width=200)

      contact=Label(frame,text="Contact No.  : ",font=("times new roman",20,"bold"),bg="white")
      contact.place(x=10,y=180)
      self.cname=ttk.Entry(frame,textvariable=self.varcontact,font=("times new roman",20))
      self.cname.place(x=190,y=180,width=200)

      email=Label(frame,text="Username : ",font=("times new roman",20,"bold"),bg="white")
      email.place(x=10,y=240)
      self.emailname=ttk.Entry(frame,textvariable=self.varusername,font=("times new roman",20))
      self.emailname.place(x=190,y=240,width=200)

      security=Label(frame,text="Security  Questions : ",font=("times new roman",18,"bold"),bg="white")
      security.place(x=440,y=60)
      
    
      self.securityname=ttk.Combobox(frame,textvariable=self.varsecurityquestion,font=("times new roman",13),width=20,state="readonly")
      self.securityname["value"]=("Select Questions","Your Idle","Your DOB","Your College Name","Your Favorite Singer","Your Best Friend")
      self.securityname.current(0)
      self.securityname.place(x=670,y=60)

      answer=Label(frame,text="Security Answer  : ",font=("times new roman",18,"bold"),bg="white")
      answer.place(x=440,y=120)
      self.answername=ttk.Entry(frame,textvariable=self.varsecurityanswer,font=("times new roman",20))
      self.answername.place(x=670,y=120,width=200)

      password=Label(frame,text="Password  : ",font=("times new roman",18,"bold"),bg="white")
      password.place(x=440,y=180)
      self.passwordrname=ttk.Entry(frame,textvariable=self.varpassword,font=("times new roman",20))
      self.passwordrname.place(x=670,y=180,width=200)

      confirmpassword=Label(frame,text="Confirm Password  : ",font=("times new roman",18,"bold"),bg="white")
      confirmpassword.place(x=440,y=240)
      self.confirmpasswordname=ttk.Entry(frame,textvariable=self.varconfirmpassword,font=("times new roman",20))
      self.confirmpasswordname.place(x=670,y=240,width=200)
      self.varcheck=IntVar()
      checkbtn=Checkbutton(frame,variable=self.varcheck,text="I Agree The Terms & Coditions",font=("times new roman",18,"bold"),bg="white",fg="red",onvalue=1,offvalue=0)
      checkbtn.place(x=30,y=320)

      img1=Image.open(r"images\63.png")
      img1=img1.resize((140,50),Image.Resampling.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)
      b1=Button(frame,command=self.registerdata,image=self.photoimg1,borderwidth=0,cursor="hand2",bg="white")
      b1.place(x=50,y=380)

      img2=Image.open(r"images\62.jpg")
      img2=img2.resize((140,50),Image.Resampling.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      b2=Button(frame,command=self.loginwindow,image=self.photoimg2,borderwidth=0,cursor="hand2",bg="white")
      b2.place(x=220,y=380)

      img3=Image.open(r"images\64.jpg")
      img3=img3.resize((430,150),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)
      img3=Label(frame,image=self.photoimg3,borderwidth=0,bg="white")
      img3.place(x=440,y=320)
    #  
    def registerdata(self):

      if self.varfname.get()=="" or self.varusername.get()=="" or self.varsecurityquestion.get()=="Security  Questions":
        messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.varpassword.get()!=self.varconfirmpassword.get():
        messagebox.showerror("Error","Password Must Be Same",parent=self.root)
      elif self.varcheck.get()==0:
        messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from adminregister where username=%s")
        value=(self.varusername.get(),)
        cur.execute(query,value)
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","User Already Exist ... Please Try Another Username",parent=self.root)
        else:
          cur.execute("insert into adminregister values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.varfname.get(),
                                                                                  self.varlname.get(),
                                                                                  self.varcontact.get(),
                                                                                  self.varusername.get(),
                                                                                  self.varsecurityquestion.get(),
                                                                                  self.varsecurityanswer.get(),
                                                                                  self.varpassword.get()
                                                                                   ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Registered Successfully",parent=self.root)

    def loginwindow(self):
      self.root.destroy()
      


   
    

if __name__ == "__main__":
  root=Tk()
  obj=register1(root)
  root.mainloop()