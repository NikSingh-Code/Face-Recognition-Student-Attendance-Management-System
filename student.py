from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from PIL.ImageFile import ImageFile
from tkinter import messagebox
import mysql.connector
import cv2



class student :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Face Recognization System")

           # variables

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



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

        title_lbl = Label(bg_img,text=" STUDENTS  ACADEMIC DETAILS MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1570,height=45)

        # student button
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img4=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\student.jpeg")
        img4=img4.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl = Label(Left_frame,image=self.photoimg4)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # current course

        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=120)

        # department


        dep_label = Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","Information Technology","Civil","Mechanical","Electrical","IOT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10)

        # course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # sem

        sem_label = Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # class student details

        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=255,width=720,height=300)

        # student id

        student_id_label = Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_id_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name

        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # student division

        student_div_label = Label(class_student_frame,text="Division:",font=("times new roman",13,"bold"),bg="white")
        student_div_label.grid(row=1,column=0,padx=10,sticky=W)

        student_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # student roll no

        student_roll_label = Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,sticky=W)

        student_roll_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # gender

        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label = Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email

        email_label = Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no

        phone_label = Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # address

        address_label = Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # teacher name
        teacher_label = Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons

        self.var_radio1=StringVar()

        radionbtn1 = Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="YES")
        radionbtn1.grid(row=5,column=0)

         

        radionbtn2 = Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radionbtn2.grid(row=5,column=1)

        # buttons frame

        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=30)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

        button_frame2 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame2.place(x=0,y=240,width=715,height=30)

        take_photo_btn = Button(button_frame2,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=35)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(button_frame2,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=35)
        update_photo_btn.grid(row=0,column=1)

 
        # right label frame
        
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img5=Image.open(r"C:\Users\nikhi\Desktop\face recognition project\college_images\student1.jpg")
        img5=img5.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        f_label = Label(Right_frame,image=self.photoimg5)
        f_label.place(x=5,y=0,width=720,height=130)

        # search system

        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        searcgh_label = Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        searcgh_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        search_btn.grid(row=0,column=3,padx=5)

        showAll_btn = Button(search_frame,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=10)
        showAll_btn.grid(row=0,column=4,padx=5)

        # table frame

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()
  
  
   # function declaration   
   
    
    def  add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)    

        else: 
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Project@2026",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)





# fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Project@2026",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




# get cursor

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

# update function
    
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)    
         else:
            try:
                    Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                        conn = mysql.connector.connect(host="localhost",username="root",password="Project@2026",database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))
                    else:
                        if not Update:
                            return 
                        messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

# delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Project@2026",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


# reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


# generate data set or take photo samples

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)  
        else:
                try:
                            Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                            if Update>0:
                                conn = mysql.connector.connect(host="localhost",username="root",password="Project@2026",database="face_recognizer")
                                my_cursor = conn.cursor()
                                student_id = self.var_std_id.get().strip()

                                

    

                                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                         self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()
                                    ))
                                conn.commit()
                                self.fetch_data()
                                
                                conn.close()




                               # load predefined data on face frontals from opencv

                                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                                def face_cropped(img):
                                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                                    for (x,y,w,h) in faces:
                                        face_cropped = img[y:y+h,x:x+w]
                                        return face_cropped
                                cap = cv2.VideoCapture(0)
                                img_id=0
                                while True:
                                    ret,my_frame = cap.read()
                                    if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face = cv2.resize(face_cropped(my_frame),(450,450))
                                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                                        file_name_path = f"data/user.{student_id}.{img_id}.jpg"

                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("Cropped Face",face)

                                    if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break


                                cap.release()
                                cv2.destroyAllWindows()

                                self.reset_data()

                                messagebox.showinfo("Result","Generating data sets completed!!!",parent=self.root)

                              
                                
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


                                







if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()