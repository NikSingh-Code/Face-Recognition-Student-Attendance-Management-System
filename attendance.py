import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
import csv
from tkinter import filedialog
from tkinter import messagebox


mydata = []

class attendace:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Attendance")

    # text variables
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_dept = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_status = StringVar()
 

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

        title_lbl = Label(bg_img,text="STUDENT ATTENDANCE ",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1570,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white",relief=RIDGE)
        main_frame.place(x=10,y=55,width=1550,height=700)

        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student AttendanceDetails",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img4=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\student.jpeg")
        img4=img4.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f1_lbl = Label(Left_frame,image=self.photoimg4)
        f1_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # Label and entry
        attendanceId_label = Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_id)
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        studentName_label = Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_name)
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # student roll number

        studentRoll_label = Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        studentRoll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentRoll_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_roll)
        studentRoll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # student department
        studentDept_label = Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        studentDept_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentDept_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_dept)
        studentDept_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_time)
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # date
        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        date_entry = Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),bg="white",textvariable=self.var_atten_date)
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance status
        attendanceStatus_label = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendanceStatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),state="readonly",width=18,textvariable=self.var_atten_status)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # buttons 
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")

        btn_frame.place(x=0,y=300,width=715,height=500)

        save_btn = Button(btn_frame,text="Import csv",command=self.import_csv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=10,pady=5)

        update_btn = Button(btn_frame,text="Export csv",command=self.export_csv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10,pady=5)

        delete_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=10,pady=5)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10,pady=5)





 
  




        # right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=500)

        # scroll bar

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","name","roll","dept","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("dept",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("dept",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        # fetch data

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
# import csv

    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

            # export csv

    def export_csv(self):
        try:
              if len(mydata)<1:
               messagebox.showerror("No Data","No Data found to export",parent=self.root)
               return False
              fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
              with open(fln,mode="w",newline="") as myfile:
               exp_write=csv.writer(myfile,delimiter=",")
              for i in mydata:
                exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error","Error occurred while exporting data"+str(es),parent=self.root)



    def get_cursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content["values"]
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_roll.set(rows[2])
            self.var_atten_dept.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_status.set(rows[6])


    def reset_data(self):
                self.var_atten_id.set("")
                self.var_atten_name.set("")
                self.var_atten_roll.set("")
                self.var_atten_dept.set("")
                self.var_atten_time.set("")
                self.var_atten_date.set("")
                self.var_atten_status.set("Status")



    def update_data(self):
     selected = self.AttendanceReportTable.focus()

     if selected == "":
        messagebox.showerror("Error", "Please select a record first", parent=self.root)
        return

      # get updated values
     values = (
        self.var_atten_id.get(),
        self.var_atten_name.get(),
        self.var_atten_roll.get(),
        self.var_atten_dept.get(),
        self.var_atten_time.get(),
        self.var_atten_date.get(),
        self.var_atten_status.get()
    )

      # update table
     self.AttendanceReportTable.item(selected, values=values)

     # update mydata list
     index = self.AttendanceReportTable.index(selected)
     mydata[index] = list(values)

     messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

  








if __name__ == "__main__":

    root = Tk()
    obj = attendace(root)
    
    root.mainloop()