from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from PIL.ImageFile import ImageFile
from developer import developer
from student import student
import os
from train import Train
from face_recognition import face_recognition
from attendance import attendace
from help import help
from tkinter import messagebox


class Face_recognization_System :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Face Recognization System")

     

          # first image


        img1=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\dilkap_gate.jpeg")
        img1=img1.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        

        # second image
        
        img=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\middle.jpg")
        img=img.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=520,y=0,width=500,height=130)


        # third image
    

        img2=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\main_building.jpeg")
        img2=img2.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # background image

        img3=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\bg.png")
        img3=img3.resize((1570,790), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1570,height=790)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1570,height=45)

        # time
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000,time)



        lbl = Label(title_lbl,font=('times new roman',14,'bold'),bg='black',fg='white')
        lbl.place(x=0,y=0,width=110,height=50)
        time()









        # student button

        img4=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\student.png")
        img4=img4.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # face detection button
        img5=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\face_detect.png")
        img5=img5.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        # attendance button
        img6=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\attendance.png")
        img6=img6.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)


        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        # help desk button

        img7=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\help_desk.png")
        img7=img7.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)


        b4_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        
        # train data button

        img8=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\train_data.png")
        img8=img8.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_classifier)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)

        # photos button

        img9=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\photo_face.png")
        img9=img9.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)

        # developer button
        
        img10=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\developer.jpg")
        img10=img10.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)


        # exit button
        
        img11=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\exit.jpg")
        img11=img11.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg="#0099FF",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)



    def open_img(self):
        os.startfile("data")

    def iexit(self):
            self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
            if self.exit > 0:
                self.root.destroy()
            else:
                return







        # function buttons

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=student(self.new_window)


    def train_classifier(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)


         
    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=face_recognition(self.new_window)


    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=attendace(self.new_window)

    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=developer(self.new_window)


    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=help(self.new_window)






if __name__=="__main__" :
    root = Tk()
    obj=Face_recognization_System(root)
    root.mainloop()