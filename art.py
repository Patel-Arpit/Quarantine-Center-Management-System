from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql

class Patient():
    def __init__(self, root):
        self.root = root
        self.root.title("Quarantine center management system")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="white")

        # =====BD Image======
        self.bg1 = ImageTk.PhotoImage(file="F:/xj/co27.jpg")

        bg1 = Label(self.root, image=self.bg1).place(x=0, y=0, relwidth=1, relheight=1)



        frame1 = Frame(self.root, bg="aquamarine", bd=60)
        frame1.place(x=100, y=630, height=150, width=300)

        reg_btn = Button(frame1, text="Registration", fg="red", bg="aquamarine", activebackground="aquamarine", bd=0,
                         cursor="hand2", command=self.home,
                         font=("times new roman", 22)).place(x=85, y=-25, width=145, height=70)

        self.bg5 = ImageTk.PhotoImage(file="F:/xj/LL1.jpg")
        bg5 = Label(frame1, image=self.bg5).place(x=-60, y=-110, width=130, height=250)

        frame2 = Frame(self.root, bg="aquamarine", bd=60)
        frame2.place(x=650, y=630, height=150, width=300)

        reg_btn = Button(frame2, text="Relative's \n & \n Payment \n Information", fg="red", bg="aquamarine", activebackground="aquamarine", bd=0,
                         cursor="hand2", command=self.relpay,
                         font=("times new roman", 19)).place(x=90, y=-35, width=130, height=110)

        self.bg6 = ImageTk.PhotoImage(file="F:/xj/r1.jpg")
        bg6 = Label(frame2, image=self.bg6).place(x=-60, y=-60, width=130, height=150)

        frame3 = Frame(self.root, bg="aquamarine", bd=60)
        frame3.place(x=1150, y=630, height=150, width=300)

        reg_btn = Button(frame3, text="Doctor \n Information", fg="red", activebackground="aquamarine", bg="aquamarine", bd=0,
                         cursor="hand2", command=self.doctor_window,
                         font=("times new roman", 19)).place(x=90, y=-40, width=130, height=110)

        self.bg7 = ImageTk.PhotoImage(file="F:/xj/doc.jfif")
        bg7 = Label(frame3, image=self.bg7).place(x=-60, y=-60, width=130, height=150)





    def home(self):
        self.root = root
        self.root.title("Quarantine center management system")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="white")

        # =======All Variable======
        self.Patient_var = StringVar()
        self.Name_var = StringVar()
        self.Test_ID = StringVar()
        self.Gender_var = StringVar()
        self.Age_var = StringVar()
        self.Phone_var = StringVar()
        self.Doctor_var = StringVar()
        self.Room_var = StringVar()
        self.Relative_var = StringVar()
        self.AdmissionDate_var = StringVar()
        self.DischargeDate_var = StringVar()
        self.Bill_var = StringVar()
        self.Death_var = StringVar()
        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =====Bg Image===
        self.bg = ImageTk.PhotoImage(file="F:/xj/back.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # =====Left Image===
        self.left = ImageTk.PhotoImage(file="F:/xj/do.png")
        left = Label(self.root, image=self.left).place(x=60, y=70, width=400, height=700)

        h1 = Frame(self.root, bg="white")
        h1.place(x=60, y=0, width=410, height=70)

        ho1 = Label(h1, text="QCMS", width=100, pady=10, bd=0, bg="white", font=("times new roman", 35, "bold"),
                    fg="darkorange").place(x=70, y=0, width=200)

        title_frame = Frame(self.root, bg="khaki")
        title_frame.place(x=460, y=0, width=1000, height=70)

        docinfotn = Button(title_frame, text="Doctors info", width=10, pady=5, bd=0, command=self.doctor_window,
                           font=("times new roman", 16, "bold")).place(x=150,
                                                                       y=13,
                                                                       width=130)

        relpaytn = Button(title_frame, text="Relative & Payment", width=70, pady=5, bd=0, command=self.relpay,
                          font=("times new roman", 16, "bold")).place(x=350,
                                                                      y=13,
                                                                      width=200)

        # ======Register Frame=====
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=460, y=70, width=1000, height=700)

        frame3 = Frame(self.root, bg="white")
        frame3.place(x=460, y=75, width=930, height=50)

        title = Label(frame3, text="REGISTRATION", bg="white", fg="orange",
                      font=("times new roman", 25, "bold"))
        title.place(x=350, y=7)

        m_title = Label(frame1, text="PATIENT INFO", bg="khaki", fg="black", font=("times new roman", 18, "bold"))
        m_title.grid(row=1, columnspan=2, pady=20)

        patient_id = Label(frame1, text="Patient ID :", bg="white", fg="black",
                           font=("times new roman", 17, "bold"))
        patient_id.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_patient = Entry(frame1, textvariable=self.Patient_var, font=("times new roman", 13, "bold"), bd=2,
                            bg="lightgray",
                            relief=GROOVE)
        txt_patient.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        name = Label(frame1, text="Name :", bg="white", fg="black", font=("times new roman", 17, "bold"))
        name.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(frame1, textvariable=self.Name_var, font=("times new roman", 13, "bold"), bd=2, bg="lightgray",
                         relief=GROOVE)
        txt_name.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        Test_id = Label(frame1, text="                Test ID :", bg="white", fg="black",
                        font=("times new roman", 17, "bold"))
        Test_id.grid(row=2, column=3, pady=10, padx=20, sticky="w")
        txt_test = Entry(frame1, textvariable=self.Test_ID, font=("times new roman", 13, "bold"), bd=2, bg="lightgray",
                         relief=GROOVE)
        txt_test.grid(row=2, column=4, pady=10, padx=20, sticky="w")

        Phone = Label(frame1, text="                Phone No. :", bg="white", fg="black",
                      font=("times new roman", 17, "bold"))
        Phone.grid(row=3, column=3, pady=10, padx=20, sticky="w")
        txt_phone = Entry(frame1, textvariable=self.Phone_var, font=("times new roman", 13, "bold"), bd=2,
                          bg="lightgray",
                          relief=GROOVE)
        txt_phone.grid(row=3, column=4, pady=10, padx=20, sticky="w")

        gender = Label(frame1, text="Gender :", bg="white", fg="black", font=("times new roman", 17, "bold"))
        gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(frame1, textvariable=self.Gender_var, font=("times new roman", 12, "bold"),
                                    state='readonly', justify=CENTER)
        combo_gender['values'] = ("Male", "Female", "other")
        combo_gender.grid(row=4, column=2, pady=10, padx=20)

        doctor = Label(frame1, text="                Doctor :", bg="white", fg="black",
                       font=("times new roman", 17, "bold"))
        doctor.grid(row=4, column=3, pady=10, padx=20, sticky="w")
        combo_doctor = ttk.Combobox(frame1, textvariable=self.Doctor_var, font=("times new roman", 12, "bold"),
                                    state='readonly')
        combo_doctor['values'] = ("Dr.Omkar", "Dr.Himanshu", "Dr.Prutha", "Dr.Vardhil")
        combo_doctor.grid(row=4, column=4, pady=10, padx=20)

        room_no = Label(frame1, text="Room No. :", bg="white", fg="black", font=("times new roman", 17, "bold"))
        room_no.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_room = Entry(frame1, textvariable=self.Room_var, font=("times new roman", 13, "bold"), bd=2, bg="lightgray",
                         relief=GROOVE)
        txt_room.grid(row=5, column=2, pady=10, padx=20, sticky="w")

        Relative = Label(frame1, text="                Relative's No. :", bg="white", fg="black",
                         font=("times new roman", 17, "bold"))
        Relative.grid(row=5, column=3, pady=10, padx=20, sticky="w")
        txt_Relative = Entry(frame1, textvariable=self.Relative_var, font=("times new roman", 13, "bold"), bd=2,
                             bg="lightgray",
                             relief=GROOVE)
        txt_Relative.grid(row=5, column=4, pady=10, padx=20, sticky="w")

        Age = Label(frame1, text="Age :", bg="white", fg="black",
                    font=("times new roman", 17, "bold"))
        Age.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_age = Entry(frame1, textvariable=self.Age_var, font=("times new roman", 13, "bold"), bd=2, bg="lightgray",
                        relief=GROOVE)
        txt_age.grid(row=6, column=2, pady=10, padx=20, sticky="w")

        Admission_date = Label(frame1, text="                Admission Date :", bg="white", fg="black",
                               font=("times new roman", 17, "bold"))
        Admission_date.grid(row=6, column=3, pady=10, padx=20, sticky="w")
        txt_admission = Entry(frame1, textvariable=self.AdmissionDate_var, font=("times new roman", 13, "bold"), bd=2,
                              bg="lightgray",
                              relief=GROOVE)
        txt_admission.grid(row=6, column=4, pady=10, padx=20, sticky="w")

        Discharge_date = Label(frame1, text="                Discharge Date :", bg="white", fg="black",
                               font=("times new roman", 17, "bold"))
        Discharge_date.grid(row=7, column=3, pady=10, padx=20, sticky="w")
        txt_dischange = Entry(frame1, textvariable=self.DischargeDate_var, font=("times new roman", 13, "bold"), bd=2,
                              bg="lightgray",
                              relief=GROOVE)
        txt_dischange.grid(row=7, column=4, pady=10, padx=20, sticky="w")

        address = Label(frame1, text="Address :", bg="white", fg="black", font=("times new roman", 17, "bold"))
        address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(frame1, width=30, height=3, font=("times new roman", 9, "bold"), bg="lightgray")
        self.txt_address.grid(row=7, column=2, pady=10, padx=20, sticky="w")

        bill = Label(frame1, text="Bill Number :", bg="white", fg="black",
                     font=("times new roman", 17, "bold"))
        bill.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        txt_bill = Entry(frame1, textvariable=self.Bill_var, font=("times new roman", 13, "bold"), bd=2, bg="lightgray",
                         relief=GROOVE)
        txt_bill.grid(row=8, column=2, pady=10, padx=20, sticky="w")

        death = Label(frame1, text="                Death :", bg="white", fg="black",
                      font=("times new roman", 17, "bold"))
        death.grid(row=8, column=3, pady=10, padx=20, sticky="w")
        combo_death = ttk.Combobox(frame1, textvariable=self.Death_var, font=("times new roman", 12, "bold"),
                                   state='readonly', justify=CENTER)
        combo_death['values'] = ("YES", "NO")
        combo_death.grid(row=8, column=4, pady=10, padx=20)

        # =======btn frame==========
        addbtn = Button(self.root, text="ADD", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.add_patients).place(x=70, y=670, width=80)
        updatebtn = Button(self.root, text="UPDATE", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.update_data).place(x=170, y=670,
                                                                                                       width=80)
        deletebtn = Button(self.root, text="DELETE", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.delete_data).place(x=270, y=670,
                                                                                                       width=80)
        clearbtn = Button(self.root, text="CLEAR", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.clear).place(x=370, y=670, width=80)

        details_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="seagreen2")
        details_Frame.place(x=460, y=510, width=1000, height=260)

        lbl_search = Label(details_Frame, text="Search By", bg="seagreen2", fg="tomato2",
                           font=("times new roman", 18, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(details_Frame, textvariable=self.Search_by, font=("times new roman", 14, "bold"),
                                    width=10, state='readonly')
        combo_search['values'] = ("Patient_ID", "Name ")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(details_Frame, textvariable=self.Search_txt, font=("times new roman", 13, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(details_Frame, text="Search", width=8, pady=5, command=self.search_data).grid(row=0,
                                                                                                         column=4,
                                                                                                         padx=5, pady=5)
        showallbtn = Button(details_Frame, text="Search all", width=8, pady=5, command=self.fetch_data).grid(
            row=0, column=5, padx=5, pady=5)

        # =======Table Frame=========
        table_Frame = Frame(details_Frame, bd=0, relief=RIDGE, bg="white")
        table_Frame.place(x=0, y=55, width=990, height=200)

        scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame, orient=VERTICAL)

        self.Patient_table = ttk.Treeview(table_Frame, column=(
            "Patient Id", "Name", "Test_ID", "Phone No.", "Gender", "Doctor", "Room No.", "Relative's No", "Age",
            "Address", "Admission Date", "Discharge Date", "Bill_NO", "Death"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Patient_table.xview)
        scroll_y.config(command=self.Patient_table.yview)

        self.Patient_table.heading("Patient Id", text="Patient ID")
        self.Patient_table.heading("Name", text="Name")
        self.Patient_table.heading("Test_ID", text="Test ID")
        self.Patient_table.heading("Phone No.", text="Phone No.")
        self.Patient_table.heading("Gender", text="Gender")
        self.Patient_table.heading("Doctor", text="Doctor")
        self.Patient_table.heading("Room No.", text="Room No.")
        self.Patient_table.heading("Relative's No", text="Relative's No.")
        self.Patient_table.heading("Age", text="Age")
        self.Patient_table.heading("Admission Date", text="Admission Date")
        self.Patient_table.heading("Discharge Date", text="Discharge Date")
        self.Patient_table.heading("Address", text="Address")
        self.Patient_table.heading("Bill_NO", text="Bill Number")
        self.Patient_table.heading("Death", text="Death")

        self.Patient_table['show'] = 'headings'
        self.Patient_table.column("Patient Id", width=150)
        self.Patient_table.column("Name", width=100)
        self.Patient_table.column("Test_ID", width=100)
        self.Patient_table.column("Phone No.", width=100)
        self.Patient_table.column("Gender", width=100)
        self.Patient_table.column("Doctor", width=100)
        self.Patient_table.column("Room No.", width=100)
        self.Patient_table.column("Relative's No", width=100)
        self.Patient_table.column("Age", width=100)
        self.Patient_table.column("Admission Date", width=150)
        self.Patient_table.column("Discharge Date", width=150)
        self.Patient_table.column("Address", width=150)
        self.Patient_table.column("Bill_NO", width=150)
        self.Patient_table.column("Death", width=100)

        self.Patient_table.pack(fill=BOTH, expand=1)
        self.Patient_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_patients(self):
        if self.Test_ID.get() == "" or self.Name_var == "":
            messagebox.showerror("Error", "all fields are required to fill ")
        else:
            con = pymysql.connect(host="localhost", user="root", database="c_patient")
            cur = con.cursor()
            cur.execute("INSERT INTO C_PATIENT VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.Patient_var.get(),
                         self.Name_var.get(),
                         self.Test_ID.get(),
                         self.Phone_var.get(),
                         self.Gender_var.get(),
                         self.Doctor_var.get(),
                         self.Room_var.get(),
                         self.Relative_var.get(),
                         self.Age_var.get(),
                         self.txt_address.get('1.0',
                                              END),
                         self.AdmissionDate_var.get(),
                         self.DischargeDate_var.get(),
                         self.Bill_var.get(),
                         self.Death_var.get()
                         ))
            

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success", "Recored has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM C_PATIENT")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Patient_table.delete(*self.Patient_table.get_children())
            for row in rows:
                self.Patient_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        curosor_row = self.Patient_table.focus()
        contents = self.Patient_table.item(curosor_row)
        row = contents['values']
        self.Patient_var.set(row[0])
        self.Name_var.set(row[1])
        self.Test_ID.set(row[2])
        self.Phone_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Doctor_var.set(row[5])
        self.Room_var.set(row[6])
        self.Relative_var.set(row[7])
        self.Age_var.set(row[8])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[9])
        self.AdmissionDate_var.set(row[10])
        self.DischargeDate_var.set(row[11])
        self.Bill_var.set(row[12])
        self.Death_var.set(row[13])

    def clear(self):
        self.Patient_var.set("")
        self.Name_var.set("")
        self.Test_ID.set("")
        self.Phone_var.set("")
        self.Gender_var.set("")
        self.Doctor_var.set("")
        self.Room_var.set("")
        self.Relative_var.set("")
        self.Age_var.set("")
        self.txt_address.delete("1.0", END)
        self.AdmissionDate_var.set("")
        self.DischargeDate_var.set("")
        self.Bill_var.set("")
        self.Death_var.set("")

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute(
            "update c_patient set name=%s, test_id=%s,phone=%s,gender=%s,doctor=%s,room_no=%s,relatives_no=%s,age=%s,"
            "address=%s,admission=%s,discharge=%s, bill_number=%s where patient_id=%s", (
                self.Name_var.get(),
                self.Test_ID.get(),
                self.Phone_var.get(),
                self.Gender_var.get(),
                self.Doctor_var.get(),
                self.Room_var.get(),
                self.Relative_var.get(),
                self.Age_var.get(),
                self.txt_address.get('1.0',
                                     END),
                self.AdmissionDate_var.get(),
                self.DischargeDate_var.get(),
                self.Bill_var.get(),
                self.Patient_var.get()))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success", "Recored has been updated")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("DELETE FROM C_PATIENT WHERE patient_id=%s", self.Patient_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM C_PATIENT WHERE " + str(self.Search_by.get()) + " LIKE"
                                                                                   " '%" + str(
            self.Search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Patient_table.delete(*self.Patient_table.get_children())
            for row in rows:
                self.Patient_table.insert('', END, values=row)
            con.commit()
        con.close()

        # =====2 window=====

    def doctor_window(self):
        self.top = Toplevel()
        self.top.title("Doctor Information")
        self.top.geometry("1530x850+0+0")
        self.top.config(bg="white")

        h1 = Frame(self.top, bg="white")
        h1.place(x=0, y=0, width=300, height=70)

        ho1 = Button(h1, text="QCMS", width=100, pady=10, bd=0, bg="white", font=("times new roman", 30, "bold"),
                     fg="darkorange").place(x=70, y=0, width=200)

        title_frane = Frame(self.top, bg="khaki")
        title_frane.place(x=300, y=0, width=1000, height=70)

        title = Label(title_frane, text="DOCTOR DETAILS ", bg="khaki", fg="black", font=("times new roman", 25, "bold"))
        title.place(x=350, y=17)

        self.do1 = ImageTk.PhotoImage(file="F:/xj/doct.jpg")
        do1 = Label(self.top, image=self.do1).place(x=30, y=120, width=230, height=250)

        d1 = Frame(self.top, bg="white")
        d1.place(x=260, y=120, width=500, height=250)

        do_name = Label(d1, text="Name : Dr.Omkar", bg="white", fg="black",
                           font=("times new roman", 19, "bold")).place(x=5, y=15)

        do_degree = Label(d1, text="(MBBS,MD)", bg="white", fg="black",
                           font=("times new roman", 11, "bold")).place(x=210, y=25)

        do_room = Label(d1, text="Cabin : A-11", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=58)

        do_timing = Label(d1, text="Timing : 7:00 am to 10:30 am", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=100)

        do_timing = Label(d1, text="Contact Details : ", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=140)

        do_phone = Label(d1, text="Phone No. : 9686881915", bg="white", fg="black",
                          font=("times new roman", 17, "bold")).place(x=20, y=170)

        do_email = Label(d1, text="Email ID : omi@gmail.com", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=200)

        self.do2 = ImageTk.PhotoImage(file="F:/xj/do1.jpg")
        do2 = Label(self.top, image=self.do1).place(x=30, y=420, width=230, height=250)

        d2 = Frame(self.top, bg="white")
        d2.place(x=260, y=420, width=500, height=250)

        do_name = Label(d2, text="Name : Dr.Himanshu", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=15)

        do_degree = Label(d2, text="(MBBS,General Physician)", bg="white", fg="black",
                          font=("times new roman", 11, "bold")).place(x=210, y=25)

        do_room = Label(d2, text="Cabin : B-19", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=58)

        do_timing = Label(d2, text="Timing : 10:00 am to 3:30 pm", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=100)

        do_timing = Label(d2, text="Contact Details : ", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=140)

        do_phone = Label(d2, text="Phone No. : 6555499521", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=170)

        do_email = Label(d2, text="Email ID : himanshu@gmail.com", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=200)

        self.do3 = ImageTk.PhotoImage(file="F:/xj/do1.jpg")
        do3 = Label(self.top, image=self.do1).place(x=770, y=120, width=230, height=250)

        d3 = Frame(self.top, bg="white")
        d3.place(x=1000, y=120, width=500, height=250)
        do_name = Label(d3, text="Name : Dr.Vardhil", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=15)

        do_degree = Label(d3, text="(MBBS,General Physician)", bg="white", fg="black",
                          font=("times new roman", 11, "bold")).place(x=210, y=25)

        do_room = Label(d3, text="Cabin : C-13", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=58)

        do_timing = Label(d3, text="Timing : 3:00 pm to 8:30 pm", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=100)

        do_timing = Label(d3, text="Contact Details : ", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=140)

        do_phone = Label(d3, text="Phone No. : 7995572226", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=170)

        do_email = Label(d3, text="Email ID : vardhil@gmail.com", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=200)

        self.do4 = ImageTk.PhotoImage(file="F:/xj/doctm.png")
        do4 = Label(self.top, image=self.do1).place(x=770, y=420, width=230, height=250)

        d4 = Frame(self.top, bg="white")
        d4.place(x=1000, y=420, width=500, height=250)
        do_name = Label(d4, text="Name : Dr.Prutha", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=15)

        do_degree = Label(d4, text="(MBBS,MD)", bg="white", fg="black",
                          font=("times new roman", 11, "bold")).place(x=210, y=25)

        do_room = Label(d4, text="Cabin : D-8", bg="white", fg="black",
                        font=("times new roman", 19, "bold")).place(x=5, y=58)

        do_timing = Label(d4, text="Timing : 8:00 pm to 11:30 pm", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=100)

        do_timing = Label(d4, text="Contact Details : ", bg="white", fg="black",
                          font=("times new roman", 19, "bold")).place(x=5, y=140)

        do_phone = Label(d4, text="Phone No. : 9875533365", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=170)

        do_email = Label(d4, text="Email ID : prutha@gmail.com", bg="white", fg="black",
                         font=("times new roman", 17, "bold")).place(x=20, y=200)

        # ====== RELATIVES & PAUMENT =======

    def relpay(self):
        self.rele = Toplevel()
        self.rele.title("Doctor Information")
        self.rele.geometry("1530x850+0+0")
        self.rele.config(bg="white")

        h1 = Frame(self.rele, bg="white")
        h1.place(x=0, y=0, width=300, height=70)

        ho1 = Button(h1, text="QCMS", width=100, pady=10, bd=0, bg="white", font=("times new roman", 30, "bold"),
                     fg="darkorange").place(x=70, y=0, width=200)

        title_frane = Frame(self.rele, bg="khaki")
        title_frane.place(x=300, y=0, width=1000, height=70)

        title = Label(title_frane, text="RELATIVE'S & PAYMENT DETAILS ", bg="khaki", fg="black",
                      font=("times new roman", 25, "bold"))
        title.place(x=350, y=17)

        rel = Frame(self.rele, bg="palegreen", bd=10)
        rel.place(x=5, y=70, width=1520, height=450)

        r_title = Label(rel, text="Relative's Info :", bg="khaki", fg="black",
                        font=("times new roman", 21, "bold"))
        r_title.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # =====variables=======
        self.name = StringVar()
        self.patientid = StringVar()
        self.type = StringVar()
        self.phone_no = StringVar()
        self.email = StringVar()
        self.search = StringVar()
        self.search_t = StringVar()

        patient_id = Label(rel, text="Patient ID :", bg="palegreen", fg="black",
                           font=("times new roman", 17, "bold"))
        patient_id.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_patient = Entry(rel, textvariable=self.patientid, font=("times new roman", 13, "bold"), bd=2,
                            bg="lightgray",
                            relief=GROOVE)
        txt_patient.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        r_name = Label(rel, text="Relative Name :", bg="palegreen", fg="black",
                       font=("times new roman", 17, "bold"))
        r_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txtr_name = Entry(rel, textvariable=self.name, font=("times new roman", 13, "bold"), bd=2,
                          bg="lightgray",
                          relief=GROOVE)
        txtr_name.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        r_ph = Label(rel, text="Phone :", bg="palegreen", fg="black",
                     font=("times new roman", 17, "bold"))
        r_ph.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txtr_ph = Entry(rel, textvariable=self.phone_no, font=("times new roman", 13, "bold"), bd=2,
                        bg="lightgray",
                        relief=GROOVE)
        txtr_ph.grid(row=5, column=2, pady=10, padx=20, sticky="w")

        r_email = Label(rel, text="Email :", bg="palegreen", fg="black",
                        font=("times new roman", 17, "bold"))
        r_email.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txtr_email = Entry(rel, textvariable=self.email, font=("times new roman", 13, "bold"), bd=2,
                           bg="lightgray",
                           relief=GROOVE)
        txtr_email.grid(row=6, column=2, pady=10, padx=20, sticky="w")

        r_address = Label(rel, text="Address :", bg="palegreen", fg="black", font=("times new roman", 17, "bold"))
        r_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.r_address = Text(rel, width=20, height=3, font=("times new roman", 13, "bold"), bg="lightgray")
        self.r_address.grid(row=7, column=2, pady=10, padx=20, sticky="w")

        r_type = Label(rel, text="Relative type :", bg="palegreen", fg="black",
                       font=("times new roman", 17, "bold"))
        r_type.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txtr_type = Entry(rel, textvariable=self.type, font=("times new roman", 13, "bold"), bd=2,
                          bg="lightgray",
                          relief=GROOVE)
        txtr_type.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        addbtn = Button(self.rele, text="ADD", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.relative_details).place(x=70, y=470,
                                                                                                            width=80)

        updatebtn = Button(self.rele, text="UPDATE", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.update_data_relative).place(x=170,
                                                                                                                y=470,
                                                                                                                width=80)

        deletebtn = Button(self.rele, text="DELETE", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.delete_data_relative).place(
            x=270, y=470,
            width=80)
        clearbtn = Button(self.rele, text="CLEAR", width=10, pady=5, bd=1, fg="darkorange", bg="white", command=self.clear_relative).place(x=370,
                                                                                                              y=470,
                                                                                                              width=80)

        details_Frame = Frame(self.rele, bd=2, relief=RIDGE, bg="white")
        details_Frame.place(x=480, y=80, width=1030, height=380)

        lbl_search = Label(details_Frame, text="Search By", bg="white", fg="tomato2",
                           font=("times new roman", 18, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(details_Frame, textvariable=self.search, font=("times new roman", 14, "bold"),
                                    width=10, state='readonly')
        combo_search['values'] = ("Patient_ID", "name ")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(details_Frame, textvariable=self.search_t, font=("times new roman", 13, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(details_Frame, text="Search", width=8, pady=5, bd=1, command=self.search_data_relative).grid(row=0,
                                                                                                                  column=4,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        showallbtn = Button(details_Frame, text="Search all", width=8, pady=5, bd=1, command=self.fetch_relative).grid(
            row=0, column=5, padx=5, pady=5)

        # =======Table Frame=========
        table_Frame = Frame(details_Frame, bd=0, relief=RIDGE, bg="white")
        table_Frame.place(x=20, y=55, width=990, height=320)

        scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame, orient=VERTICAL)

        self.Patient_table = ttk.Treeview(table_Frame, column=(
            "Patient Id", "Name", "Type", "Phone No.", "Email", "Address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Patient_table.xview)
        scroll_y.config(command=self.Patient_table.yview)

        self.Patient_table.heading("Patient Id", text="Patient ID")
        self.Patient_table.heading("Name", text="Name")
        self.Patient_table.heading("Type", text="Type")
        self.Patient_table.heading("Phone No.", text="Phone Number")
        self.Patient_table.heading("Email", text="Email ID")
        self.Patient_table.heading("Address", text="Address")

        self.Patient_table['show'] = 'headings'
        self.Patient_table.column("Patient Id", width=150)
        self.Patient_table.column("Name", width=100)
        self.Patient_table.column("Type", width=100)
        self.Patient_table.column("Phone No.", width=150)
        self.Patient_table.column("Email", width=150)
        self.Patient_table.column("Address", width=150)

        self.Patient_table.pack(fill=BOTH, expand=1)
        self.Patient_table.bind("<ButtonRelease-1>", self.get_cursor_relative)
        self.fetch_relative()

        #=========Payment table=====

        self.Patient_id = StringVar()
        self.Bill_number = StringVar()
        self.Amount = StringVar()
        self.search_pay = StringVar()
        self.searchall_pay = StringVar()

        pay = Frame(self.rele, bg="lightgreen", bd=10)
        pay.place(x=5, y=525, width=1520, height=260)

        pay_title = Label(pay, text="Payment Details :", bg="khaki", fg="black",
                          font=("times new roman", 21, "bold"))
        pay_title.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        patient_id = Label(pay, text="Patient ID :", bg="lightgreen", fg="black",
                           font=("times new roman", 17, "bold"))
        patient_id.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_patient = Entry(pay,textvariable=self.Patient_id, font=("times new roman", 13, "bold"), bd=2,
                            bg="lightgray",
                            relief=GROOVE)
        txt_patient.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        bill_num = Label(pay, text="Bill Number :", bg="lightgreen", fg="black",
                         font=("times new roman", 17, "bold"))
        bill_num.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_bnum = Entry(pay, textvariable=self.Bill_number, font=("times new roman", 13, "bold"), bd=2,
                         bg="lightgray",
                         relief=GROOVE)
        txt_bnum.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        amount = Label(pay, text="Amount :", bg="lightgreen", fg="black",
                       font=("times new roman", 17, "bold"))
        amount.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_amount = Entry(pay, textvariable=self.Amount, font=("times new roman", 13, "bold"), bd=2,
                           bg="lightgray",
                           relief=GROOVE)
        txt_amount.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        addbtn = Button(pay, text="ADD", width=10, pady=5, bd=1, fg="darkorange", bg="white",
                        command=self.payment_details).place(x=70, y=210,
                                                             width=80)

        updatebtn = Button(pay, text="UPDATE", width=10, pady=5, bd=1, fg="darkorange", bg="white",
                           command=self.update_data_payment).place(x=170,
                                                                    y=210,
                                                                    width=80)

        deletebtn = Button(pay, text="DELETE", width=10, pady=5, bd=1, fg="darkorange", bg="white",
                           command=self.delete_data_payment).place(
            x=270, y=210,
            width=80)
        clearbtn = Button(pay, text="CLEAR", width=10, pady=5, bd=1, fg="darkorange", bg="white",
                          command=self.clear_payment).place(x=370,
                                                             y=210,
                                                             width=80)


        frm_pay = Frame(pay, bg="white", bd=10)
        frm_pay.place(x=470, y=0, width=1020, height=240)

        lbl_search = Label(frm_pay, text="Search By", bg="white", fg="tomato2",
                           font=("times new roman", 18, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(frm_pay, textvariable=self.search_pay, font=("times new roman", 14, "bold"),
                                    width=10, state='readonly')
        combo_search['values'] = ("Patient_ID", "name ")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(frm_pay, textvariable=self.searchall_pay, font=("times new roman", 13, "bold"), width=20,
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(frm_pay, text="Search", width=8, pady=5, bd=1, command=self.search_data_payment).grid(row=0,
                                                                                                                  column=4,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        showallbtn = Button(frm_pay, text="Search all", width=8, pady=5,bd=1, command=self.fetch_payment).grid(
            row=0, column=5, padx=5, pady=5)

        frm_pay1 = Frame(frm_pay, bg="khaki", bd=10)
        frm_pay1.place(x=10, y=45, width=980, height=180)

        self.Payment_table = ttk.Treeview(frm_pay1, column=(
            "Patient Id", "Bill number", "Amount"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Payment_table.xview)
        scroll_y.config(command=self.Payment_table.yview)

        self.Payment_table.heading("Patient Id", text="Patient ID")
        self.Payment_table.heading("Bill number", text="Bill Number")
        self.Payment_table.heading("Amount", text="Amount")

        self.Payment_table['show'] = 'headings'
        self.Payment_table.column("Patient Id", width=150)
        self.Payment_table.column("Bill number", width=150)
        self.Payment_table.column("Amount", width=150)

        self.Payment_table.pack(fill=BOTH, expand=1)
        #self.Patient_table.bind("<ButtonRelease-1>", self.get_cursor_payment)
        self.fetch_payment()

    def payment_details(self):
        if self.Patient_id.get() == "":
            messagebox.showerror("Error", "all fields are required to fill ")
        else:
            con = pymysql.connect(host="localhost", user="root", database="c_patient")
            cur = con.cursor()
            cur.execute("INSERT INTO PAYMENT VALUES (%s,%s,%s)", (self.Patient_id.get(),
                                                                  self.Bill_number.get(),
                                                                  self.Amount.get()))

            con.commit()
            self.fetch_payment()
            self.clear_payment()
            messagebox.showinfo("success", "Recored has been inserted")

    def fetch_payment(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM PAYMENT")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Payment_table.delete(*self.Payment_table.get_children())
            for row in rows:
                self.Payment_table.insert('', END, values=row)
            con.commit()
        con.close()

    '''def get_cursor_payment(self, ev):
        curosor_row = self.Payment_table.focus()
        contents = self.Payment_table.item(curosor_row)
        row = contents['values']
        self.Patient_id.set(row[0])
        self.Bill_number.set(row[1])
        self.Amount.set(row[2])'''

    def clear_payment(self):
        self.Patient_id.set("")
        self.Bill_number.set("")
        self.Amount.set("")

    def search_data_payment(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM PAYMENT WHERE " + str(self.search_pay.get()) + " LIKE"
                                                                                " '%" + str(self.searchall_pay.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Payment_table.delete(*self.Payment_table.get_children())
            for row in rows:
                self.Payment_table.insert('', END, values=row)
            con.commit()
        con.close()

    def delete_data_payment(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("DELETE FROM PAYMENT WHERE patient_id=%s", self.Patient_id.get())
        con.commit()
        con.close()
        self.fetch_payment()
        self.clear_payment()

    def update_data_payment(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("UPDATE PAYMENT SET bill_number=%s, amount=%s WHERE patient_id=%s", (
            self.Bill_number.get(),
            self.Amount.get()))
        con.commit()
        self.fetch_payment()
        self.clear_payment()
        con.close()
        messagebox.showinfo("success", "Recored has been inserted")


    #===============relatives=================

    def relative_details(self):
        if self.email.get() == "" or self.name == "":
            messagebox.showerror("Error", "All fields are required to fill ")
        else:
            con = pymysql.connect(host="localhost", user="root", database="c_patient")
            cur = con.cursor()
            cur.execute("INSERT INTO RELATIVES VALUES (%s,%s,%s,%s,%s,%s)", (self.patientid.get(),
                                                                             self.name.get(),
                                                                             self.type.get(),
                                                                             self.phone_no.get(),
                                                                             self.email.get(),
                                                                             self.r_address.get('1.0',
                                                                                                END)))
            
            con.commit()
            self.fetch_relative()
            con.close()
            messagebox.showinfo("success", "Recored has been inserted")

    def fetch_relative(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM RELATIVES")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Patient_table.delete(*self.Patient_table.get_children())
            for row in rows:
                self.Patient_table.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor_relative(self, ev):
        curosor_row = self.Patient_table.focus()
        contents = self.Patient_table.item(curosor_row)
        row = contents['values']
        self.patientid.set(row[0])
        self.name.set(row[1])
        self.type.set(row[2])
        self.phone_no.set(row[3])
        self.email.set(row[4])
        self.r_address.insert(END, row[5])

    def clear_relative(self):
        self.patientid.set("")
        self.name.set("")
        self.type.set("")
        self.phone_no.set("")
        self.email.set("")
        self.r_address.delete("1.0", END)

    def search_data_relative(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("SELECT * FROM RELATIVES WHERE " + str(self.search.get()) + " LIKE"
                                                                                " '%" + str(self.search_t.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Patient_table.delete(*self.Patient_table.get_children())
            for row in rows:
                self.Patient_table.insert('', END, values=row)
            con.commit()
        con.close()

    def delete_data_relative(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("DELETE FROM RELATIVES WHERE patient_id=%s", self.patientid.get())
        con.commit()
        con.close()
        self.fetch_relative()
        self.clear_relative()

    def update_data_relative(self):
        con = pymysql.connect(host="localhost", user="root", database="c_patient")
        cur = con.cursor()
        cur.execute("UPDATE RELATIVES SET name=%s, type=%s, relatives_no=%s, email=%s, address=%s WHERE patient_id=%s", (
            self.name.get(),
            self.type.get(),
            self.phone_no.get(),
            self.email.get(),
            self.r_address.get('1.0',
                               END)))

        con.commit()
        self.fetch_relative()
        self.clear_relative()
        con.close()
        messagebox.showinfo("success", "Recored has been updated")







root = Tk()
obj = Patient(root)
root.mainloop()