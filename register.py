from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1570x790+0+0")

# ================= Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

# ================= Background =================
        bg=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\bg.png")
        bg=bg.resize((1570,790),Image.Resampling.LANCZOS)
        self.bg=ImageTk.PhotoImage(bg)

        bg_img=Label(self.root,image=self.bg)
        bg_img.place(x=0,y=0,width=1570,height=790)

# ================= Main Frame =================
        frame=Frame(self.root,bg="white")
        frame.place(x=350,y=100,width=900,height=500)

# ================= Left Image =================
        img_left=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\register_left.png")
        img_left=img_left.resize((350,500),Image.Resampling.LANCZOS)
        self.img_left=ImageTk.PhotoImage(img_left)

        left_lbl=Label(frame,image=self.img_left)
        left_lbl.place(x=0,y=0,width=350,height=500)

# ================= Title =================
        title=Label(frame,text="REGISTER HERE",
        font=("times new roman",20,"bold"),
        bg="white",fg="darkgreen")

        title.place(x=380,y=20)

# ================= First Name =================
        Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white").place(x=370,y=80)

        ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13)).place(x=370,y=110,width=200)

# ================= Last Name =================
        Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white").place(x=600,y=80)

        ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13)).place(x=600,y=110,width=200)

# ================= Contact =================
        Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white").place(x=370,y=150)

        ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13)).place(x=370,y=180,width=200)

# ================= Email =================
        Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white").place(x=600,y=150)

        ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13)).place(x=600,y=180,width=200)

# ================= Security Question =================
        Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white").place(x=370,y=220)

        combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13),state="readonly")

        combo_security["values"]=(
        "Select",
        "Your Birth Place",
        "Your Best Friend Name",
        "Your Pet Name"
        )

        combo_security.current(0)
        combo_security.place(x=370,y=250,width=200)

# ================= Security Answer =================
        Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white").place(x=600,y=220)

        ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",13)).place(x=600,y=250,width=200)

# ================= Password =================
        Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white").place(x=370,y=290)

        ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",13),show="*").place(x=370,y=320,width=200)

# ================= Confirm Password =================
        Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white").place(x=600,y=290)

        ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",13),show="*").place(x=600,y=320,width=200)

# ================= Checkbox =================
        self.var_check=IntVar()

        Checkbutton(frame,variable=self.var_check,
        text="I Agree The Terms & Conditions",
        font=("times new roman",12),
        bg="white").place(x=370,y=360)

# ================= Buttons =================
        Button(frame,text="Register Now",
        command=self.register_data,
        font=("times new roman",15,"bold"),
        bg="red",fg="white").place(x=380,y=410,width=150)

        Button(frame,text="Reset",
        command=self.reset_data,
        font=("times new roman",15,"bold"),
        bg="gray",fg="white").place(x=600,y=410,width=150)

# ================= Register Function =================
    def register_data(self):

        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must match")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to terms & conditions")

        else:
            try:
                conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Project@2026",
                database="face_recognizer"
                )

                my_cursor=conn.cursor()

                my_cursor.execute(
                "insert into register (fname,lname,contact,email,securityQ,securityA,password) values (%s,%s,%s,%s,%s,%s,%s)",
                (
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_securityA.get(),
                self.var_pass.get()
                )
                )

                conn.commit()
                conn.close()

                messagebox.showinfo("Success","Registration Successful")

            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}")

# ================= Reset Function =================
    def reset_data(self):

        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_securityQ.set("Select")
        self.var_securityA.set("")
        self.var_pass.set("")
        self.var_confpass.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()