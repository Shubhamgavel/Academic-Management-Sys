from tkinter import*
from  tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def mainfn():
    wind=Tk()
    obj=admin(wind)
    wind.mainloop()

class admin:
  
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
      self.vartextuser=ttk.Entry(frame,font=("times new roman",14,"bold"))
      self.vartextuser.place(x=200,y=125,width=200)

      passwordlbl=Label(frame,text="Password :",font=("times new roman",18,"bold"),fg="red",bg="black")
      passwordlbl.place(x=70,y=165)
      self.vartextpassword=ttk.Entry(frame,font=("times new roman",14,"bold"))
      self.vartextpassword.place(x=200,y=165,width=200)


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
     
      loginbtn=Button(frame,command=self.loginadmin,text="Login",font=("times new roman",18,"bold"),bd=3,relief=RIDGE,fg="black",bg="skyblue",activeforeground="black",activebackground="skyblue")
      loginbtn.place(x=50,y=220,width=120,height=35)
      registerbtn=Button(frame,command=self.reg,text="New User Register",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      registerbtn.place(x=230,y=210,width=170,height=35)
      paswordbtn=Button(frame,text="Forgot Password ",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      paswordbtn.place(x=230,y=240,width=170,height=35)

    def reg(self):
        self.new_window=Toplevel(self.root)
        self.obj1=register2(self.new_window)
    
    
    

    def loginadmin(self):
      if self.vartextuser.get()=="" or self.vartextpassword.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      elif self.vartextuser.get()=="naman" and self.vartextpassword.get()=="1234":
        messagebox.showinfo("Success","Welcome",parent=self.root)
        
        
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        cur.execute("select * from adminlogin2 where username2=%s and password2=%s",(self.vartextuser.get(),self.vartextpassword.get()))
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("error","invalid username and password",parent=self.root)
        else:
          open_new=messagebox.askyesno("YesNo","Access only Admin",parent=self.root)
          if open_new>0:
            self.new_window=Toplevel(self.root)
            self.obj3=feed(self.new_window)
          else :
            if not open_new:
              return
        conn.commit()
        conn.close()



class register2:
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
      self.ename=ttk.Entry(frame,textvariable=self.varfname2,font=("times new roman",20))
      self.ename.place(x=190,y=60,width=200)

      lname=Label(frame,text="Last Name  : ",font=("times new roman",20,"bold"),bg="white")
      lname.place(x=10,y=120)
      self.e1name=ttk.Entry(frame,textvariable=self.varlname2,font=("times new roman",20))
      self.e1name.place(x=190,y=120,width=200)

      contact=Label(frame,text="Contact No.  : ",font=("times new roman",20,"bold"),bg="white")
      contact.place(x=10,y=180)
      self.cname=ttk.Entry(frame,textvariable=self.varcontact2,font=("times new roman",20))
      self.cname.place(x=190,y=180,width=200)

      email=Label(frame,text="Username : ",font=("times new roman",20,"bold"),bg="white")
      email.place(x=10,y=240)
      self.emailname=ttk.Entry(frame,textvariable=self.varusername2,font=("times new roman",20))
      self.emailname.place(x=190,y=240,width=200)

      security=Label(frame,text="Security  Questions : ",font=("times new roman",18,"bold"),bg="white")
      security.place(x=440,y=60)
      
    
      self.securityname=ttk.Combobox(frame,textvariable=self.varsecurityquestion2,font=("times new roman",13),width=20,state="readonly")
      self.securityname["value"]=("Select Questions","Your Idle","Your DOB","Your College Name","Your Favorite Singer","Your Best Friend")
      self.securityname.current(0)
      self.securityname.place(x=670,y=60)

      answer=Label(frame,text="Security Answer  : ",font=("times new roman",18,"bold"),bg="white")
      answer.place(x=440,y=120)
      self.answername=ttk.Entry(frame,textvariable=self.varsecurityanswer2,font=("times new roman",20))
      self.answername.place(x=670,y=120,width=200)

      password=Label(frame,text="Password  : ",font=("times new roman",18,"bold"),bg="white")
      password.place(x=440,y=180)
      self.passwordrname=ttk.Entry(frame,textvariable=self.varpassword2,font=("times new roman",20))
      self.passwordrname.place(x=670,y=180,width=200)

      confirmpassword=Label(frame,text="Confirm Password  : ",font=("times new roman",18,"bold"),bg="white")
      confirmpassword.place(x=440,y=240)
      self.confirmpasswordname=ttk.Entry(frame,textvariable=self.varconfirmpassword,font=("times new roman",20))
      self.confirmpasswordname.place(x=670,y=240,width=200)
      self.varcheck2=IntVar()
      checkbtn=Checkbutton(frame,variable=self.varcheck2,text="I Agree The Terms & Coditions",font=("times new roman",18,"bold"),bg="white",fg="red",onvalue=1,offvalue=0)
      checkbtn.place(x=30,y=320)

      img1=Image.open(r"images\63.png")
      img1=img1.resize((140,50),Image.Resampling.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)
      b1=Button(frame,command=self.registerdata2,image=self.photoimg1,borderwidth=0,cursor="hand2",bg="white")
      b1.place(x=50,y=380)

      img2=Image.open(r"images\62.jpg")
      img2=img2.resize((140,50),Image.Resampling.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)
      b2=Button(frame,image=self.photoimg2,borderwidth=0,cursor="hand2",bg="white")
      b2.place(x=220,y=380)

      img3=Image.open(r"images\64.jpg")
      img3=img3.resize((430,150),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)
      img3=Label(frame,image=self.photoimg3,borderwidth=0,bg="white")
      img3.place(x=440,y=320)
    #  
    def registerdata2(self):

      if self.varfname2.get()=="" or self.varusername2.get()=="" or self.varsecurityquestion2.get()=="Security  Questions":
        messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      elif self.varpassword2.get()!=self.varconfirmpassword.get():
        messagebox.showerror("Error","Password Must Be Same",parent=self.root)
      elif self.varcheck2.get()==0:
        messagebox.showerror("Error","Please Agree Our Terms And Conditions",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from adminlogin2 where username2=%s")
        value=(self.varusername2.get(),)
        cur.execute(query,value)
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","User Already Exist ... Please Try Another Username",parent=self.root)
        else:
          cur.execute("insert into adminlogin2 values(%s,%s,%s,%s,%s,%s,%s)",(
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
       img4=Image.open(r"images\104.jpg")
       img4=img4.resize((330,400),Image.Resampling.LANCZOS)
       self.photoimg4=ImageTk.PhotoImage(img4)
       img4=Label(lbl1,image=self.photoimg4,bd=5,relief=RIDGE)
       img4.place(x=25,y=90,width=330,height=400)
       lbl5=Label(lbl1,relief=RIDGE,bg="#d9b2ff")
       lbl5.place(x=25,y=505,width=330,height=130)
       lbl6=Label(lbl5,text=" Naman Jha ",font=("times new roman",25,"bold"),fg="black",bg="#d9b2ff")
       lbl6.place(x=65,y=0)
       lbl7=Label(lbl5,text=" (  BCA  III  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl7.place(x=65,y=40)
       lbl8=Label(lbl5,text=" ( Roll no. :- 22 )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl8.place(x=45,y=80)
       
       lbl3=Label(self.root,relief=RIDGE,bg="black")
       lbl3.place(x=440,y=80,width=1070,height=670)
       lbl4=Label(lbl3,text="Guided  By ",font=("times new roman",30,"bold"),fg="skyblue",bg="black")
       lbl4.place(x=390,y=15)
       img5=Image.open(r"images\92.jpg")
       img5=img5.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg5=ImageTk.PhotoImage(img5)
       img5=Label(lbl3,image=self.photoimg5,bd=5,relief=RIDGE)
       img5.place(x=25,y=90,width=320,height=400)
       lbl12=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl12.place(x=25,y=505,width=320,height=130)
       lbl9=Label(lbl12,text="Mrs. Rekha Awasthi",font=("times new roman",23,"bold"),fg="black",bg="#d9b2ff")
       lbl9.place(x=15,y=0)
       lbl10=Label(lbl12,text=" (  Asst.  Prof.  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl10.place(x=55,y=40)
       lbl11=Label(lbl12,text=" ( Computer  Science )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl11.place(x=17,y=80)


       img6=Image.open(r"images\98.jpeg")
       img6=img6.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg6=ImageTk.PhotoImage(img6)
       img6=Label(lbl3,image=self.photoimg6,bd=3,relief=RIDGE)
       img6.place(x=375,y=90,width=320,height=400)
       lbl13=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl13.place(x=375,y=505,width=320,height=130)
       lbl14=Label(lbl13,text="Mrs. Barkha Raghuwanshi",font=("times new roman",19,"bold"),fg="black",bg="#d9b2ff")
       lbl14.place(x=10,y=0)
       lbl15=Label(lbl13,text=" (  Asst.  Prof.  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl15.place(x=55,y=40)
       lbl16=Label(lbl13,text=" ( Computer  Science )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl16.place(x=17,y=80)


       img7=Image.open(r"images\93.jpg")
       img7=img7.resize((320,400),Image.Resampling.LANCZOS)
       self.photoimg7=ImageTk.PhotoImage(img7)
       img7=Label(lbl3,image=self.photoimg7,bd=5,relief=RIDGE)
       img7.place(x=725,y=90,width=320,height=400)
       lbl17=Label(lbl3,relief=RIDGE,bg="#d9b2ff")
       lbl17.place(x=725,y=505,width=320,height=130)
       lbl18=Label(lbl17,text="Ms. Pooja Singh",font=("times new roman",23,"bold"),fg="black",bg="#d9b2ff")
       lbl18.place(x=50,y=0)
       lbl19=Label(lbl17,text=" (  Asst.  Prof.  )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl19.place(x=55,y=40)
       lbl20=Label(lbl17,text=" ( Computer  Science )",font=("times new roman",21,"bold"),fg="black",bg="#d9b2ff")
       lbl20.place(x=17,y=80)

  def logout(self):
        self.root.destroy()

    
if __name__ == "__main__":
   mainfn()