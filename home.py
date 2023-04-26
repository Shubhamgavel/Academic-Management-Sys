from email.charset import add_alias
from re import M
from tkinter import*
from PIL import Image,ImageTk 
from cse1 import course4
from student import students
from rslt1 import result1
from view import viewresults
from contact import feed




class Student:

    def __init__(self,root):
        self.root=root
        self.root.title("Students Academic Record")
        self.root.geometry("1550x830+0+0")
        self.root.config(bg="white")
       #icons
       
        lbltitle=Label(self.root,relief=RIDGE,text="STUDENT'S  ACADEMIC  RECORD ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
        lbltitle.place(x=0,y=0,width=1530,height=60)
        img4=Image.open(r"images\ITM7.jpg")
        img4=img4.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=60,width=1530,height=770)
        

        M_Frame=LabelFrame(self.root,bg="black")
        M_Frame.place(x=10,y=70,width=1512,height=80)
        btn_course=Button(M_Frame,text="Course",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course)
        btn_course.place(x=30,y=15,width=200,height=50)
        btn_student=Button(M_Frame,text="Student",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student)
        btn_student.place(x=290,y=15,width=200,height=50)
        btn_result=Button(M_Frame,text="Result",font=("",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result)
        btn_result.place(x=540,y=15,width=200,height=50)
        btn_view=Button(M_Frame,text="View",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_view)
        btn_view.place(x=790,y=15,width=200,height=50)
        btn_feedback=Button(M_Frame,text="Contact",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_feedback)
        btn_feedback.place(x=1040,y=15,width=200,height=50)
        btn_logout=Button(M_Frame,text="Logout",font=("times new roman",20,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout)
        btn_logout.place(x=1290,y=15,width=200,height=50)
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=course4(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=students(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=result1(self.new_win)

    def add_view(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=viewresults(self.new_win)

    def add_feedback(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=feed(self.new_win)

    def logout(self):
        self.root.destroy()
        import register
 
 

 
 
 


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()