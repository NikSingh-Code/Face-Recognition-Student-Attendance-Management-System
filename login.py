from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import  Face_recognization_System
from register import Register


 # ================= LOGIN PAGE =================
class Login:

    def __init__(self,root):

        self.root=root
        self.root.title("Login")
        self.root.geometry("1570x790+0+0")

# Background
        img=Image.open("college_images/bg.png")
        img=img.resize((1570,790))
        self.bg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1570,height=790)

# Login Frame
        frame=Frame(bg_img,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

# Login Logo
        img1=Image.open("college_images/login.png")
        img1=img1.resize((200,200))
        self.img1=ImageTk.PhotoImage(img1)

        Label(frame,image=self.img1,bg="black").place(x=80,y=0,width=170,height=170)

# Username
        Label(frame,text="Email",
              font=("times new roman",15,"bold"),
              bg="black",
              fg="white").place(x=80,y=170)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=80,y=200,width=220)

# Password
        Label(frame,text="Password",
              font=("times new roman",15,"bold"),
              bg="black",
              fg="white").place(x=80,y=240)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15),show="*")
        self.txtpass.place(x=80,y=270,width=220)

# Login Button
        Button(frame,
               text="Login",
               command=self.login,
               font=("times new roman",15,"bold"),
               bg="#2F80ED",
               fg="white").place(x=110,y=320,width=120)

# Register Button
        Button(frame,
               text="New User? Register",
               command=self.register_window,
               font=("times new roman",10,"bold"),
               bg="black",
               fg="white",
               borderwidth=0).place(x=90,y=360)

# Forgot Password
        Button(frame,
               text="Forgot Password?",
               command=self.forgot_password_window,
               font=("times new roman",10,"bold"),
               bg="black",
               fg="white",
               borderwidth=0).place(x=95,y=390)


# ================= OPEN REGISTER =================
    def register_window(self):
        self.new_window=Toplevel(self.root)
        Register(self.new_window)


# ================= LOGIN FUNCTION =================
    def login(self):

        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")

        else:
            try:
                conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Project@2026",
                    database="face_recognizer"
                )

                cur=conn.cursor()

                cur.execute(
                "select * from register where email=%s and password=%s",
                (self.txtuser.get(),self.txtpass.get()))

                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","Invalid Email or Password")

                else:
                    messagebox.showinfo("Success","Login Successful")

                    self.root.destroy()
                    root = Tk()
                    Face_recognization_System(root)
                    root.mainloop()

                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error:{str(es)}")


# ================= IMPROVED FORGOT PASSWORD UI =================
    def forgot_password_window(self):

        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter your Email ID first")

        else:

            self.root2=Toplevel(self.root)
            self.root2.title("Reset Password")
            self.root2.geometry("450x450+500+200")
            self.root2.config(bg="white")

# Title
            Label(self.root2,
                  text="Reset Your Password",
                  font=("times new roman",20,"bold"),
                  bg="white",
                  fg="darkgreen").place(x=100,y=30)

# Security Question
            Label(self.root2,
                  text="Select Security Question",
                  font=("times new roman",13),
                  bg="white").place(x=60,y=120)

            self.combo_security=ttk.Combobox(self.root2,
                                             font=("times new roman",13),
                                             state="readonly")

            self.combo_security["values"]=(
                "Select",
                "Your Birth Place",
                "Your Best Friend Name",
                "Your Pet Name"
            )

            self.combo_security.current(0)
            self.combo_security.place(x=60,y=150,width=320)

# Security Answer
            Label(self.root2,
                  text="Enter Security Answer",
                  font=("times new roman",13),
                  bg="white").place(x=60,y=200)

            self.txt_security=ttk.Entry(self.root2,
                                        font=("times new roman",13))

            self.txt_security.place(x=60,y=230,width=320)

# New Password
            Label(self.root2,
                  text="Enter New Password",
                  font=("times new roman",13),
                  bg="white").place(x=60,y=280)

            self.txt_newpass=ttk.Entry(self.root2,
                                       font=("times new roman",13),
                                       show="*")

            self.txt_newpass.place(x=60,y=310,width=320)

# Reset Button
            Button(self.root2,
                   text="Reset Password",
                   command=self.reset_password,
                   font=("times new roman",14,"bold"),
                   bg="green",
                   fg="white",
                   cursor="hand2").place(x=150,y=370,width=150)


# ================= RESET PASSWORD =================
    def reset_password(self):

        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Project@2026",
                database="face_recognizer"
            )

            cur=conn.cursor()

            cur.execute(
            "select * from register where email=%s and securityQ=%s and securityA=%s",
            (self.txtuser.get(),
             self.combo_security.get(),
             self.txt_security.get()))

            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Incorrect details")

            else:

                cur.execute(
                "update register set password=%s where email=%s",
                (self.txt_newpass.get(),self.txtuser.get()))

                conn.commit()

                messagebox.showinfo("Success","Password Reset Successful")
                self.root2.destroy()

            conn.close()

        except Exception as es:
            messagebox.showerror("Error",f"Error:{str(es)}")


# ================= REGISTER PAGE =================
class Register:

    def __init__(self,root):

        self.root=root
        self.root.title("Register")
        self.root.geometry("1570x790+0+0")

# Background
        bg=Image.open("college_images/bg.png")
        bg=bg.resize((1570,790))
        self.bg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1570,height=790)

# Main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=350,y=100,width=900,height=500)

# Left Image
        img_left=Image.open("college_images/register_left.png")
        img_left=img_left.resize((350,500))
        self.img_left=ImageTk.PhotoImage(img_left)

        Label(frame,image=self.img_left).place(x=0,y=0,width=350,height=500)

# Title
        Label(frame,
              text="REGISTER HERE",
              font=("times new roman",20,"bold"),
              bg="white",
              fg="darkgreen").place(x=380,y=20)

# First Name
        Label(frame,text="First Name",bg="white").place(x=370,y=80)
        ttk.Entry(frame).place(x=370,y=110,width=200)

# Last Name
        Label(frame,text="Last Name",bg="white").place(x=600,y=80)
        ttk.Entry(frame).place(x=600,y=110,width=200)

# Contact
        Label(frame,text="Contact No",bg="white").place(x=370,y=150)
        ttk.Entry(frame).place(x=370,y=180,width=200)

# Email
        Label(frame,text="Email",bg="white").place(x=600,y=150)
        ttk.Entry(frame).place(x=600,y=180,width=200)

# Security Question
        Label(frame,text="Select Security Questions",bg="white").place(x=370,y=220)

        combo=ttk.Combobox(frame,state="readonly")
        combo["values"]=(
            "Select",
            "Your Birth Place",
            "Your Best Friend Name",
            "Your Pet Name"
        )
        combo.current(0)
        combo.place(x=370,y=250,width=200)

# Security Answer
        Label(frame,text="Security Answer",bg="white").place(x=600,y=220)
        ttk.Entry(frame).place(x=600,y=250,width=200)

# Password
        Label(frame,text="Password",bg="white").place(x=370,y=290)
        ttk.Entry(frame,show="*").place(x=370,y=320,width=200)

# Confirm Password
        Label(frame,text="Confirm Password",bg="white").place(x=600,y=290)
        ttk.Entry(frame,show="*").place(x=600,y=320,width=200)

# Terms Checkbox
        Checkbutton(frame,
                    text="I Agree The Terms & Conditions",
                    bg="white").place(x=370,y=360)

# Register Button
        Button(frame,
               text="Register Now",
               bg="red",
               fg="white",
               font=("times new roman",13,"bold")).place(x=400,y=410,width=150)

# Login Button
        Button(frame,
               text="Login Now",
               bg="#2F80ED",
               fg="white",
               font=("times new roman",13,"bold"),
               command=self.back_login).place(x=600,y=410,width=150)

    def back_login(self):
        self.root.destroy()


# ================= MAIN =================
if __name__ == "__main__":

    root=Tk()
    Login(root)
    root.mainloop()