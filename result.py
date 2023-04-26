from codeop import CommandCompiler
from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk 
from tkinter import filedialog
import os

class resultee:

    def  __init__(self,root):

      self.root=root
      self.root.title("Students Academic Record")
      self.root.geometry("1550x830+0+0")
      self.root.config(bg="white")

      ##################### VARIABLES ######################################
      self.varroll=StringVar()
      self.varuniqueid=StringVar()
      self.varname=StringVar()
      self.vargender=StringVar()
      self.vardob=StringVar()
      self.varmobile=StringVar()
      self.varcourseid=StringVar()
      self.varcourse=StringVar()
      self.varaddress=StringVar()
      self.varyear=StringVar()
      self.varsubject1=StringVar()
      self.varsubject2=StringVar()
      self.varsubject3=StringVar()
      self.varsubject4=StringVar()
      self.varsubject5=StringVar()
      self.varsubject6=StringVar()
      self.varm1=IntVar()
      self.varm2=IntVar()
      self.varm3=IntVar()
      self.varm4=IntVar()
      self.varm5=IntVar()
      self.varm6=IntVar()
      self.vartotalmarks=IntVar()
      self.varfullmarks=IntVar()
      self.varobtainedmarks=IntVar()
      self.varpercentage=DoubleVar()
      

      img4=Image.open(r"images\result.jpeg")
      img4=img4.resize((1530,720),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)
   

      bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
      bg_lbl.place(x=0,y=135,width=1530,height=720)

      lbltitle=Label(bg_lbl,relief=RIDGE,text="MANAGE  STUDENT'S  RESULT ",font=("times new roman",37,"bold"),fg="skyblue",bg="black")
      lbltitle.place(x=0,y=5,width=1530,height=60)

      #1
      img=Image.open(r"images\r1.jpeg")  
      img=img.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      self.btn1=Button(self.root,command=self.openimage,image=self.photoimg,cursor="hand2")
      self.btn1.place(x=0,y=0,width=385,height=140)
      #2
      img1=Image.open(r"images\84.jpg")
      img1=img1.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      self.btn2=Button(self.root,command=self.openimage1,image=self.photoimg1,cursor="hand2")
      self.btn2.place(x=385,y=0,width=385,height=140)
       
       #3
      img2=Image.open(r"images\25.webp")
      img2=img2.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      self.btn3=Button(self.root,command=self.openimage2,image=self.photoimg2,cursor="hand2")
      self.btn3.place(x=770,y=0,width=385,height=140)

      #4
      img3=Image.open(r"images\85.jpeg")
      img3=img3.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      self.btn4=Button(self.root,command=self.openimage3,image=self.photoimg3,cursor="hand2")
      self.btn4.place(x=1155,y=0,width=385,height=140)
       #maNAGEFRAME
      manageframe=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
    
      manageframe.place(x=15,y=70,width=1500,height=610)

      #leftframe
    
      dataleftframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text=" Add  Student's  Result  ",font=("times new roman",20,"bold"),fg="red",bg="white")

    
      dataleftframe.place(x=10,y=0,width=690,height=600)
       
      img5=Image.open(r"images\28.webp")
      img5=img5.resize((780,200),Image.Resampling.LANCZOS)
      self.photoimg5=ImageTk.PhotoImage(img5)
      myimg=Label(manageframe,image=self.photoimg5)
      myimg.place(x=710,y=0,width=780,height=200)

      btnframe=Frame(dataleftframe,bd=2,relief=RIDGE,bg="green")
      btnframe.place(x=7,y=515,width=670,height=45)

      btnfetch=Button(btnframe,command=self.fetchroll,text="Fetch ",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
      btnfetch.grid(row=0,column=0,sticky=W,padx=11,pady=6)
     

      btnadd=Button(btnframe,command=self.adddata,text="Save",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
      btnadd.grid(row=0,column=2,sticky=W,padx=11,pady=6)
      btnupdate=Button(btnframe,command=self.updatedata,text="Update",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
      btnupdate.grid(row=0,column=3,sticky=W,padx=11,pady=6)
      btndelete=Button(btnframe,command=self.deteledata,text="Delete",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
      btndelete.grid(row=0,column=4,sticky=W,padx=11,pady=6)

      btnclear=Button(btnframe,command=self.cleardata,text="Clear",font=("times new roman",13,"bold"),width=10,bg="gold",fg="black")
      btnclear.grid(row=0,column=5,sticky=W,padx=11,pady=6)
        #roll no#############################################################################################
      lblroll=Label(dataleftframe,text="Roll no.       :",font=("times new roman",16,"bold"),bg="white")
      lblroll.grid(row=0,column=0,padx=2,pady=10,sticky=W)

      lblroll.place(x=10,y=10)

      rollentry=ttk.Entry(dataleftframe,textvariable=self.varroll,font=("times new roman",16),width=15)

      rollentry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
   
      rollentry.place(x=140,y=10)
      ################unique  id #########################
      lbluniqueid=Label(dataleftframe,text="Unique  I'd     :",font=("times new roman",16,"bold"),bg="white")
      lbluniqueid.grid(row=0,column=2,padx=2,sticky=W)
      lbluniqueid.place(x=350,y=10)

      uniqueidentry=ttk.Entry(dataleftframe,textvariable=self.varuniqueid,font=("times new roman",16),width=15,state="readonly")

      uniqueidentry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
   
      uniqueidentry.place(x=500,y=10)
      #################name#########################
      lblname=Label(dataleftframe,text="Name          :",font=("times new roman",16,"bold"),bg="white")
      lblname.grid(row=1,column=0,padx=2,sticky=W)
      lblname.place(x=10,y=60)

      nameentry=ttk.Entry(dataleftframe,textvariable=self.varname,font=("times new roman",16),width=15,state="readonly")

      nameentry.grid(row=1,column=1,padx=2,pady=10,sticky=W)
   
      nameentry.place(x=140,y=60)

      ############# gENDER   ###############
      lblgender=Label(dataleftframe,text="Gender           :",font=("times new roman",16,"bold"),bg="white")
      lblgender.grid(row=1,column=2,padx=2,sticky=W)
      lblgender.place(x=350,y=60)

      genderentry=ttk.Entry(dataleftframe,textvariable=self.vargender,font=("times new roman",16),width=15,state="readonly")
           
      
      genderentry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
      genderentry.place(x=500,y=60)
      ################# dob #########################
      lbldob=Label(dataleftframe,text="D.O.B         :",font=("times new roman",16,"bold"),bg="white")
      lbldob.grid(row=2,column=0,padx=2,sticky=W)
      lbldob.place(x=10,y=110)

      dobentry=ttk.Entry(dataleftframe,textvariable=self.vardob,font=("times new roman",16),width=15,state="readonly")

      dobentry.grid(row=2,column=1,padx=2,pady=10,sticky=W)
   
      dobentry.place(x=140,y=110)
       ################# Mobile#########################
      lblmobile=Label(dataleftframe,text="Mobile            :",font=("times new roman",16,"bold"),bg="white")
      lblmobile.grid(row=2,column=2,padx=2,sticky=W)
      lblmobile.place(x=350,y=110)

      mobileentry=ttk.Entry(dataleftframe,textvariable=self.varmobile,font=("times new roman",16),width=15,state="readonly")

      mobileentry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
   
      mobileentry.place(x=500,y=110)
      ################# course  id#########################
      lblcourseid=Label(dataleftframe,text="Course I'd  :",font=("times new roman",16,"bold"),bg="white")
      lblcourseid.grid(row=3,column=1,padx=2,sticky=W)
      lblcourseid.place(x=10,y=160)

      courseidentry=ttk.Entry(dataleftframe,textvariable=self.varcourseid,font=("times new roman",16),width=15,state="readonly")
      courseidentry.grid(row=3,column=1,padx=2,pady=10,sticky=W)
   
      courseidentry.place(x=140,y=160)
      ################# course  #########################
      lblcourse=Label(dataleftframe,text="Course            :",font=("times new roman",16,"bold"),bg="white")
      lblcourse.grid(row=3,column=2,padx=2,sticky=W)
      lblcourse.place(x=350,y=160)
      courseentry=ttk.Entry(dataleftframe,textvariable=self.varcourse,font=("times new roman",16),width=15,state="readonly")

      courseentry.grid(row=3,column=3,padx=2,pady=10,sticky=W)
   
      courseentry.place(x=500,y=160)
      ################# address#########################
      lbladdress=Label(dataleftframe,text="Address      :",font=("times new roman",16,"bold"),bg="white")
      lbladdress.grid(row=4,column=0,padx=2,sticky=W)
      lbladdress.place(x=10,y=210)

      addressentry=ttk.Entry(dataleftframe,textvariable=self.varaddress,font=("times new roman",16),width=15,state="readonly")

      addressentry.grid(row=4,column=1,padx=2,pady=10,sticky=W)
   
      addressentry.place(x=140,y=210)
      ################# year  #########################
      lblyear=Label(dataleftframe,text="Year                :",font=("times new roman",16,"bold"),bg="white")
      lblyear.grid(row=4,column=2,padx=2,sticky=W)
      lblyear.place(x=350,y=210)

      yeardentry=ttk.Entry(dataleftframe,textvariable=self.varyear,font=("times new roman",16),width=15,state="readonly")
      yeardentry.grid(row=4,column=3,padx=2,pady=10,sticky=W)
   
      yeardentry.place(x=500,y=210)
      ################# course #########################
      lblsb1=Label(dataleftframe,text="Subjects   ",font=("times new roman",16,"bold"),bg="white",fg="blue")
      lblsb1.grid(row=5,column=0,padx=2,sticky=W)
      lblsb1.place(x=30,y=250)

      lblsb2=Label(dataleftframe,text="    Marks  ",font=("times new roman",16,"bold"),bg="white",fg="blue")
      lblsb2.grid(row=5,column=1,padx=2,pady=10,sticky=W)
  
      lblsb2.place(x=180,y=250)
      ################# year  #########################
      lblsb3=Label(dataleftframe,text="      Subjects               ",font=("times new roman",16,"bold"),bg="white",fg="blue")
      lblsb3.grid(row=5,column=2,padx=2,sticky=W)
      lblsb3.place(x=350,y=250)
      lblsb4=Label(dataleftframe,text="         Marks              ",font=("times new roman",16,"bold"),bg="white",fg="blue")
      lblsb4.grid(row=5,column=3,padx=2,pady=10,sticky=W)
   
      lblsb4.place(x=500,y=250)
      ################# subject1 #########################
      subject1entry=ttk.Entry(dataleftframe,textvariable=self.varsubject1,font=("times new roman",16),width=15,state="readonly")
      subject1entry.grid(row=6,column=0,padx=2,sticky=W)
      subject1entry.place(x=10,y=300)

      m1entry=ttk.Entry(dataleftframe,textvariable=self.varm1,font=("times new roman",13),width=12)

      m1entry.grid(row=6,column=1,padx=2,pady=10,sticky=W)
   
      m1entry.place(x=200,y=300)
      ################# subject2  #########################
      subject2entry=ttk.Entry(dataleftframe,textvariable=self.varsubject2,font=("times new roman",16),width=15,state="readonly")
      subject2entry.grid(row=6,column=2,padx=2,sticky=W)
      subject2entry.place(x=350,y=300)

      m2entry=ttk.Entry(dataleftframe,textvariable=self.varm2,font=("times new roman",13),width=12)

      m2entry.grid(row=6,column=3,padx=2,pady=10,sticky=W)
   
      m2entry.place(x=550,y=300)
      ################# subject3 #########################
      subject3entry=ttk.Entry(dataleftframe,textvariable=self.varsubject3,font=("times new roman",16),width=15,state="readonly")
      subject3entry.grid(row=7,column=0,padx=2,sticky=W)
      subject3entry.place(x=10,y=350)

      m3entry=ttk.Entry(dataleftframe,textvariable=self.varm3,font=("times new roman",13),width=12)

      m3entry.grid(row=7,column=1,padx=2,pady=10,sticky=W)
   
      m3entry.place(x=200,y=350)
      ################# subject4  ########################3
      subject4entry=ttk.Entry(dataleftframe,textvariable=self.varsubject4,font=("times new roman",16),width=15,state="readonly")
      subject4entry.grid(row=7,column=2,padx=2,sticky=W)
      subject4entry.place(x=350,y=350)

      m4entry=ttk.Entry(dataleftframe,textvariable=self.varm4,font=("times new roman",13),width=12)

      m4entry.grid(row=7,column=3,padx=2,pady=10,sticky=W)
   
      m4entry.place(x=550,y=350)
      ################# subject5 #########################
      subject5entry=ttk.Entry(dataleftframe,textvariable=self.varsubject5,font=("times new roman",16),width=15,state="readonly")
      subject5entry.grid(row=8,column=0,padx=2,sticky=W)
      subject5entry.place(x=10,y=400)

      m5entry=ttk.Entry(dataleftframe,textvariable=self.varm5,font=("times new roman",13),width=12)

      m5entry.grid(row=8,column=1,padx=2,pady=10,sticky=W)
   
      m5entry.place(x=200,y=400)
      ################# subject6  ########################3
      subject6entry=ttk.Entry(dataleftframe,textvariable=self.varsubject6,font=("times new roman",16),width=15,state="readonly")
      subject6entry.grid(row=8,column=2,padx=2,sticky=W)
      subject6entry.place(x=350,y=400)

      m6entry=ttk.Entry(dataleftframe,textvariable=self.varm6,font=("times new roman",13),width=12)

      m6entry.grid(row=8,column=3,padx=2,pady=10,sticky=W)
   
      m6entry.place(x=550,y=400)
      ################# totalmarks#########################
      btntotalmarks=Button(dataleftframe,text="Full  Marks : ",font=("times new roman",11,"bold"),width=18,bg="skyblue",fg="black")
      btntotalmarks.grid(row=9,column=0,sticky=W,padx=2,pady=7)
      btntotalmarks.place(x=350,y=440)
      totalmarksentry=ttk.Entry(dataleftframe,textvariable=self.varfullmarks,font=("times new roman",14),width=12)

      totalmarksentry.grid(row=9,column=1,padx=2,pady=10,sticky=W)
   
      totalmarksentry.place(x=200,y=440)
      ################# totalmarks#########################
      btnfullmarks=Button(dataleftframe,text="Total Marks : ",font=("times new roman",11,"bold"),width=18,bg="skyblue",fg="black")
      btnfullmarks.grid(row=9,column=2,sticky=W,padx=2,pady=7)
      btnfullmarks.place(x=10,y=440)
      fullmarksentry=ttk.Entry(dataleftframe,textvariable=self.vartotalmarks,font=("times new roman",14),width=12)

      fullmarksentry.grid(row=9,column=3,padx=2,pady=10,sticky=W)
   
      fullmarksentry.place(x=550,y=440)
      ################# obtainedmarks#########################
      btnobtainedmarks=Button(dataleftframe,command=self.obtain,text="Obtained  Marks : ",font=("times new roman",13,"bold"),width=16,bg="skyblue",fg="black")
      btnobtainedmarks.grid(row=10,column=0,sticky=W,padx=2,pady=7)
      btnobtainedmarks.place(x=10,y=475)
      obtainedmarksentry=ttk.Entry(dataleftframe,textvariable=self.varobtainedmarks,font=("times new roman",14),width=12)

      obtainedmarksentry.grid(row=10,column=1,padx=2,pady=10,sticky=W)
      obtainedmarksentry.place(x=200,y=475)
      ################# percentage  #########################
      btnpercentage=Button(dataleftframe,command=self.per,text="Percentage : ",font=("times new roman",11,"bold"),width=18,bg="skyblue",fg="black")
      btnpercentage.grid(row=10,column=2,sticky=W,padx=2,pady=7)
      btnpercentage.place(x=350,y=475)
      percentageentry=ttk.Entry(dataleftframe,textvariable=self.varpercentage,font=("times new roman",14),width=12)

      percentageentry.grid(row=10,column=3,padx=2,pady=10,sticky=W)
      percentageentry.place(x=550,y=475)
       #rightframe 
           # ############################################################### #rightframe
      datarightframe=LabelFrame(manageframe,bd=4,relief=RIDGE,padx=2,text=" Student's  Result  Details ",font=("times new roman",20,"bold"),fg="red",bg="white")

      datarightframe.place(x=710,y=220,width=780,height=380)
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
      tableframe.place(x=0,y=65,width=767,height=275)
      scrollx=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
      scrolly=ttk.Scrollbar(tableframe,orient=VERTICAL)
      self.result_table=ttk.Treeview(tableframe,column=("roll","uniqueid","name","gender","dob","mobile","courseid","course","address","year","subject1","subject2","subject3","subject4","subject5","subject6","m1","m2","m3","m4","m5","m6","totalmarks","fullmarks","obtainedmarks","percentage"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
      scrollx.pack(side=BOTTOM,fill=X)
      scrolly.pack(side=RIGHT,fill=Y)
      scrollx.config(command=self.result_table.xview)
      scrolly.config(command=self.result_table.yview)
      self.result_table.heading("roll",text="Roll no.")
      self.result_table.heading("uniqueid",text="Unique I'd")
      self.result_table.heading("name",text="Name")
      self.result_table.heading("gender",text="Gender")
      self.result_table.heading("dob",text="D.O.B")
      self.result_table.heading("mobile",text="Mobile")
      self.result_table.heading("courseid",text="Course I'd")
      self.result_table.heading("course",text="Course")
      self.result_table.heading("address",text="Address")
      self.result_table.heading("year",text="Year")
      self.result_table.heading("subject1",text="Subject 1")
      self.result_table.heading("subject2",text="Subject 2")
      self.result_table.heading("subject3",text="Subject 3")
      self.result_table.heading("subject4",text="Subject 4")
      self.result_table.heading("subject5",text="Subject 5")
      self.result_table.heading("subject6",text="Subject 6")
      self.result_table.heading("m1",text="Marks  1")
      self.result_table.heading("m2",text="Marks  2")
      self.result_table.heading("m3",text="Marks  3")
      self.result_table.heading("m4",text="Marks  4")
      self.result_table.heading("m5",text="Marks  5")
      self.result_table.heading("m6",text="Marks  6")
      self.result_table.heading("totalmarks",text="Total Marks")
      self.result_table.heading("fullmarks",text="Full Marks")
      self.result_table.heading("obtainedmarks",text="Obtained Marks")
      self.result_table.heading("percentage",text="Percentage")

      self.result_table["show"]="headings"
      self.result_table.column("roll",width=100)
      self.result_table.column("uniqueid",width=150)
      self.result_table.column("name",width=150)
      self.result_table.column("gender",width=150)
      self.result_table.column("dob",width=150)
      self.result_table.column("mobile",width=150)
      self.result_table.column("courseid",width=150)
      self.result_table.column("course",width=150)
      self.result_table.column("address",width=150)
      self.result_table.column("year",width=150)
      self.result_table.column("subject1",width=150)
      self.result_table.column("subject2",width=150)
      self.result_table.column("subject3",width=150)
      self.result_table.column("subject4",width=150)
      self.result_table.column("subject5",width=150)
      self.result_table.column("subject6",width=150)
      self.result_table.column("m1",width=150)
      self.result_table.column("m2",width=150)
      self.result_table.column("m3",width=150)
      self.result_table.column("m4",width=150)
      self.result_table.column("m5",width=150)
      self.result_table.column("m6",width=150)
      self.result_table.column("totalmarks",width=150)
      self.result_table.column("fullmarks",width=150)

      self.result_table.column("obtainedmarks",width=150)
      self.result_table.column("percentage",width=150)
      
      self.result_table.pack(fill=BOTH,expand=1)
      self.result_table.bind("<ButtonRelease>",self.getcursor)
      self.fetchdata()

    def adddata(self):
        if(self.varroll.get()=="" or self.varuniqueid.get()=="" or self.varname.get()=="" or self.varcourseid.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required")
        else:
            try:

        
                conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                mycursor=conn.cursor()
                mycursor.execute("insert into result values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                  self.varroll.get(),
                                                                                                  self.varuniqueid.get(),
                                                                                                  self.varname.get(),
                                                                                                  self.vargender.get(),
                                                                                                  self.vardob.get(),
                                                                                            
                                                                                                  self.varmobile.get(),
                                                                                                  
                                                                                                  
                                                                                                  self.varcourseid.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  self.varaddress.get(),
                                                                                                  self.varyear.get(),
                                                                                                  self.varsubject1.get(),
                                                                                                  self.varsubject2.get(),
                                                                                                  self.varsubject3.get(),
                                                                                                  self.varsubject4.get(),
                                                                                                  self.varsubject5.get(),
                                                                                                  self.varsubject6.get(),
                                                                                                  self.varm1.get(),
                                                                                                  self.varm2.get(),
                                                                                                  self.varm3.get(),
                                                                                                  self.varm4.get(),
                                                                                                  self.varm5.get(),
                                                                                                  self.varm6.get(),
                                                                                                  self.vartotalmarks.get(),
                                                                                                  self.varfullmarks.get(),
                                                                                                  self.varobtainedmarks.get(),
                                                                                                  self.varpercentage.get(),
                                                                                                  
                                                                                                  

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
        mycursor.execute("select *from result ")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.result_table.delete(*self.result_table.get_children())
            for i in data:
                self.result_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def getcursor(self,event=""):
        cursorrow=self.result_table.focus()
        content=self.result_table.item(cursorrow)
        data=content["values"]


        self.varroll.set(data[0])
        self.varuniqueid.set(data[1])
        self.varname.set(data[2])
        self.vargender.set(data[3])
        self.vardob.set(data[4])
        
        self.varmobile.set(data[5])
        
        
        self.varcourseid.set(data[6])
        self.varcourse.set(data[7])
        self.varaddress.set(data[8])
        self.varyear.set(data[9])
        self.varsubject1.set(data[10])
        self.varsubject2.set(data[11])
        self.varsubject3.set(data[12])
        self.varsubject4.set(data[13])
        self.varsubject5.set(data[14])
        self.varsubject6.set(data[15])
        self.varm1.set(data[16])
        self.varm2.set(data[17])
        self.varm3.set(data[18])
        self.varm4.set(data[19])
        self.varm5.set(data[20])
        self.varm6.set(data[21])
        self.vartotalmarks.set(data[22])
        self.varfullmarks.set(data[23])

        self.varobtainedmarks.set(data[24])
        self.varpercentage.set(data[25])

    

        
        
        
        
    
    def updatedata(self):

        if(self.varroll.get()=="" or self.varuniqueid.get()=="" or self.varname.get()=="" or self.varcourseid.get()==""):
            messagebox.showerror("Error.....","All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure bto update this courses information",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    mycursor.execute("update result set uniqueid=%s,name=%s,gender=%s,dob=%s,mobile=%s,courseid=%s,course=%s,address=%s,year=%s,subject1=%s,subject2=%s,subject3=%s,subject4=%s,subject5=%s,subject6=%s,m1=%s,m2=%s,m3=%s,m4=%s,m5=%s,m6=%s,totalmarks=%s,fullmarks=%s,obtainedmarks=%s,percentage=%s where roll=%s",(
                        
                                                                                                  self.varuniqueid.get(),
                                                                                                  self.varname.get(),
                                                                                                  self.vargender.get(),
                                                                                                  self.vardob.get(),
                                                                                                  
                                                                                                  self.varmobile.get(),
                                                                                                  
                                                                                                  
                                                                                                  self.varcourseid.get(),
                                                                                                  self.varcourse.get(),
                                                                                                  self.varaddress.get(),
                                                                                                  self.varyear.get(),
                                                                                                  self.varsubject1.get(),
                                                                                                  self.varsubject2.get(),
                                                                                                  self.varsubject3.get(),
                                                                                                  self.varsubject4.get(),
                                                                                                  self.varsubject5.get(),
                                                                                                  self.varsubject6.get(),
                                                                                                  self.varm1.get(),
                                                                                                  self.varm2.get(),
                                                                                                  self.varm3.get(),
                                                                                                  self.varm4.get(),
                                                                                                  self.varm5.get(),
                                                                                                  self.varm6.get(),
                                                                                                  self.vartotalmarks.get(),
                                                                                                  self.varfullmarks.get(),
                                                                                                  self.varobtainedmarks.get(),
                                                                                                  self.varpercentage.get(),
                                                                                                  self.varroll.get(),


                                                                                                      

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
        if self.varroll.get()=="":
            messagebox.showerror("Error.....","All Fields Are Required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to Delete this courses",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                    mycursor=conn.cursor()
                    sql="Delete from result where roll=%s"
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
    def obtain(self):
        self.varobtainedmarks=(self.varm1.get()+self.varm2.get()+self.varm3.get()+self.varm4.get()+self.varm5.get()+self.varm6.get())
    def per(Self):
        self.varpercentage=(self.varobtainedmarks/self.vartotalmarks)*100
    def cleardata(self):
        self.varroll.set("")
        self.varuniqueid.set("")
        self.varname.set("")
        self.vargender.set("")
        self.vardob.set("")
        self.varmobile.set("")
        
        
        self.varcourseid.set("")
        self.varcourse.set("")
        self.varaddress.set("")
        self.varyear.set("")
        self.varsubject1.set("")
        self.varsubject2.set("")
        self.varsubject3.set("")
        self.varsubject4.set("")
        self.varsubject5.set("")
        self.varsubject6.set("")
        self.varm1.set("")
        self.varm2.set("")
        self.varm3.set("")
        self.varm4.set("")
        self.varm5.set("")
        self.varm6.set("")
        self.vartotalmarks.set("")
        self.varfullmarks.set("")

        self.varobtainedmarks.set("")
        self.varpercentage.set("")

    

    
    def fetchroll(self):

     if self.varroll.get()=="":
      messagebox.showerror("Error","Please Enter roll number",parent=self.root)
     else:
        conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
        mycursor=conn.cursor()
        query=("select uniqueid,name,gender,dob,mobile,courseid,course,address,year,subject1,subject2,subject3,subject4,subject5,subject6 from student where roll=%s")
        value=(self.varroll.get(),)
        mycursor.execute(query,value)
        row=mycursor.fetchone()

        if row==None:
          messagebox.showerror("Error","This number not found",parent=self.root)
        else:
          conn.commit()
          conn.close()
          self.varuniqueid.set(row[0])
          self.varname.set(row[1])
          self.vargender.set(row[2])
          self.vardob.set(row[3])
          self.varmobile.set(row[4])
          self.varcourseid.set(row[5])
          self.varcourse.set(row[6])
          self.varaddress.set(row[7])
          self.varyear.set(row[8])
          self.varsubject1.set(row[9])
          self.varsubject2.set(row[10])
          self.varsubject3.set(row[11])
          self.varsubject4.set(row[12])
          self.varsubject5.set(row[13])
          self.varsubject6.set(row[14])
    def searchdata(self):
        if self.var_combosearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please Select Option")

        else:

            
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="tiger@123",database="project")
                mycursor=conn.cursor()
                mycursor.execute("select * from result where "+str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=mycursor.fetchall()
                if len(data)!=0:
                    
                    self.result_table.delete(*self.result_table.get_children())
                    for i in data:
                        self.result_table.insert("",END,values=i)
                    conn.commit()
                conn.close()



                    

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


        

  
     


    def openimage(self):
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
      img=Image.open(fln)
      imgbrowse=img.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimgbrowse=ImageTk.PhotoImage(imgbrowse)
      self.btn1.config(image=self.photoimgbrowse)

    def openimage1(self):
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All Files","*.*")),parent=self.root)
      img1=Image.open(fln)
      imgbrowse1=img1.resize((385,140),Image.Resampling.LANCZOS)
      self.photoimgbrowse1=ImageTk.PhotoImage(imgbrowse1)
      self.btn2.config(image=self.photoimgbrowse1)

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




if __name__ == "__main__":
    root=Tk()
    obj=resultee(root)
    root.mainloop()