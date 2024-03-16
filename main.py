from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1400x800+0+0")
    self.root.title("face Recognition System")



    #Here i added image for SBUP
    #first image SBUP logo
    img1=Image.open(r"P:\Python Project\SBUPMAIN.jpeg")
    img1=img1.resize((400,130),Image.Resampling.LANCZOS)
    self.photoimg1=ImageTk.PhotoImage(img1)

    sbup_Flag=Label(self.root,image=self.photoimg1)
    sbup_Flag.place(x=0,y=0,width=400,height=130)


    #Second image SBUP logo
    img2=Image.open(r"P:\Python Project\SBUPSCREEN.png")
    img2=img2.resize((560,130),Image.Resampling.LANCZOS)
    self.photoimg2=ImageTk.PhotoImage(img2)

    sbup_Flag=Label(self.root,image=self.photoimg2)
    sbup_Flag.place(x=400,y=0,width=560,height=130)
   
    #Third image SBUP logo
    img3=Image.open(r"P:\Python Project\SBUPMAIN.jpeg")
    img3=img3.resize((400,130),Image.Resampling.LANCZOS)
    self.photoimg3=ImageTk.PhotoImage(img3)

    sbup_Flag=Label(self.root,image=self.photoimg3)
    sbup_Flag.place(x=960,y=0,width=400,height=130)


    #BAckground under SBUP
    img4=Image.open(r"P:\Python Project\MAINSCREEN\WHITEBG.png")
    img4=img4.resize((1400,700),Image.Resampling.LANCZOS)
    self.photoimg4=ImageTk.PhotoImage(img4)

    bg_Sbup=Label(self.root,image=self.photoimg4)
    bg_Sbup.place(x=0,y=130,width=1400,height=700)


    #Making SBUP title
    title_lbl=Label(bg_Sbup,text="FACE RECOGNITION SMART ATTENDANCE",font=("times new roman",35,"bold"),bg="white",fg="blue")
    title_lbl.place(x=0,y=0,width=1400,height=45)


    #Making STUDENT Button1
    img5=Image.open(r"P:\Python Project\BUTTONS\STUDENTBT.png")
    img5=img5.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg5=ImageTk.PhotoImage(img5)

    b1=Button(bg_Sbup,image=self.photoimg5,cursor="hand2")
    b1.place(x=150,y=100,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=150,y=300,width="220",height="40")



    
 #Making DETECT FACE Button2
    img6=Image.open(r"P:\Python Project\BUTTONS\FACERECOG.png")
    img6=img6.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg6=ImageTk.PhotoImage(img6)

    b1=Button(bg_Sbup,image=self.photoimg6,cursor="hand2")
    b1.place(x=425,y=100,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=425,y=300,width="220",height="40")


    #Making ATTENDANCE Button3
    img7=Image.open(r"P:\Python Project\BUTTONS\ATTENDANCE.png")
    img7=img7.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg7=ImageTk.PhotoImage(img7)

    b1=Button(bg_Sbup,image=self.photoimg7,cursor="hand2")
    b1.place(x=710,y=100,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=710,y=300,width="220",height="40")

    #Making HELP Button4
    img8=Image.open(r"P:\Python Project\BUTTONS\HELPDESK.png")
    img8=img8.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg8=ImageTk.PhotoImage(img8)

    b1=Button(bg_Sbup,image=self.photoimg8,cursor="hand2")
    b1.place(x=1000,y=100,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=1000,y=300,width="220",height="40")


    #making TRAIN DATA button5
    img9=Image.open(r"P:\Python Project\BUTTONS\TRAINDATA.png")
    img9=img9.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg9=ImageTk.PhotoImage(img9)

    b1=Button(bg_Sbup,image=self.photoimg9,cursor="hand2")
    b1.place(x=150,y=350,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=150,y=550,width="220",height="40")



    #making PHOTOS DATA button6
    img10=Image.open(r"P:\Python Project\BUTTONS\PHOTODATA.png")
    img10=img10.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg10=ImageTk.PhotoImage(img10)

    b1=Button(bg_Sbup,image=self.photoimg10,cursor="hand2")
    b1.place(x=425,y=350,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Photos Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=425,y=550,width="220",height="40")
    

    #making DEVELOPER  button7
    img11=Image.open(r"P:\Python Project\BUTTONS\DEV.png")
    img11=img11.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg11=ImageTk.PhotoImage(img11)

    b1=Button(bg_Sbup,image=self.photoimg11,cursor="hand2")
    b1.place(x=710,y=350,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Devloper",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=710,y=550,width="220",height="40")

    #making EXIT button8
    img12=Image.open(r"P:\Python Project\BUTTONS\EXIT.png")
    img12=img12.resize((220,220),Image.Resampling.LANCZOS)
    self.photoimg12=ImageTk.PhotoImage(img12)

    b1=Button(bg_Sbup,image=self.photoimg12,cursor="hand2")
    b1.place(x=1000,y=350,width="220",height="220")

    b1_1=Button(bg_Sbup,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=1000,y=550,width="220",height="40")




if __name__ == "__main__":
  root=Tk()
  obj=Face_Recognition_System(root)
  root.mainloop()