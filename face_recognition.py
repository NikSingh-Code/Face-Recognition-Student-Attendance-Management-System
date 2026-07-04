import os
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime


class face_recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1570x790+0+0")
        self.root.title("Face Recognition")

        # Prevent duplicate attendance
        self.marked_students = set()

        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 35, "bold"),
                          bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1570, height=45)

        # Top Image
        img_top = Image.open(r"college_images\fd_1.png")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Bottom Image
        img_bottom = Image.open(r"college_images\fd_2.png")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        b1_1 = Button(self.root, text="FACE RECOGNITION",
                      command=self.face_recog,
                      cursor="hand2",
                      font=("times new roman", 12, "bold"),
                      bg="red", fg="white")
        b1_1.place(x=630, y=400, width=200, height=40)

    # ================= Attendance =================

    def mark_attendance(self, id, r, n, d):

        with open("attendance.csv", "a+", newline="\n") as f:
            f.seek(0)
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if str(id) not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")

                f.writelines(f"\n{id},{r},{n},{d},{dtString},{d1},Present")

    # ================= Face Recognition =================

    def face_recog(self):

        # MySQL connection outside loop (faster)
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Project@2026",
            database="face_recognizer"
        )
        my_cursor = conn.cursor()

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            features = classifier.detectMultiScale(gray_image, 1.3, 5)

            for (x, y, w, h) in features:

                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                confidence = int((100*(1-predict/300)))

                my_cursor.execute(
                    "SELECT Name, Roll, Dept FROM student WHERE student_id=" + str(id))
                data = my_cursor.fetchone()

                if data:
                    n = data[0]
                    r = data[1]
                    d = data[2]
                else:
                    n = "Unknown"
                    r = "Unknown"
                    d = "Unknown"

                if confidence > 77:

                    cv2.putText(img, f"ID:{id}", (x, y-75),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                    cv2.putText(img, f"Roll:{r}", (x, y-55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                    cv2.putText(img, f"Name:{n}", (x, y-35),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                    cv2.putText(img, f"Dept:{d}", (x, y-15),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                    if id not in self.marked_students:
                        self.mark_attendance(id, r, n, d)
                        self.marked_students.add(id)

                else:

                    cv2.putText(img, "Unknown Face", (x, y-10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

            return img

        def recognize(img, clf, faceCascade):

            img = draw_boundary(img, faceCascade, 1.3, 5, (255, 25, 255), clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:

            ret, img = video_cap.read()

            # Resize frame for faster processing
            img = cv2.resize(img, (640, 480))

            img = recognize(img, clf, faceCascade)

            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:   # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


# ================= Main =================

if __name__ == "__main__":

    root = Tk()
    obj = face_recognition(root)
    root.mainloop()