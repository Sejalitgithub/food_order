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
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_ProductNo=StringVar()
        self.var_Category= StringVar()
        self.var_PName = StringVar()
        self.var_Quantity=StringVar()
        self.var_Price=StringVar()
        self.var_PaymentMode=StringVar()
        self.var_address = StringVar()



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

        register_lb1=Label(frame,text="ORDER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lb1.place(x=20,y=20)


      # ======================== label and entry =======================

        # ======================= row1 =============================
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=80)
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=50,y=110,width=250)

        name = Label(frame, text="Name", font=("times new roman", 15, "bold"), bg="white",fg="black")
        name.place(x=370, y=80)
        self.txtname = ttk.Entry(frame,textvariable=self.var_name, font=("times new roman", 15, "bold"))
        self.txtname.place(x=370, y=110, width=250)


      # ====================== Row2 ==============================
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=50, y=140)
        self.txtemail = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txtemail.place(x=50, y=170, width=250)

        ProductNo = Label(frame, text="Product Number", font=("times new roman", 15, "bold"), bg="white", fg="black")
        ProductNo.place(x=370, y=140)
        self.txtProductNo = ttk.Entry(frame,textvariable=self.var_ProductNo, font=("times new roman", 15, "bold"))
        self.txtProductNo.place(x=370, y=170, width=250)

        # ============================ row3 =============================
        category = Label(frame, text="Category", font=("times new roman", 15, "bold"), bg="white", fg="black")
        category.place(x=50, y=200)
        self.txtcategory = ttk.Entry(frame, textvariable=self.var_Category, font=("times new roman", 15))
        self.txtcategory.place(x=50, y=230, width=250)

        PName = Label(frame, text="Product Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        PName.place(x=370, y=200)
        self.txtPName = ttk.Entry(frame, textvariable=self.var_PName, font=("times new roman", 15, "bold"))
        self.txtPName.place(x=370, y=230, width=250)

        # ========================== row4 =============================
        Quantity=Label(frame,text="Quatity", font=("times new roman", 15, "bold"), bg="white", fg="black")
        Quantity.place(x=50,y=260)

        self.txtQuantity = ttk.Entry(frame, textvariable=self.var_Quantity, font=("times new roman", 15, "bold"))
        self.txtQuantity.place(x=50,y=290,width=250)



        price = Label(frame, text="Price", font=("times new roman", 15, "bold"), bg="white", fg="black")
        price.place(x=370, y=260)
        self.txtprice = ttk.Entry(frame,textvariable=self.var_Price, font=("times new roman", 15, "bold"))
        self.txtprice.place(x=370, y=290, width=250)

      # ============================ row5 =============================
        address = Label(frame, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="black")
        address.place(x=50, y=320)
        self.txtaddress = ttk.Entry(frame,textvariable=self.var_address, font=("times new roman", 15))
        self.txtaddress.place(x=50, y=350, width=250)

        PaymentMode = Label(frame, text="Payment Mode", font=("times new roman", 15, "bold"), bg="white", fg="black")
        PaymentMode.place(x=370, y=320)

        self.combo_PaymentMode = ttk.Combobox(frame, textvariable=self.var_PaymentMode, font=("times new roman", 15, "bold"))
        self.combo_PaymentMode["values"] = ("Select","Online","Offline")
        self.combo_PaymentMode.place(x=370, y=350, width=250)
        self.combo_PaymentMode.current(0)

        # ========================= check button ============================
        # self.var_check=IntVar()
        # checkbtn=Checkbutton(frame,variable=self.var_check,text="Order Confirm", font=("times new roman", 15, "bold"),onvalue=1,offvalue=0)
        # checkbtn.place(x=50,y=390)

      #  ======================= button ============================

        viewbtn = Button(frame, text="Confirm", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")

        viewbtn.place(x=50,y=450,width=200)

        newbtn = Button(frame, text="BACK", width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        newbtn.place(x=330, y=450, width=200)


      #
      # ============================= Function Declaration ===============================

    def order_data(self):
            if self.var_PName.get()=="" or self.var_email.get()=="" or self.var_address.get()=="Select":
                messagebox.showerror("Error","All fields are required")
            elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same")
            elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and condition")
            else:
                conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",database="food_order", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                query=("select * from ordercustomer where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist try another email")
                else:
                    my_cursor.execute("insert into ordercustomer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                           self.var_contact.get(),
                                                                                           self.var_name.get(),
                                                                                           self.var_email.get(),
                                                                                           self.var_ProductNo.get(),
                                                                                           self.var_Category.get(),
                                                                                           self.var_PName.get(),
                                                                                           self.var_Quantity.get(),
                                                                                           self.var_Price.get(),
                                                                                           self.var_address.get(),
                                                                                           self.var_PaymentMode.get(),
                                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")







if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()