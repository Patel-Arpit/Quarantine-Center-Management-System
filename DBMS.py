from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class patient:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1530x800+0+0")

        #=====BD Image======
        self.bg1 = ImageTk.PhotoImage(file="F:/xj/hq5.jpg")
        bg1 = Label(self.root, image=self.bg1).place(x=0, y=0, relwidth=1, relheight=1)



        #=====Login Frame=====

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=350, y=300, height=340, width=500)

        title = Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=20)
        desc = Label(Frame_login, text="Accountant Patient login Area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white").place(x=90,
                                                                                                                   y=90)

        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"),
                     fg="gray", bg="white").place(x=90,y=130)
        self.txt_user = Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=160,width=320,height=35)

        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"),
                         fg="gray", bg="white").place(x=90, y=200)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15),show="*", bg="lightgray")
        self.txt_pass.place(x=90, y=230, width=320, height=35)

        
        login_btn = Button(self.root, text="Login", fg="white", bg="red", activebackground="red", bd=2,command=self.login_function,cursor="hand2",
                        font=("times new roman", 17)).place(x=510, y=620,width=180,height=40)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.txt_pass.get()!="123" or self.txt_user.get()!="123":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
        else:
            messagebox.showinfo("", "WELCOME",parent=self.root)
            #messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}", parent=self.root)
            self.root.destroy()
            import art

root = Tk()
obj = patient(root)
root.mainloop()