from email.charset import add_alias
from re import M
from tkinter import*
from PIL import Image,ImageTk 
from newcourse import newc
from view import viewresults
from contact import feed
from feed1 import feedbacknew



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
    root=Tk()
    obj=Student1(root)
    root.mainloop()