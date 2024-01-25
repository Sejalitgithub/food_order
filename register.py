from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

     # ============================= variable ========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_add = StringVar()
        self.var_city = StringVar()
        self.var_securityQ=StringVar()
        self.var_security=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


      # ========================== bg image ===============================
        img3 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page4.jpg")
        img3 = img3.resize((1600, 900), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        limage1 = Label(self.root, image=self.photoimg3 ,relief=RIDGE)
        limage1.place(x=0, y=0, relwidth=1, relheight=1)

      # ======================= left image =======================

        img1 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page15.jpg")
        img1 = img1.resize((470, 550), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        limage = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        limage.place(x=50, y=100, width=470, height=550)

      # ========================== main frame ===========================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lb1=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lb1.place(x=20,y=20)


      # ======================== label and entry =======================

        # ======================= row1 =============================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=80)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=110,width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white",fg="black")
        l_name.place(x=370, y=80)
        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=110, width=250)


      # ====================== Row2 ==============================
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=140)
        self.txtcontact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txtcontact.place(x=50, y=170, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=140)
        self.txtemail = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtemail.place(x=370, y=170, width=250)

        # ============================ row3 =============================
        add = Label(frame, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="black")
        add.place(x=50, y=200)
        self.txtadd = ttk.Entry(frame, textvariable=self.var_add, font=("times new roman", 15))
        self.txtadd.place(x=50, y=230, width=250)

        city = Label(frame, text="City", font=("times new roman", 15, "bold"), bg="white",
                             fg="black")
        city.place(x=370, y=200)
        self.txtcity = ttk.Entry(frame, textvariable=self.var_city, font=("times new roman", 15, "bold"))
        self.txtcity.place(x=370, y=230, width=250)

        # ========================== row4 =============================
        security_Q=Label(frame,text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50,y=260)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Favourite dish","Your favourite sweet","Your favourite drink")
        self.combo_security_Q.place(x=50,y=290,width=250)
        self.combo_security_Q.current(0)


        security = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security.place(x=370, y=260)
        self.txtsecurity = ttk.Entry(frame,textvariable=self.var_security, font=("times new roman", 15, "bold"))
        self.txtsecurity.place(x=370, y=290, width=250)

      # ============================ row5 =============================
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=320)
        self.txtpswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txtpswd.place(x=50, y=350, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=320)
        self.txtconfirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass,font=("times new roman", 15, "bold"))
        self.txtconfirm_pswd.place(x=370, y=350, width=250)

      # ========================= check button ============================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions", font=("times new roman", 15, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=390)

      #  ======================= button ============================

        img=Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page12.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimgage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimgage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman", 15, "bold"))
        b1.place(x=0,y=440,width=300)

        img1 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page13.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimgage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimgage1, borderwidth=0, cursor="hand2",font=("times new roman", 15, "bold"))
        b2.place(x=330, y=440, width=300)
      #
      # ============================= Function Declaration ===============================

    def register_data(self):
            if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and condition")
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",database="food_order", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                query=("select * from customer where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist try another email")
                else:
                    my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_fname.get(),
                                                                                           self.var_lname.get(),
                                                                                           self.var_contact.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_add.get(),
                                                                                           self.var_city.get(),
                                                                                           self.var_securityQ.get(),
                                                                                           self.var_security.get(),
                                                                                           self.var_pass.get(),
                                                                                           self.var_confpass.get(),
                                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")







if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()