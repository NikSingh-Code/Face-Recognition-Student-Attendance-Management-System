from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1570,height=45)

        # background image
        img3=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\dbg.png")
        img3=img3.resize((1570,790), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=45,width=1570,height=790)

        # frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1000,y=50,width=500,height=500)

        # Developer information text
        text1 = "Hello, we are the developers of this project."
        text2 = "We are a group of 4 students who are passionate about technology and software development."
        text3 = "We have worked hard to create this Face Recognition Attendance System."
        text4 = "We hope this system will be useful for educational institutions and organizations."
        text5 = "We are committed to providing high-quality software solutions."
        text6 = "We are always looking for ways to improve our skills and knowledge."
        text7 = "Thank you for using our Face Recognition Attendance System."

        Label(main_frame,text=text1,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=20)

        Label(main_frame,text=text2,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=70)

        Label(main_frame,text=text3,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=130)

        Label(main_frame,text=text4,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=190)

        Label(main_frame,text=text5,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=250)

        Label(main_frame,text=text6,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=310)

        Label(main_frame,text=text7,font=("times new roman",15,"bold"),
              bg="white",fg="black",wraplength=450,justify=LEFT).place(x=10,y=370)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()