from distutils.cmd import Command

from tkinter import*
from  tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from email.charset import add_alias
from cse1 import course4
from student import students
from result import results
from view import viewresults
from contact import feed
#from frontpage import mainpage1

def main1():
  win=Tk()
  app=loginadmin(win)
  win.mainloop()


class loginadmin:
  
    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")

      img4=Image.open(r"images\71.jpg")
      img4=img4.resize((1530,830),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
      
   

      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
      lbltitle=Label(bg_lbl,relief=RIDGE,text="Admin Login Page ",font=("courier new",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1530,height=60)
      frame=Frame(self.root,bg="black")
      frame.place(x=580,y=556,width=450,height=280)
      img5=Image.open(r"images\61.jpg")
      img5=img5.resize((70,70),Image.Resampling.LANCZOS)
      self.photoimg5=ImageTk.PhotoImage(img5)
      lblimg5=Label(frame,image=self.photoimg5,bg="black",borderwidth=0)
      lblimg5.place(x=190,y=5,width=70,height=70)

      letsstart=Label(frame,text=" Admin Sign Up ",font=("times new roman",22,"bold"),fg="skyblue",bg="black")
      letsstart.place(x=110,y=80)

      #label
      userlbl=Label(frame,text="Username :",font=("times new roman",18,"bold"),fg="red",bg="black")
      userlbl.place(x=70,y=120)
      self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
      self.txtuser.place(x=200,y=125,width=200)

      passwordlbl=Label(frame,text="Password :",font=("times new roman",18,"bold"),fg="red",bg="black")
      passwordlbl.place(x=70,y=165)
      self.txtpassword=ttk.Entry(frame,font=("times new roman",14,"bold"))
      self.txtpassword.place(x=200,y=165,width=200)


      img6=Image.open(r"images\60.jpg")
      img6=img6.resize((30,30),Image.Resampling.LANCZOS)
      self.photoimg6=ImageTk.PhotoImage(img6)
      lblimg6=Label(frame,image=self.photoimg5,bg="black",borderwidth=0)
      lblimg6.place(x=25,y=121,width=30,height=30)

      img6=Image.open(r"images\59.jpg")
      img6=img6.resize((30,30),Image.Resampling.LANCZOS)
      self.photoimg6=ImageTk.PhotoImage(img6)
      lblimg6=Label(frame,image=self.photoimg5,bg="black",borderwidth=0)
      lblimg6.place(x=25,y=163,width=30,height=30)
     
      loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",18,"bold"),bd=3,relief=RIDGE,fg="black",bg="skyblue",activeforeground="black",activebackground="skyblue")
      loginbtn.place(x=50,y=220,width=120,height=35)
      registerbtn=Button(frame,command=self.registerwindow,text="New User Register",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      registerbtn.place(x=230,y=210,width=170,height=35)
      paswordbtn=Button(frame,text="Forgot Password ",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      paswordbtn.place(x=230,y=240,width=170,height=35)
    
    def registerwindow(self):
      self.newwindow=Toplevel(self.root)
      self.app=register1(self.newwindow)

    def login(self):
        if row==None:
          messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
        else:
          openmin=messagebox.askyesno("YesNo","Access Only Admin",parent=self.root)
          if openmin>0:
            self.newwindow=Toplevel(self.newwindow)
            self.app=Student(self.newwindow)
          else:
            if not openmin:
              return 
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
      
        
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
          cur=conn.cursor()
        cur.execute("select * from adminregister where username=%s and password =%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpassword.get()
                                                                                          ))
        row=cur.fetchone()
        
        conn.commit()
        conn.close()



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
      b2=Button(frame,command=self.destroy,image=self.photoimg2,borderwidth=0,cursor="hand2",bg="white")
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
    def destroy(self):
      self.root.destroy()


class Student:

    def __init__(self,root):
        self.root=root
        self.root.title("Students Academic Record")
        self.root.geometry("1550x830+0+0")
        self.root.config(bg="white")
       #icons
       
        lbltitle=Label(self.root,relief=RIDGE,text="STUDENT'S  ACADEMIC  RECORD ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
        lbltitle.place(x=0,y=0,width=1530,height=60)
        img4=Image.open(r"images\72.jpg")
        img4=img4.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=60,width=1530,height=770)
        bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=60,width=1530,height=770)

        M_Frame=LabelFrame(self.root,bg="black")
        M_Frame.place(x=10,y=70,width=1520,height=80)
        btn_course=Button(M_Frame,text="Course",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course)
        btn_course.place(x=40,y=15,width=200,height=50)
        btn_student=Button(M_Frame,text="Student",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student)
        btn_student.place(x=300,y=15,width=200,height=50)
        btn_result=Button(M_Frame,text="Result",font=("",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result)
        btn_result.place(x=550,y=15,width=200,height=50)
        btn_view=Button(M_Frame,text="View",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_view)
        btn_view.place(x=800,y=15,width=200,height=50)
        btn_feedback=Button(M_Frame,text="Contact",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_feedback)
        btn_feedback.place(x=1050,y=15,width=200,height=50)
        btn_logout=Button(M_Frame,text="Logout",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=1300,y=15,width=200,height=50)
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=course4(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=students(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=results(self.new_win)

    def add_view(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=viewresults(self.new_win)

    def add_feedback(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=feed(self.new_win)
    def logout(self):
      self.root.destroy()

    
      
   


   
   
if __name__ == "__main__":
  main1()