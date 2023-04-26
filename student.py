from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os


class students:

  def  __init__(self,root):

    self.root=root
    self.root.title("Students Academic Record")
    self.root.geometry("1550x830+0+0")
    self.root.config(bg="white")

    self.varroll=StringVar()
    self.varuniqueid=StringVar()
    self.varname=StringVar()
    self.vargender=StringVar()
    
    self.vardob=StringVar()
    self.varblood=StringVar()
    self.varmobile=StringVar()
    self.varemail=StringVar()
    self.varaddress=StringVar()
    self.varcourseid=StringVar()
    self.varcourse=StringVar()
    
    self.varyear=StringVar()
    self.varsubject1=StringVar()
    self.varsubject2=StringVar()
    self.varsubject3=StringVar()
    self.varsubject4=StringVar()
    self.varsubject5=StringVar()
    self.varsubject6=StringVar()

        
  
    img4=Image.open(r"images\result.jpeg")
    img4=img4.resize((1530,720),Image.Resampling.LANCZOS)
    self.photoimg4=ImageTk.PhotoImage(img4)
   

    bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
    bg_lbl.place(x=0,y=135,width=1530,height=720)

    lbltitle=Label(bg_lbl,relief=RIDGE,text="MANAGE  STUDENT'S  DETAILS",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
    lbltitle.place(x=0,y=5,width=1530,height=60)

   #1
    img=Image.open(r"images\81.jpg")  
    img=img.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimg=ImageTk.PhotoImage(img)

    self.btn1=Button(self.root,command=self.openimage,image=self.photoimg,cursor="hand2")
    self.btn1.place(x=0,y=0,width=385,height=140)
    #2
    img1=Image.open(r"images\42.jpg")
    img1=img1.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimg1=ImageTk.PhotoImage(img1)

    self.btn2=Button(self.root,command=self.openimage1,image=self.photoimg1,cursor="hand2")
    self.btn2.place(x=385,y=0,width=385,height=140)
       
     #3
    img2=Image.open(r"images\41.jpg")
    img2=img2.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimg2=ImageTk.PhotoImage(img2)

    self.btn3=Button(self.root,command=self.openimage2,image=self.photoimg2,cursor="hand2")
    self.btn3.place(x=770,y=0,width=385,height=140)

    #4
    img3=Image.open(r"images\44.jpg")
    img3=img3.resize((380,140),Image.Resampling.LANCZOS)
    self.photoimg3=ImageTk.PhotoImage(img3)

    self.btn4=Button(self.root,command=self.openimage3,image=self.photoimg3,cursor="hand2")
    self.btn4.place(x=1155,y=0,width=380,height=140)

    #maNAGEFRAME
    manageframe=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
    
    manageframe.place(x=15,y=70,width=1500,height=610)

      #leftframe
    
    dataleftframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text="  Student  Information ",font=("times new roman",20,"bold"),fg="red",bg="white")

    
    dataleftframe.place(x=10,y=0,width=690,height=590)

    img5=Image.open(r"images\36.jpg")
    img5=img5.resize((387,200),Image.Resampling.LANCZOS)
    self.photoimg5=ImageTk.PhotoImage(img5)
    myimg=Label(manageframe,image=self.photoimg5)
    myimg.place(x=710,y=15,width=387,height=200)

    img6=Image.open(r"images\35.jpg")
    img6=img6.resize((387,200),Image.Resampling.LANCZOS)
    self.photoimg6=ImageTk.PhotoImage(img6)
    myimg=Label(manageframe,image=self.photoimg6)
    myimg.place(x=1100,y=15,width=387,height=200)
    btnframe=Frame(dataleftframe,bd=2,relief=RIDGE,bg="green")
    btnframe.place(x=10,y=470,width=660,height=60)
         
    btnfetch=Button(btnframe,command=self.fetchcourseid,text="Fetch ",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btnfetch.grid(row=0,column=0,sticky=W,padx=9,pady=10)

    btnadd=Button(btnframe,command=self.adddata,text="Save",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btnadd.grid(row=0,column=1,sticky=W,padx=9,pady=10)

    btnupdate=Button(btnframe,command=self.updatedata,text="Update",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btnupdate.grid(row=0,column=2,sticky=W,padx=9,pady=10)

    btndelete=Button(btnframe,command=self.deteledata,text="Delete",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btndelete.grid(row=0,column=3,sticky=W,padx=9,pady=10)

    btnclear=Button(btnframe,command=self.cleardata,text="Clear",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btnclear.grid(row=0,column=4,sticky=W,padx=9,pady=10)

    btnexit=Button(btnframe,command=self.exit,text="Exit",font=("times new roman",13,"bold"),width=8,bg="gold",fg="black")
    btnexit.grid(row=0,column=5,sticky=W,padx=9,pady=10)
    #roll no#############################################################################################
    lblroll=Label(dataleftframe,text="Roll no.       :",font=("times new roman",16,"bold"),bg="white")
    lblroll.grid(row=0,column=0,padx=7,pady=10,sticky=W)
    lblroll.place(x=10,y=10)
    lblroll=Label(dataleftframe,text="*",font=("times new roman",20,"bold"),bg="white",fg="red")
    lblroll.grid(row=0,column=0,padx=7,pady=10,sticky=W)

    lblroll.place(x=80,y=7)

    rollentry=ttk.Entry(dataleftframe,textvariable=self.varroll,font=("times new roman",16),width=15)

    rollentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
   
    rollentry.place(x=140,y=10)
    ################unique  id #########################
    lbluniqueid=Label(dataleftframe,text="Unique  I'd     :",font=("times new roman",16,"bold"),bg="white")
    lbluniqueid.grid(row=0,column=2,padx=2,sticky=W)
    lbluniqueid.place(x=350,y=10)
    lbluniqueid=Label(dataleftframe,text="*",font=("times new roman",18,"bold"),bg="white",fg="red")
    lbluniqueid.grid(row=0,column=2,padx=2,sticky=W)
    lbluniqueid.place(x=450,y=7)


    uniqueidentry=ttk.Entry(dataleftframe,textvariable=self.varuniqueid,font=("times new roman",16),width=15)

    uniqueidentry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
   
    uniqueidentry.place(x=500,y=10)
    #################name#########################
    lblname=Label(dataleftframe,text="Name          :",font=("times new roman",16,"bold"),bg="white")
    lblname.grid(row=1,column=0,padx=2,sticky=W)
    lblname.place(x=10,y=60)

    nameentry=ttk.Entry(dataleftframe,textvariable=self.varname,font=("times new roman",16,"bold"),width=15)

    nameentry.grid(row=1,column=1,padx=2,pady=10,sticky=W)
   
    nameentry.place(x=140,y=60)

    ############# gENDER   ###############
    lblgender=Label(dataleftframe,text="Gender           :",font=("times new roman",16,"bold"),bg="white")
    lblgender.grid(row=1,column=2,padx=2,sticky=W)
    lblgender.place(x=350,y=60)

    combogender=ttk.Combobox(dataleftframe,textvariable=self.vargender,font=("arial",11),width=18,state="readonly")
    combogender["value"]=("Select Gender ","Male","Female")
           
    combogender.current(0)
    combogender.grid(row=1,column=3,padx=2,pady=10,sticky=W)
    combogender.place(x=500,y=65)
    ################# dob #########################
    lbldob=Label(dataleftframe,text="D.O.B         :",font=("times new roman",16,"bold"),bg="white")
    lbldob.grid(row=2,column=0,padx=2,sticky=W)
    lbldob.place(x=10,y=110)

    dobentry=ttk.Entry(dataleftframe,textvariable=self.vardob,font=("times new roman",16),width=15)

    dobentry.grid(row=2,column=1,padx=2,pady=10,sticky=W)
   
    dobentry.place(x=140,y=110)
     ################# Blood Group #########################
    lblblood=Label(dataleftframe,text="Blood Group :",font=("times new roman",16,"bold"),bg="white")
    lblblood.grid(row=2,column=2,padx=2,sticky=W)
    lblblood.place(x=350,y=110)

    bloodentry=ttk.Entry(dataleftframe,textvariable=self.varblood,font=("times new roman",16),width=15)

    bloodentry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
   
    bloodentry.place(x=500,y=110)
    ################# Mobile#########################
    lblmobile=Label(dataleftframe,text="Mobile        :",font=("times new roman",16,"bold"),bg="white")
    lblmobile.grid(row=3,column=1,padx=2,sticky=W)
    lblmobile.place(x=10,y=160)

    mobileentry=ttk.Entry(dataleftframe,textvariable=self.varmobile,font=("times new roman",16),width=15)

    mobileentry.grid(row=3,column=1,padx=2,pady=10,sticky=W)
   
    mobileentry.place(x=140,y=160)
    ################# email#########################
    lblemail=Label(dataleftframe,text="Email  I'd       :",font=("times new roman",16,"bold"),bg="white")
    lblemail.grid(row=3,column=2,padx=2,sticky=W)
    lblemail.place(x=350,y=160)

    emailentry=ttk.Entry(dataleftframe,textvariable=self.varemail,font=("times new roman",16),width=15)

    emailentry.grid(row=3,column=3,padx=2,pady=10,sticky=W)
   
    emailentry.place(x=500,y=160)
    ################# address#########################
    lbladdress=Label(dataleftframe,text="Address      :",font=("times new roman",16,"bold"),bg="white")
    lbladdress.grid(row=4,column=0,padx=2,sticky=W)
    lbladdress.place(x=10,y=210)

    addressentry=ttk.Entry(dataleftframe,textvariable=self.varaddress,font=("times new roman",16),width=15)

    addressentry.grid(row=4,column=1,padx=2,pady=10,sticky=W)
   
    addressentry.place(x=140,y=210)
    ################# courseid  #########################
    lblcourseid=Label(dataleftframe,text="Course   I'd    :",font=("times new roman",16,"bold"),bg="white")
    lblcourseid.grid(row=4,column=2,padx=2,sticky=W)
    lblcourseid.place(x=350,y=210)

    courseidentry=ttk.Entry(dataleftframe,textvariable=self.varcourseid,font=("times new roman",16),width=15)
    courseidentry.grid(row=4,column=3,padx=2,pady=10,sticky=W)
   
    courseidentry.place(x=500,y=210)
    ################# course #########################
    lblcourse=Label(dataleftframe,text="Course        :",font=("times new roman",16,"bold"),bg="white")
    lblcourse.grid(row=5,column=0,padx=2,sticky=W)
    lblcourse.place(x=10,y=260)

    courseentry=ttk.Entry(dataleftframe,textvariable=self.varcourse,font=("times new roman",16),width=15,state="readonly")

    courseentry.grid(row=5,column=1,padx=2,pady=10,sticky=W)
   
    courseentry.place(x=140,y=260)
    ################# year  #########################
    lblyear=Label(dataleftframe,text="Year                :",font=("times new roman",16,"bold"),bg="white")
    lblyear.grid(row=5,column=2,padx=2,sticky=W)
    lblyear.place(x=350,y=260)
    yearentry=ttk.Entry(dataleftframe,textvariable=self.varyear,font=("times new roman",16),width=15,state="readonly")
    yearentry.grid(row=5,column=3,padx=2,pady=10,sticky=W)
   
    yearentry.place(x=500,y=260)
    ################# subject1 #########################
    lblsubject1=Label(dataleftframe,text="Subject  1   :",font=("times new roman",16,"bold"),bg="white")
    lblsubject1.grid(row=6,column=0,padx=2,sticky=W)
    lblsubject1.place(x=10,y=310)

    subject1entry=ttk.Entry(dataleftframe,textvariable=self.varsubject1,font=("times new roman",16),width=15,state="readonly")

    subject1entry.grid(row=6,column=1,padx=2,pady=10,sticky=W)
   
    subject1entry.place(x=140,y=310)
    ################# subject2  #########################
    lblsubject2=Label(dataleftframe,text="Subject  2       :",font=("times new roman",16,"bold"),bg="white")
    lblsubject2.grid(row=6,column=2,padx=2,sticky=W)
    lblsubject2.place(x=350,y=310)
    subject2entry=ttk.Entry(dataleftframe,textvariable=self.varsubject2,font=("times new roman",16),width=15,state="readonly")
    subject2entry.grid(row=6,column=3,padx=2,pady=10,sticky=W)
   
    subject2entry.place(x=500,y=310)
    ################# subject3 #########################
    lblsubject3=Label(dataleftframe,text="Subject  3   :",font=("times new roman",16,"bold"),bg="white")
    lblsubject3.grid(row=7,column=0,padx=2,sticky=W)
    lblsubject3.place(x=10,y=360)
    subject3entry=ttk.Entry(dataleftframe,textvariable=self.varsubject3,font=("times new roman",16),width=15,state="readonly")

    subject3entry.grid(row=7,column=1,padx=2,pady=10,sticky=W)
   
    subject3entry.place(x=140,y=360)
    ################# subject4  ########################3
    lblsubject4=Label(dataleftframe,text="Subject  4       :",font=("times new roman",16,"bold"),bg="white")
    lblsubject4.grid(row=7,column=2,padx=2,sticky=W)
    lblsubject4.place(x=350,y=360)
    subject4entry=ttk.Entry(dataleftframe,textvariable=self.varsubject4,font=("times new roman",16),width=15,state="readonly")
    subject4entry.grid(row=7,column=3,padx=2,pady=10,sticky=W)
   
    subject4entry.place(x=500,y=360)
    ################# subject5 #########################
    lblsubject5=Label(dataleftframe,text="Subject  5   :",font=("times new roman",16,"bold"),bg="white")
    lblsubject5.grid(row=8,column=0,padx=2,sticky=W)
    lblsubject5.place(x=10,y=410)
    subject5entry=ttk.Entry(dataleftframe,textvariable=self.varsubject5,font=("times new roman",16),width=15,state="readonly")

    subject5entry.grid(row=8,column=1,padx=2,pady=10,sticky=W)
   
    subject5entry.place(x=140,y=410)
    ################# subject6  ########################3
    lblsubject6=Label(dataleftframe,text="Subject  6       :",font=("times new roman",16,"bold"),bg="white")
    lblsubject6.grid(row=8,column=2,padx=2,sticky=W)
    lblsubject6.place(x=350,y=410)
    subject6entry=ttk.Entry(dataleftframe,textvariable=self.varsubject6,font=("times new roman",16),width=15,state="readonly")
    subject6entry.grid(row=8,column=3,padx=2,pady=10,sticky=W)
   
    subject6entry.place(x=500,y=410)
    
    
    
        



    #rightframe 
           # ############################################################### #rightframe
    datarightframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text=" Student's  Details ",font=("times new roman",20,"bold"),fg="red",bg="white")

    datarightframe.place(x=710,y=220,width=780,height=370)
    btnsframe=Frame(datarightframe,bd=4,relief=RIDGE,padx=2,bg="green")
    btnsframe.place(x=3,y=0,width=765,height=60)

    search=Button(btnsframe,text="Search By :",font=("times new roman",14,"bold"),width=11,bg="gold",fg="black")
    search.grid(row=0,column=0,padx=10,pady=7,sticky=W)
     #search
    self.var_combosearch=StringVar()
    combosearch=ttk.Combobox(btnsframe,textvariable=self.var_combosearch,font=("times new roman",14,"bold"),width=13,state="readonly")
    combosearch["value"]=("Select Options","roll","name","uniqueid","courseid","Course")
    combosearch.current(0)
    combosearch.grid(row=0,column=1,padx=8,pady=7,sticky=W)
    self.var_search=StringVar()

    searchentry=ttk.Entry(btnsframe,textvariable=self.var_search,font=("times new roman",14,"bold"),width=13)

    searchentry.grid(row=0,column=2,padx=8,pady=7,sticky=W)
        

    btnsearch=Button(btnsframe,command=self.searchdata,text="Search",font=("times new roman",14,"bold"),width=10,bg="gold",fg="black")
    btnsearch.grid(row=0,column=3,sticky=W,padx=8,pady=7)

    btnshowall=Button(btnsframe,command=self.fetchdata,text="Show  All",font=("times new roman",14,"bold"),width=10,bg="gold",fg="black")
    btnshowall.grid(row=0,column=4,sticky=W,padx=8,pady=7)
    tableframe=Frame(datarightframe,bd=4,relief=RIDGE)
    tableframe.place(x=0,y=65,width=767,height=265)

    scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
    scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
    self.student_table=ttk.Treeview(tableframe,column=("roll","uniqueid","name","gender","dob","blood","mobile","email","address","courseid","course","year","subject1","subject2","subject3","subject4","subject5","subject6"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    scrollx.pack(side=BOTTOM,fill=X)
    scrolly.pack(side=RIGHT,fill=Y)

    scrollx.config(command=self.student_table.xview)
    scrolly.config(command=self.student_table.yview)
    self.student_table.heading("roll",text="Roll no.")
    self.student_table.heading("uniqueid",text="Unique I'd")
    self.student_table.heading("name",text="Name")
    self.student_table.heading("gender",text="Gender")
    self.student_table.heading("dob",text="D.O.B")
    self.student_table.heading("blood",text="Blood Group")
    self.student_table.heading("mobile",text="Mobile")
    self.student_table.heading("email",text="Email I'd")
    self.student_table.heading("address",text="Address")
    self.student_table.heading("courseid",text="Course I'd")
    self.student_table.heading("course",text="Course")
    self.student_table.heading("year",text="Year")
    self.student_table.heading("subject1",text="Subject 1")
    self.student_table.heading("subject2",text="Subject 2")
    self.student_table.heading("subject3",text="Subject 3")
    self.student_table.heading("subject4",text="Subject 4")
    self.student_table.heading("subject5",text="Subject 5")
    self.student_table.heading("subject6",text="Subject 6")
    self.student_table["show"]="headings"
    self.student_table.column("roll",width=100)
    self.student_table.column("uniqueid",width=150)
    self.student_table.column("name",width=150)
    self.student_table.column("gender",width=150)
    self.student_table.column("dob",width=150)
    self.student_table.column("blood",width=150)
    self.student_table.column("mobile",width=150)
    self.student_table.column("email",width=150)
    self.student_table.column("address",width=150)
    self.student_table.column("courseid",width=150)
    self.student_table.column("course",width=150)
    self.student_table.column("year",width=150)
    self.student_table.column("subject1",width=150)
    self.student_table.column("subject2",width=150)
    self.student_table.column("subject3",width=150)
    self.student_table.column("subject4",width=150)
    self.student_table.column("subject5",width=150)
    self.student_table.column("subject6",width=150)
    self.student_table.pack(fill=BOTH,expand=1)
    self.student_table.bind("<ButtonRelease>",self.getcursor)
    self.fetchdata()
      #mysql#########################################

  def adddata(self):
        if(self.varroll.get()=="" or self.varuniqueid.get()=="" or self.varname.get()=="" or self.varcourseid.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required",parent=self.root)
        else:
            try:

        
                conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                  self.varroll.get(),
                                                                                                  self.varuniqueid.get(),
                                                                                                  self.varname.get(),
                                                                                                  self.vargender.get(),
                                                                                                  self.vardob.get(),
                                                                                                  self.varblood.get(),
                                                                                                  self.varmobile.get(),
                                                                                                  self.varemail.get(),
                                                                                                  self.varaddress.get(),
                                                                                                  self.varcourseid.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  self.varyear.get(),
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
                messagebox.showinfo("Success","Student Information  has been added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


  def fetchdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        mycursor=conn.cursor()
        mycursor.execute("select *from student ")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


  

     #get cursor

 
  def getcursor(self,event=""):
        cursorrow=self.student_table.focus()
        content=self.student_table.item(cursorrow)
        data=content["values"]


        self.varroll.set(data[0])
        self.varuniqueid.set(data[1])
        self.varname.set(data[2])
        self.vargender.set(data[3])
        self.vardob.set(data[4])
        self.varblood.set(data[5])
        self.varmobile.set(data[6])
        self.varemail.set(data[7])
        self.varaddress.set(data[8])
        self.varcourseid.set(data[9])
        self.varcourse.set(data[10])

        self.varyear.set(data[11])
        self.varsubject1.set(data[12])
        self.varsubject2.set(data[13])
        self.varsubject3.set(data[14])
        self.varsubject4.set(data[15])
        self.varsubject5.set(data[16])
        self.varsubject6.set(data[17])

  def updatedata(self):

        if(self.varroll.get()=="" or self.varuniqueid.get()=="" or self.varname.get()=="" or self.varcourseid.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure bto update this Student information",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    mycursor.execute("update student set uniqueid=%s,name=%s,gender=%s,dob=%s,blood=%s,mobile=%s,email=%s,address=%s,courseid=%s,course=%s,year=%s,subject1=%s,subject2=%s,subject3=%s,subject4=%s,subject5=%s,subject6=%s where roll=%s",(
                        
                                                                                                  self.varuniqueid.get(),
                                                                                                  self.varname.get(),
                                                                                                  self.vargender.get(),
                                                                                                  self.vardob.get(),
                                                                                                  self.varblood.get(),
                                                                                                  self.varmobile.get(),
                                                                                                  self.varemail.get(),
                                                                                                  self.varaddress.get(),
                                                                                                  self.varcourseid.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  self.varyear.get(),
                                                                                                  self.varsubject1.get(),
                                                                                                  self.varsubject2.get(),
                                                                                                  self.varsubject3.get(),
                                                                                                  self.varsubject4.get(),
                                                                                                  self.varsubject5.get(),
                                                                                                  self.varsubject6.get(),
                                                                                                  self.varroll.get(),    

                                                                                                  ))        

                else:
                    if not update:
                        return
                conn.commit()
                self.fetchdata()
                conn.close()

                messagebox.showinfo("success","Student Details Updated Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
  def deteledata(self):
        if self.varroll.get()=="":
            messagebox.showerror("Error.....","All Fields Are Required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to Delete this student's information ",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    sql="Delete from student where roll=%s"
                    value=(self.varroll.get(),)
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
        self.varroll.set("")
        self.varuniqueid.set("")
        self.varname.set("")
        self.vargender.set("Select Gender")
        self.vardob.set("")
        self.varblood.set("")
        self.varmobile.set("")
        self.varemail.set("")
        self.varaddress.set("")
        self.varcourseid.set("")
        self.varcourse.set("")
        self.varyear.set("")
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
                mycursor.execute("select * from student where "+str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=mycursor.fetchall()
                if len(data)!=0:
                    
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()



                    

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


        

        
         #openimage
  def openimage(self):
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
    img=Image.open(fln)
    imgbrowse=img.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimgbrowse=ImageTk.PhotoImage(imgbrowse)
    self.btn1.config(image=self.photoimgbrowse)

      #openimage
  def openimage1(self):
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
    img1=Image.open(fln)
    imgbrowse1=img1.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimgbrowse1=ImageTk.PhotoImage(imgbrowse1)
    self.btn2.config(image=self.photoimgbrowse1)

  def fetchcourseid(self):
     if self.varcourseid.get()=="":
      messagebox.showerror("Error","Please Enter course id",parent=self.root)
     else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        mycursor=conn.cursor()
        query=("select course,year,subject1,subject2,subject3,subject4,subject5,subject6 from coursetable where courseid=%s")
        value=(self.varcourseid.get(),)
        mycursor.execute(query,value)
        row=mycursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This course id  not found",parent=self.root)
        else:
          conn.commit()
          conn.close()
          self.varcourse.set(row[0])
          self.varyear.set(row[1])
          self.varsubject1.set(row[2])
          self.varsubject2.set(row[3])
          self.varsubject3.set(row[4])
          self.varsubject4.set(row[5])
          self.varsubject5.set(row[6])
          self.varsubject6.set(row[7])

     






     

  def openimage2(self):
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
    img2=Image.open(fln)
    imgbrowse2=img2.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimgbrowse2=ImageTk.PhotoImage(imgbrowse2)
    self.btn3.config(image=self.photoimgbrowse2)

  def openimage3(self):
    
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
    img3=Image.open(fln)
    imgbrowse3=img3.resize((385,140),Image.Resampling.LANCZOS)
    self.photoimgbrowse3=ImageTk.PhotoImage(imgbrowse3)
    self.btn4.config(image=self.photoimgbrowse3)

  def exit(self):
    self.root.destroy()

  

        





if __name__ == "__main__":
    root=Tk()
    obj=students(root)
    root.mainloop()