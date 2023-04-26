from cProfile import label
from tkinter import*
from  tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from view import viewresults
from contact import feed
from feed1 import feedbacknew
from newcourse import newc

from student import students
from rslt1 import result1
from view import viewresults
from contact import feed

def main():
  win=Tk()
  app=loginstudent(win)
  win.mainloop()


class loginstudent:
  
    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")

      img4=Image.open(r"images\334.jpg")
      img4=img4.resize((1530,830),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
      
   

      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
      lbltitle=Label(bg_lbl,relief=RIDGE,text="Student Login Page ",font=("courier new",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1530,height=60)
      frame=Frame(self.root,bg="black")
      frame.place(x=580,y=530,width=430,height=370)
      img5=Image.open(r"images\61.jpg")
      img5=img5.resize((70,70),Image.Resampling.LANCZOS)
      self.photoimg5=ImageTk.PhotoImage(img5)
      lblimg5=Label(frame,image=self.photoimg5,bg="black",borderwidth=0)
      lblimg5.place(x=190,y=5,width=70,height=70)

      letsstart=Label(frame,text="Student  Sign  In",font=("times new roman",22,"bold"),fg="skyblue",bg="black")
      letsstart.place(x=110,y=80)

      #label
      userlbl=Label(frame,text="Username :",font=("times new roman",18,"bold"),fg="red",bg="black")
      userlbl.place(x=70,y=120)
      self.txtuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
      self.txtuser.place(x=200,y=125,width=200)

      passwordlbl=Label(frame,text="Password :",font=("times new roman",18,"bold"),fg="red",bg="black")
      passwordlbl.place(x=70,y=165)
      self.txtpassword=ttk.Entry(frame,show="*",font=("times new roman",14,"bold"))
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
      loginbtn.place(x=25,y=245,width=80,height=35)
      exitbtn=Button(frame,command=self.exit,text="Exit",font=("times new roman",18,"bold"),bd=3,relief=RIDGE,fg="black",bg="skyblue",activeforeground="black",activebackground="skyblue")
      exitbtn.place(x=120,y=245,width=80,height=35)
      registerbtn=Button(frame,command=self.registerwindow,text="New User Register",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      registerbtn.place(x=230,y=230,width=170,height=35)
      paswordbtn=Button(frame,command=self.forgotpass,text="Forgot Password ",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      paswordbtn.place(x=230,y=260,width=170,height=35)

      checkbtn=Checkbutton(frame,command=self.showpassword,text="Show Password",font=("times new roman",15),fg="skyblue",bg="black",activeforeground="skyblue",activebackground="black")
      checkbtn.place(x=190,y=200)

    def showpassword(self):
      if self.txtpassword.cget('show')=="*":
        self.txtpassword.config(show='')
      else:
        self.txtpassword.config(show='*')

    def registerwindow(self):
      self.newwindow=Toplevel(self.root)
      self.app=register1(self.newwindow)
    
    def exit(self):
      self.root.destroy()

    def resetpass(self):
      if self.securityname2.get=="Select Questions":
        messagebox.showerror("Error","select Security questions",parent=self.root2)
      elif self.answername2.get()=="":
        messagebox.showerror("error","Please entere the answer",parent=self.root2)
      elif self.newpassname2.get()=="":
        messagebox.showerror("error","Please Enter th new passsword",parent=self.root2)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from studentlogin where username2=%s and securityquestion2=%s and securityanswer2=%s")
        value=(self.txtuser.get(),self.securityname2.get(),self.answername2.get())
        cur.execute(query,value)
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("error","please enter the correct answer",parent=self.root2)
        else:
          query=("update studentlogin set password2=%s where username2=%s")
          value=(self.newpassname2.get(),self.txtuser.get())
          cur.execute(query,value)
          conn.commit()
          conn.close()
          messagebox.showinfo("info","your password is been reset",parent=self.root2)

    def clr(self):
      self.root2.destroy()


    def forgotpass(self):
      if self.txtuser.get()=="":
        messagebox.showerror("Error","please enter the username to reset the password",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from studentlogin where username2=%s")
        value=(self.txtuser.get(),)
        cur.execute(query,value)
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","please enter the valid username",parent=self.root)
        else:
          conn.close()
          self.root2=Toplevel()
          self.root2.title=("forgot password")
          self.root2.geometry("490x380+550+500")
          self.root2.config(bg="black")
          l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="black")
          l.place(x=0,y=10,relwidth=1)

          security=Label(self.root2,text="Security Questions : ",font=("times new roman",18,"bold"),bg="black",fg="skyblue")
          security.place(x=20,y=60)
          self.securityname2=ttk.Combobox(self.root2,font=("times new roman",17),width=16,state="readonly")
          self.securityname2["value"]=("Select Questions","Your Idle","Your DOB","Your College Name","Your Favorite Singer","Your Best Friend")
          self.securityname2.current(0)
          self.securityname2.place(x=260,y=60)

          answer=Label(self.root2,text="Security Answer      : ",font=("times new roman",18,"bold"),bg="black",fg="skyblue")
          answer.place(x=20,y=140)
          self.answername2=ttk.Entry(self.root2,font=("times new roman",20))
          self.answername2.place(x=260,y=140,width=200)

          

          newpass=Label(self.root2,text="New Password         : ",font=("times new roman",18,"bold"),bg="black",fg="skyblue")
          newpass.place(x=20,y=220)
          self.newpassname2=ttk.Entry(self.root2,font=("times new roman",20))
          self.newpassname2.place(x=260,y=220,width=200)

          btn=Button(self.root2,command=self.resetpass,text="Reset",font=("times new roman",22,"bold"),bg="skyblue",fg="red",activebackground="skyblue",activeforeground="red")
          btn.place(x=40,y=280,width=140,height=40)

          btn1=Button(self.root2,command=self.clr,text="Login",font=("times new roman",22,"bold"),bg="skyblue",fg="red",activebackground="skyblue",activeforeground="red")
          btn1.place(x=280,y=280,width=140,height=40)


      




    


    def login(self):
      if self.txtuser.get()=="" or self.txtpassword.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      elif self.txtuser.get()=="naman" and self.txtpassword.get()=="1234":
        messagebox.showinfo("Success","Welcome",parent=self.root)
        self.newwindow=Toplevel(self.newwindow)
        self.app=Student1(self.newwindow)
      
        
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        cur.execute("select * from studentlogin where username2=%s and password2 =%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpassword.get()
                                                                                          ))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
        else:
          openmain=messagebox.askyesno("YesNo","Access Only Student",parent=self.root)
          if openmain>0:
            self.newwindow=Toplevel(self.root)
            self.app=Student1(self.newwindow)
          else:
            if not openmain:
              return 
        conn.commit()
        conn.close()

    


    
    



class register1:

    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")

      self.varfname2=StringVar()
      self.varlname2=StringVar()
      self.varcontact2=StringVar()
      self.varusername2=StringVar()
      self.varsecurityquestion2=StringVar()
      self.varsecurityanswer2=StringVar()
      self.varpassword2=StringVar()
      self.varconfirmpassword2=StringVar()

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
      self.ename=ttk.Entry(frame,textvariable=self.varfname2,font=("times new roman",20))
      self.ename.place(x=190,y=60,width=200)

      lname=Label(frame,text="Last Name     : ",font=("times new roman",20,"bold"),bg="white")
      lname.place(x=10,y=120)
      self.e1name=ttk.Entry(frame,textvariable=self.varlname2,font=("times new roman",20))
      self.e1name.place(x=190,y=120,width=200)

      contact=Label(frame,text="Contact No.   : ",font=("times new roman",20,"bold"),bg="white")
      contact.place(x=10,y=180)
      self.cname=ttk.Entry(frame,textvariable=self.varcontact2,font=("times new roman",20))
      self.cname.place(x=190,y=180,width=200)

      email=Label(frame,text="Username      : ",font=("times new roman",20,"bold"),bg="white")
      email.place(x=10,y=240)
      self.emailname=ttk.Entry(frame,textvariable=self.varusername2,font=("times new roman",20))
      self.emailname.place(x=190,y=240,width=200)

      security=Label(frame,text="Security  Questions : ",font=("times new roman",18,"bold"),bg="white")
      security.place(x=440,y=60)
      
    
      self.securityname2=ttk.Combobox(frame,textvariable=self.varsecurityquestion2,font=("times new roman",13),width=20,state="readonly")
      self.securityname2["value"]=("Select Questions","Your Idle","Your DOB","Your College Name","Your Favorite Singer","Your Best Friend")
      self.securityname2.current(0)
      self.securityname2.place(x=670,y=60)

      answer=Label(frame,text="Security Answer      : ",font=("times new roman",18,"bold"),bg="white")
      answer.place(x=440,y=120)
      self.answername2=ttk.Entry(frame,textvariable=self.varsecurityanswer2,font=("times new roman",20))
      self.answername2.place(x=670,y=120,width=200)

      password=Label(frame,text="Password                  : ",font=("times new roman",18,"bold"),bg="white")
      password.place(x=440,y=180)
      self.passwordrname=ttk.Entry(frame,textvariable=self.varpassword2,font=("times new roman",20))
      self.passwordrname.place(x=670,y=180,width=200)

      confirmpassword=Label(frame,text="Confirm Password   : ",font=("times new roman",18,"bold"),bg="white")
      confirmpassword.place(x=440,y=240)
      self.confirmpasswordname=ttk.Entry(frame,textvariable=self.varconfirmpassword2,font=("times new roman",20))
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
      b2=Button(frame,command=self.logout,image=self.photoimg2,borderwidth=0,cursor="hand2",bg="white")
      b2.place(x=220,y=380)

      img3=Image.open(r"images\64.jpg")
      img3=img3.resize((430,150),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)
      img3=Label(frame,image=self.photoimg3,borderwidth=0,bg="white")
      img3.place(x=440,y=320)
    #  
    def registerdata(self):

      if self.varfname2.get()=="" or self.varusername2.get()=="" or self.varsecurityquestion2.get()=="Security  Questions":
        messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.varpassword2.get()!=self.varconfirmpassword2.get():
        messagebox.showerror("Error","Password Must Be Same",parent=self.root)
      elif self.varcheck.get()==0:
        messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from studentlogin where username2=%s")
        value=(self.varusername2.get(),)
        cur.execute(query,value)
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","User Already Exist ... Please Try Another Username",parent=self.root)
        else:
          cur.execute("insert into studentlogin values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.varfname2.get(),
                                                                                  self.varlname2.get(),
                                                                                  self.varcontact2.get(),
                                                                                  self.varusername2.get(),
                                                                                  self.varsecurityquestion2.get(),
                                                                                  self.varsecurityanswer2.get(),
                                                                                  self.varpassword2.get()
                                                                                   ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Registered Successfully",parent=self.root)

    def logout(self):
      self.root.destroy()

class Student1:

    def __init__(self,root):
        self.root=root
        self.root.title("Students Academic Record")
        self.root.geometry("1550x830+0+0")
        self.root.config(bg="white")
       #icons
       
        lbltitle=Label(self.root,relief=RIDGE,text="STUDENT'S  ACADEMIC  RECORD ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
        lbltitle.place(x=0,y=0,width=1530,height=60)
        img4=Image.open(r"images\338.jpg")
        img4=img4.resize((1530,800),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        img4=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
        img4.place(x=0,y=60,width=1530,height=770)
        

        M_Frame=LabelFrame(self.root,bg="black")
        M_Frame.place(x=10,y=65,width=1510,height=80)
        btn_course=Button(M_Frame,command=self.add_new,text="Course's Available",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2")
        btn_course.place(x=60,y=15,width=280,height=50)
      
        btn_result=Button(M_Frame,command=self.add_view,text="View Result",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2")
        btn_result.place(x=410,y=15,width=200,height=50)
        btn_view=Button(M_Frame,text="Contact",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_contact)
        btn_view.place(x=690,y=15,width=200,height=50)
        btn_feedback=Button(M_Frame,text="Feedback",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_fedn)
        btn_feedback.place(x=970,y=15,width=200,height=50)
        btn_logout=Button(M_Frame,text="Logout",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=1240,y=15,width=200,height=50)
        

    def add_view(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=viewresults(self.new_win)

    def add_new(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=newc(self.new_win)


    def add_contact(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=feed(self.new_win)

    def add_fedn(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=feedbacknew(self.new_win)

    

    


        
    def logout(self):
        self.root.destroy()      


if __name__ == "__main__":
  main()