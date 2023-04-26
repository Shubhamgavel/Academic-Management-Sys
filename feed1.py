from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os

class feedbacknew:

   def  __init__(self,root):

      self.root=root
      self.root.title("Students Academic Record")
      self.root.geometry("1290x550+120+200")
      self.root.config(bg="darkgreen")
      self.varroll=StringVar()
      self.varname=StringVar()
      self.varcourse=StringVar()
      self.varyear=StringVar()
      self.varemail=StringVar()
      self.varmobile=StringVar()
      self.varfeedback=StringVar()
      lbltitle=Label(self.root,relief=RIDGE,text="Feedback Form ",font=("courier new",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=0,width=1290,height=60)
      

      lbl1=Label(self.root,relief=RIDGE)
      lbl1.place(x=20,y=80,width=680,height=450)

      lblid=Label(lbl1,text="Please Submit Your Feedback Form",font=("times new roman",22,"bold"),fg="red")
      

      lblid.place(x=120,y=0)

      img4=Image.open(r"images\55.jpg")
      img4=img4.resize((560,450),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
      img4=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      img4.place(x=710,y=80,width=560,height=450)

      lblname=Label(lbl1,text="Name      :",font=("times new roman",22,"bold"))
      lblname.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblname.place(x=10,y=70)

      nameentry=ttk.Entry(lbl1,textvariable=self.varname,font=("times new roman",15,"bold"),width=15)

      nameentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      nameentry.place(x=140,y=76)

      lblroll=Label(lbl1,text="Roll  No.   :",font=("times new roman",18,"bold"))
      lblroll.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblroll.place(x=370,y=70)

      rollentry=ttk.Entry(lbl1,textvariable=self.varroll,font=("times new roman",15,"bold"),width=15)

      rollentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      rollentry.place(x=500,y=74)

      lblcourse=Label(lbl1,text="Course    :",font=("times new roman",20,"bold"))
      lblcourse.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblcourse.place(x=10,y=135)
      

      courseentry=ttk.Combobox(lbl1,textvariable=self.varcourse,font=("times new roman",13,"bold"),width=15,state="readonly")
      courseentry["value"]=("Select Course","BCA","BSC","BBA","B.COM","LLB")
      courseentry.current(0)
      

      courseentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      courseentry.place(x=140,y=145)

      lblyear=Label(lbl1,text="Year       :",font=("times new roman",20,"bold"))
      lblyear.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblyear.place(x=370,y=135)

      yearentry=ttk.Combobox(lbl1,textvariable=self.varyear,font=("times new roman",13,"bold"),width=15,state="readonly")
      yearentry["value"]=("Select Year","1st Year","2nd Year","3rd Year")
      yearentry.current(0)
      

      yearentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
 
      yearentry.place(x=500,y=145)

      lblemail=Label(lbl1,text="Email      :",font=("times new roman",20,"bold"))
      lblemail.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblemail.place(x=10,y=195)

      emailentry=ttk.Entry(lbl1,textvariable=self.varemail,font=("times new roman",15,"bold"),width=15)

      emailentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      emailentry.place(x=140,y=200)

      lblmobile=Label(lbl1,text="Mobile      :",font=("times new roman",18,"bold"))
      lblmobile.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblmobile.place(x=370,y=199)

      mobileentry=ttk.Entry(lbl1,textvariable=self.varmobile,font=("times new roman",15,"bold"),width=15)

      mobileentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      mobileentry.place(x=500,y=198)

      lblfeed=Label(lbl1,text="Write Your Feedback Here ...",font=("times new roman",20,"bold"),fg="blue")
      lblfeed.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblfeed.place(x=10,y=250)
      feedentry=ttk.Entry(lbl1,textvariable=self.varfeedback,font=("times new roman",15,"bold"))
      feedentry.place(x=20,y=300,width=640,height=40)

      btnsubmit=Button(lbl1,command=self.sumbit,text="Submit",font=("times new roman",16,"bold"),width=13,bg="skyblue",fg="black")
      btnsubmit.grid(row=0,column=2,sticky=W,padx=6,pady=7)
      btnsubmit.place(x=40,y=380)
      

      btnclear=Button(lbl1,command=self.clear,text="Clear",font=("times new roman",16,"bold"),width=13,bg="skyblue",fg="black")
      btnclear.grid(row=0,column=3,sticky=W,padx=6,pady=7)
      btnclear.place(x=260,y=380)

      btnexit=Button(lbl1,command=self.exit,text="Exit",font=("times new roman",16,"bold"),width=13,bg="skyblue",fg="black")
      btnexit.grid(row=0,column=4,sticky=W,padx=6,pady=7)
      btnexit.place(x=470,y=380)


   def sumbit(self):

        
      if self.varname.get()=="" or self.varroll.get()=="" or self.varcourse.get()=="Select Course" or self.varfeedback.get=="":
        messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        cur=conn.cursor()
        query=("select * from fedback where roll=%s")
        value=(self.varname.get(),)
        cur.execute(query,value)
        row=cur.fetchone()
        if row!=None:
          messagebox.showerror("Error","User Already Exist ... Please Try Another Username",parent=self.root)
        else:
          cur.execute("insert into fedback values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.varname.get(),
                                                                                  self.varroll.get(),
                                                                                  self.varcourse.get(),
                                                                                  self.varyear.get(),
                                                                                  self.varemail.get(),
                                                                                  self.varmobile.get(),
                                                                                  self.varfeedback.get()
                                                                                   ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Your Response is Submitted Successfully",parent=self.root)
   
   def clear(self):
       self.varroll.set("")
       self.varname.set("")
       self.varcourse.set("Select Course")
       self.varyear.set("Select Year")
       self.varemail.set("")
       self.varmobile.set("")
       self.varfeedback.set("")

   def exit(self):
        self.root.destroy()
    

    


      


     





if __name__ == "__main__":
   root=Tk()
   obj=feedbacknew(root)
   root.mainloop()