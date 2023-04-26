from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class newc:

  def  __init__(self,root):

       self.root=root
       self.root.title("Students Academic Record")
       self.root.geometry("700x830+400+0")
       self.root.config(bg="black")

       img4=Image.open(r"images\1.jpg")
       #img4=img4.resize((550,730),Image.Resampling.LANCZOS)
       self.photoimg4=ImageTk.PhotoImage(img4)
       bg_lbl=Label(self.root,image=self.photoimg4,bd=2,relief=RIDGE)
       bg_lbl.place(x=75,y=30,width=550,height=730)

       btn_exit=Button(self.root,command=self.exit,text="Exit",font=("times new roman",20,"bold"),bg="skyblue",fg="black",cursor="hand2",activebackground="skyblue",activeforeground="black")
       btn_exit.place(x=290,y=770,width=100,height=50)

  def exit(self):
        self.root.destroy()
        




if __name__ == "__main__":
    root=Tk()
    obj=newc(root)
    root.mainloop()