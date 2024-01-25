from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector
from register import Register


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Sejal\Desktop\hotelphotos\page 8.jpg")
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="cyan")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page9.jpg")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimag1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimag1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="cyan")
        get_str.place(x=95, y=100)

        # LABEL
        username = lb1 = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="cyan")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = lb1 = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="cyan")
        password.place(x=70, y=225)
        self.txtpassword = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)

        # ========================  Image Icon =====================

        img2 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page9.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimag2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimag2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page10.jpg")
        img3 = img3.resize((25, 25,), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimag3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimag3.place(x=650, y=397, width=25, height=25)

        # login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="black", bg="white", activebackground="white", activeforeground="black")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # registration button
        registerbtn = Button(frame, text="New User Register", command=self.register_window,font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="black", bg="cyan",activebackground="cyan", activeforeground="black")
        registerbtn.place(x=15, y=350, width=160)

        # forget button
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,
                           font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="black", bg="cyan",
                           activebackground="cyan", activeforeground="black")
        forgetbtn.place(x=10, y=370, width=160, )

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "all field required")
        elif self.txtuser.get() == "Seema" and self.txtpassword.get() == "sejal":
            messagebox.showinfo("Success", "Welcome")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",
                                           database="hotel_management", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where fname=%s and password=%s", (
                self.txtuser.get(),
                self.txtpassword.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Register(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ========================= reset password =================================
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",
                                           database="hotel_management", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txtsecurity.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter correct Answer", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txtnewpassword.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset,please login new password")
                self.root2.destroy()

    # ========================== forget password =======================================

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email address to reset the password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",
                                           database="hotel_management", auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error", "Please enter the valid user name", parent=self.root2)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red",
                          bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"))
                self.combo_security_Q["values"] = (
                    "Select", "Your Favourite dish", "Your favourite sweet", "Your favourite drink")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                 fg="black")
                security.place(x=50, y=150)
                self.txtsecurity = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txtsecurity.place(x=50, y=180, width=250)

                newpassword = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                                    fg="black")
                newpassword.place(x=50, y=220)
                self.txtnewpassword = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txtnewpassword.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"),
                             fg="white", bg="green")
                btn.place(x=120, y=290)


if __name__ == "__main__":
    main()
