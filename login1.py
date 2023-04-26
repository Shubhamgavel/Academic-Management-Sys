

from tkinter import*
from  tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector





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
      registerbtn=Button(frame,text="New User Register",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      registerbtn.place(x=230,y=210,width=170,height=35)
      paswordbtn=Button(frame,text="Forgot Password ",font=("times new roman",15),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
      paswordbtn.place(x=230,y=240,width=170,height=35)
    
    

    def login(self):
       if  self.txtuser.get() or self.txtpassword.get()=="":
          messagebox.showerror("error","all fields qare requireds",parent=self.root)

       else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                cur=con.cursor()
                cur.execute("select * from adminregister where username=%s and password =%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpassword.get()
                                                                                          ))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Uswrname ",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                con.close()
                    

            
            except Exception as es:
             messagebox.showerror("error",f"error due nto :{str(es)}",parent=self.root)

         
     

    
if __name__ == "__main__":
    root=Tk()
    obj=loginadmin(root)
    root.mainloop()