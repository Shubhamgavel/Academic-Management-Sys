
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os


class course4:

  def  __init__(self,root):

       self.root=root
       self.root.title("Students Academic Record")
       self.root.geometry("1550x830+0+0")
       self.root.config(bg="white")

       self.varcourseid=StringVar()
       self.vardepartment=StringVar()
       self.varcourse=StringVar()
       self.varcharges=StringVar()
       self.varduration=StringVar()
       self.varyear=StringVar()
       self.varsubject1=StringVar()
       self.varsubject2=StringVar()
       self.varsubject3=StringVar()
       self.varsubject4=StringVar()
       self.varsubject5=StringVar()
       self.varsubject6=StringVar()

         #1
       img=Image.open(r"images\7.jpeg")
       img=img.resize((510,160),Image.Resampling.LANCZOS)
       self.photoimg=ImageTk.PhotoImage(img)

       self.btn1=Button(self.root,command=self.openimage,image=self.photoimg,cursor="hand2")
       self.btn1.place(x=0,y=0,width=510,height=160)

        #2
       img1=Image.open(r"images\rslt2.jpeg")
       img1=img1.resize((510,160),Image.Resampling.LANCZOS)
       self.photoimg1=ImageTk.PhotoImage(img1)

       self.btn2=Button(self.root,command=self.openimage1,image=self.photoimg1,cursor="hand2")
       self.btn2.place(x=510,y=0,width=510,height=160)
       
        #3
       img2=Image.open(r"images\6.jpeg")
       img2=img2.resize((510,160),Image.Resampling.LANCZOS)
       self.photoimg2=ImageTk.PhotoImage(img2)

       self.btn3=Button(self.root,command=self.openimage2,image=self.photoimg2,cursor="hand2")
       self.btn3.place(x=1020,y=0,width=510,height=160)

        #bg image

       img3=Image.open(r"images\result.jpeg")
       img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
       self.photoimg3=ImageTk.PhotoImage(img3)


       bg_lbl=Label(self.root,image=self.photoimg3,bd=2,relief=RIDGE)
       bg_lbl.place(x=0,y=160,width=1530,height=710)

       lbltitle=Label(bg_lbl,relief=RIDGE,text="MANAGE  COURSE  DETAILS ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
       lbltitle.place(x=0,y=0,width=1530,height=50)

        #maNAGEFRAME
       manageframe=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
    
       manageframe.place(x=15,y=55,width=1500,height=600)

        #leftframe
    
       dataleftframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text=" Course Information ",font=("times new roman",20,"bold"),fg="red",bg="white")

    
       dataleftframe.place(x=10,y=10,width=650,height=570)

        #img
    
       img4=Image.open(r"images\5.webp")
    
       img4=img4.resize((638,120),Image.Resampling.LANCZOS)
       self.photoimg4=ImageTk.PhotoImage(img4)


       myimg=Label(dataleftframe,image=self.photoimg4)
       myimg.place(x=0,y=0,width=638,height=120)

         #coursesid
       lblid=Label(dataleftframe,text="Course I'd    :",font=("times new roman",16,"bold"),bg="white")
       lblid.grid(row=0,column=0,padx=2,pady=10,sticky=W)

       lblid.place(x=10,y=120)
       lblid=Label(dataleftframe,text="*",font=("times new roman",16,"bold"),bg="white",fg="red")
       lblid.grid(row=0,column=0,padx=2,pady=10,sticky=W)

       lblid.place(x=106,y=115)


       identry=ttk.Entry(dataleftframe,textvariable=self.varcourseid,font=("times new roman",16,"bold"),width=15)

       identry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

       identry.place(x=140,y=120)
         #dept

       lbldept=Label(dataleftframe,text="Department  :",font=("times new roman",16,"bold"),bg="white")
       lbldept.grid(row=0,column=2,padx=2,sticky=W)

       lbldept.place(x=330,y=120)
       combodep=ttk.Combobox(dataleftframe,textvariable=self.vardepartment,font=("arial",11,"bold"),width=18,state="readonly")
       combodep["value"]=("Select Department","Computer","Commerce","Science","Management","Law")
       combodep.current(0)
       combodep.grid(row=0,column=3,padx=2,pady=10,sticky=W)
       combodep.place(x=465,y=120)
        #course##############################################################################

       lblcourses=Label(dataleftframe,text="Courses       :",font=("times new roman",16,"bold"),bg="white")
       lblcourses.grid(row=1,column=0,padx=2,sticky=W)

       lblcourses.place(x=10,y=180)

       combocourses=ttk.Combobox(dataleftframe,textvariable=self.varcourse,font=("arial",11,"bold"),width=18,state="readonly")
       combocourses["value"]=("Select courses","BCA","BSC","BBA","B.COM","LLB")
           
       combocourses.current(0)
       combocourses.grid(row=1,column=1,padx=2,pady=10,sticky=W)
       combocourses.place(x=140,y=180)


        #year#############################################################
       lblyear=Label(dataleftframe,text="Year              :",font=("times new roman",16,"bold"),bg="white")
       lblyear.grid(row=1,column=2,padx=2,pady=10,sticky=W)

       lblyear.place(x=330,y=180)

       comboyear=ttk.Combobox(dataleftframe,textvariable=self.varyear,font=("arial",11,"bold"),width=18,state="readonly")
       comboyear["value"]=("Select Year","1st Year","2nd Year","3rd Year")
       comboyear.current(0)
       comboyear.grid(row=0,column=3,padx=2,pady=10,sticky=W)
       comboyear.place(x=465,y=180)

       #Charges########################################################
       lblCharges=Label(dataleftframe,text="Charges      :",font=("times new roman",16,"bold"),bg="white")
       lblCharges.grid(row=2,column=0,padx=2,sticky=W)

       lblCharges.place(x=10,y=240)
       Chargesentry=ttk.Entry(dataleftframe,textvariable=self.varcharges,font=("times new roman",15,"bold"),width=16)

       Chargesentry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

       Chargesentry.place(x=140,y=240)

         #duration
       lblduration=Label(dataleftframe,text="Duration        :",font=("times new roman",15,"bold"),bg="white")
       lblduration.grid(row=2,column=2,padx=2,pady=10,sticky=W)

       lblduration.place(x=330,y=240)

       durationentry=ttk.Entry(dataleftframe,textvariable=self.varduration,font=("times new roman",15,"bold"),width=16)

       durationentry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

       durationentry.place(x=465,y=240)



        #sub1
       lblsub1=Label(dataleftframe,text="Subject  1    :",font=("times new roman",15,"bold"),bg="white")
       lblsub1.grid(row=3,column=0,padx=2,pady=10,sticky=W)

       lblsub1.place(x=10,y=290)

       subject1entry=ttk.Entry(dataleftframe,textvariable=self.varsubject1,font=("times new roman",15,"bold"),width=16)

       subject1entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

       subject1entry.place(x=140,y=290)

        

        #subject2
       lblsubject2=Label(dataleftframe,text="Subject  2      :",font=("times new roman",15,"bold"),bg="white")
       lblsubject2.grid(row=3,column=2,padx=2,pady=10,sticky=W)

       lblsubject2.place(x=330,y=290)

       subject2entry=ttk.Entry(dataleftframe,textvariable=self.varsubject2,font=("times new roman",15,"bold"),width=16)

       subject2entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)

       subject2entry.place(x=465,y=290)


        #subject3
       lblsubject3=Label(dataleftframe,text="Subject  3    :",font=("times new roman",15,"bold"),bg="white")
       lblsubject3.grid(row=4,column=0,padx=2,pady=10,sticky=W)
 
       lblsubject3.place(x=10,y=340)

       subject3entry=ttk.Entry(dataleftframe,textvariable=self.varsubject3,font=("times new roman",15,"bold"),width=16)

       subject3entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)

       subject3entry.place(x=140,y=340)

           #subject4
       lblsubject4=Label(dataleftframe,text="Subject  4      :",font=("times new roman",15,"bold"),bg="white")
       lblsubject4.grid(row=4,column=2,padx=2,pady=10,sticky=W)

       lblsubject4.place(x=330,y=340)

       subject4entry=ttk.Entry(dataleftframe,textvariable=self.varsubject4,font=("times new roman",15,"bold"),width=16)

       subject4entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)

       subject4entry.place(x=465,y=340)

        #subject5
       lblsubject5=Label(dataleftframe,text="Subject  5    :",font=("times new roman",15,"bold"),bg="white")
       lblsubject5.grid(row=5,column=0,padx=2,pady=10,sticky=W)

       lblsubject5.place(x=10,y=390)

       subject5entry=ttk.Entry(dataleftframe,textvariable=self.varsubject5,font=("times new roman",15,"bold"),width=16)

       subject5entry.grid(row=5,column=1,padx=2,pady=10,sticky=W)

       subject5entry.place(x=140,y=390)

        #subject6
       lblsubject6=Label(dataleftframe,text="Subject  6      :",font=("times new roman",15,"bold"),bg="white")
       lblsubject6.grid(row=5,column=2,padx=2,pady=10,sticky=W)
   
       lblsubject6.place(x=330,y=390)

       subject6entry=ttk.Entry(dataleftframe,textvariable=self.varsubject6,font=("times new roman",15,"bold"),width=16)

       subject6entry.grid(row=5,column=3,padx=2,pady=10,sticky=W)

       subject6entry.place(x=465,y=390)
     

      #save##########################################################
        
       btnframe=Frame(dataleftframe,bd=2,relief=RIDGE,bg="green")
       btnframe.place(x=10,y=460,width=620,height=53)
        
       btnadd=Button(btnframe,command=self.adddata,text="Save",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
       btnadd.grid(row=0,column=0,sticky=W,padx=6,pady=7)

       btnupdate=Button(btnframe,command=self.updatedata,text="Update",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
       btnupdate.grid(row=0,column=1,sticky=W,padx=6,pady=7)

       btndelete=Button(btnframe,command=self.deteledata,text="Delete",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
       btndelete.grid(row=0,column=2,sticky=W,padx=6,pady=7)

       btnclear=Button(btnframe,command=self.cleardata,text="Clear",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
       btnclear.grid(row=0,column=3,sticky=W,padx=6,pady=7)

       btnexit=Button(btnframe,command=self.exit,text="Exit",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
       btnexit.grid(row=0,column=4,sticky=W,padx=6,pady=7)
        



        ################################################################ #rightframe
       datarightframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text=" Course Details ",font=("times new roman",20,"bold"),fg="red",bg="white")

       datarightframe.place(x=670,y=10,width=810,height=570)


       img5=Image.open(r"images\15.png")
       img5=img5.resize((800,150),Image.Resampling.LANCZOS)
       self.photoimg5=ImageTk.PhotoImage(img5)
 

       myimg=Label(datarightframe,image=self.photoimg5)
       myimg.place(x=0,y=0,width=800,height=150)

        #rightframe
       lblsub7=Label(datarightframe,text="Search courses Details......",font=("times new roman",20,"bold"),fg="red",bg="white")
       lblsub7.place(x=0,y=150)
       btnsframe=Frame(datarightframe,bd=4,relief=RIDGE,padx=2,bg="green")
       btnsframe.place(x=3,y=195,width=790,height=60)

       search=Button(btnsframe,text="Search By :",font=("times new roman",14,"bold"),width=11,bg="gold",fg="black")
       search.grid(row=0,column=0,padx=10,pady=7,sticky=W)

         #search
       self.var_combosearch=StringVar()
       combosearch=ttk.Combobox(btnsframe,textvariable=self.var_combosearch,font=("times new roman",14,"bold"),width=13,state="readonly")
       combosearch["value"]=("Select Options","courseid","Department","Course")
       combosearch.current(0)
       combosearch.grid(row=0,column=1,padx=8,pady=7,sticky=W)
       self.var_search=StringVar()

       searchentry=ttk.Entry(btnsframe,textvariable=self.var_search,font=("times new roman",14,"bold"),width=13)

       searchentry.grid(row=0,column=2,padx=8,pady=7,sticky=W)
        

       btnsearch=Button(btnsframe,command=self.searchdata,text="Search",font=("times new roman",14,"bold"),width=11,bg="gold",fg="black")
       btnsearch.grid(row=0,column=3,sticky=W,padx=8,pady=7)

       btnshowall=Button(btnsframe,command=self.fetchdata,text="Show  All",font=("times new roman",14,"bold"),width=11,bg="gold",fg="black")
       btnshowall.grid(row=0,column=4,sticky=W,padx=8,pady=7)

        #course table
       tableframe=Frame(datarightframe,bd=4,relief=RIDGE)
       tableframe.place(x=0,y=260,width=795,height=270)

       scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
       scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
        
       self.course_table=ttk.Treeview(tableframe,column=("courseid","department","course","year","charges","duration","subject1","subject2","subject3","subject4","subject5","subject6",),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       scrollx.pack(side=BOTTOM,fill=X)
       scrolly.pack(side=RIGHT,fill=Y)

       scrollx.config(command=self.course_table.xview)
       scrolly.config(command=self.course_table.yview)

       self.course_table.heading("courseid",text="Course I'd")
       self.course_table.heading("department",text="Department")
       self.course_table.heading("course",text="Course")
       self.course_table.heading("year",text="year")
       self.course_table.heading("charges",text="Charge")
       self.course_table.heading("duration",text="Duration")
       self.course_table.heading("subject1",text="Subject  1")
       self.course_table.heading("subject2",text="Subject  2   ")
       self.course_table.heading("subject3",text="Subject 3")
       self.course_table.heading("subject4",text="Subject  4")
       self.course_table.heading("subject5",text="Subject  5")
       self.course_table.heading("subject6",text="Subject  6")

       self.course_table["show"]="headings"

       self.course_table.column("courseid",width=100)
       self.course_table.column("department",width=150)
       self.course_table.column("course",width=150)
       self.course_table.column("year",width=150)
       self.course_table.column("charges",width=150)
       self.course_table.column("duration",width=150)
       self.course_table.column("subject1",width=150)
       self.course_table.column("subject2",width=150)
       self.course_table.column("subject3",width=150)
       self.course_table.column("subject4",width=150)
       self.course_table.column("subject5",width=150)
       self.course_table.column("subject6",width=150)
       self.course_table.pack(fill=BOTH,expand=1)
       self.course_table.bind("<ButtonRelease>",self.getcursor)
       self.fetchdata()



        #mysql#########################################

  def adddata(self):
        if(self.varcourseid.get()=="" or self.vardepartment.get()=="" or self.varcourse.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required",parent=self.root)
        else:
            try:

        
                conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                mycursor=conn.cursor()
                mycursor.execute("insert into coursetable values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                  self.varcourseid.get(),
                                                                                                  self.vardepartment.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  
                                                                                                  self.varyear.get(),
                                                                                                  self.varcharges.get(),
                                                                                                  self.varduration.get(),
                                                                                                  self.varsubject1.get(),
                                                                                                  self.varsubject2.get(),
                                                                                                  self.varsubject3.get(),
                                                                                                  self.varsubject4.get(),
                                                                                                  self.varsubject5.get(),
                                                                                                  self.varsubject6.get(),
                                                                                                  

                                                                                               ))


                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success","courses has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


  def fetchdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        mycursor=conn.cursor()
        mycursor.execute("select *from coursetable ")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.course_table.delete(*self.course_table.get_children())
            for i in data:
                self.course_table.insert("",END,values=i)
            conn.commit()
        conn.close()


  

     #get cursor

 
  def getcursor(self,event=""):
        cursorrow=self.course_table.focus()
        content=self.course_table.item(cursorrow)
        data=content["values"]


        self.varcourseid.set(data[0])
        self.vardepartment.set(data[1])
        self.varcourse.set(data[2])
        
        self.varyear.set(data[3])
        self.varcharges.set(data[4])
        
       
        
        self.varduration.set(data[5])
        self.varsubject1.set(data[6])
        self.varsubject2.set(data[7])
        self.varsubject3.set(data[8])
        self.varsubject4.set(data[9])
        self.varsubject5.set(data[10])
        self.varsubject6.set(data[11])

  def updatedata(self):
        if(self.varcourseid.get()=="" or self.vardepartment.get()=="" or self.varcourse.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure bto update this courses information",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    mycursor.execute("update coursetable set department=%s,course=%s,year=%s,charges=%s,duration=%s,subject1=%s,subject2=%s,subject3=%s,subject4=%s,subject5=%s,subject6=%s where courseid=%s",(
                        
                                                                                                  self.vardepartment.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  
                                                                                                  self.varyear.get(),
                                                                                                  self.varcharges.get(),
                                                                                                  self.varduration.get(),
                                                                                                  self.varsubject1.get(),
                                                                                                  self.varsubject2.get(),
                                                                                                  self.varsubject3.get(),
                                                                                                  self.varsubject4.get(),
                                                                                                  self.varsubject5.get(),
                                                                                                  self.varsubject6.get(),
                                                                                                  self.varcourseid.get(),    

                                                                                                    ))        

                else:
                    if not update:
                        return
                conn.commit()
                self.fetchdata()
                conn.close()

                messagebox.showinfo("success","courses Updated Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

  def deteledata(self):
        if self.varcourseid.get()=="":
            messagebox.showerror("Error.....","All Fields Are Required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to Delete this courses",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    sql="Delete from coursetable where courseid=%s"
                    value=(self.varcourseid.get(),)
                    mycursor.execute(sql,value)
                else:
                    if not Delete:
                      return 
                conn.commit()
                self.fetchdata()
            
                conn.close()
                messagebox.showinfo("Delete","Your Data has been deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
  def cleardata(self):
        self.varcourseid.set("")
        self.vardepartment.set("Select Department")
        self.varcourse.set("Select courses")
        self.varyear.set("Select Year")
        self.varcharges.set("")
        
        
        self.varduration.set("")
        self.varsubject1.set("")
        self.varsubject2.set("")
        self.varsubject3.set("")
        self.varsubject4.set("")
        self.varsubject5.set("")


        self.varsubject6.set("")
  def searchdata(self):
        if self.var_combosearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please Select Option")

        else:

            
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                mycursor=conn.cursor()
                mycursor.execute("select * from coursetable where "+str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=mycursor.fetchall()
                if len(data)!=0:
                    
                    self.course_table.delete(*self.course_table.get_children())
                    for i in data:
                        self.course_table.insert("",END,values=i)
                    conn.commit()
                conn.close()



                    

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    
 

    #openimage
  def openimage(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
        img=Image.open(fln)
        imgbrowse=img.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimgbrowse=ImageTk.PhotoImage(imgbrowse)
        self.btn1.config(image=self.photoimgbrowse)

         #openimage
  def openimage1(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
        img1=Image.open(fln)
        imgbrowse1=img1.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimgbrowse1=ImageTk.PhotoImage(imgbrowse1)
        self.btn2.config(image=self.photoimgbrowse1)


      #openimage
      #
      # 
  def openimage2(self):
    
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
        img2=Image.open(fln)
        imgbrowse2=img2.resize((510,160),Image.Resampling.LANCZOS)
        self.photoimgbrowse2=ImageTk.PhotoImage(imgbrowse2)
        self.btn2.config(image=self.photoimgbrowse2)

  def exit(self):
        self.root.destroy()


    
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=course4(root)
    root.mainloop()