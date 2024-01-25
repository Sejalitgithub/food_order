from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox




class Ifood:
    def __init__(self,root):
        self.root=root
        self.root.title("food ordering management")
        self.root.geometry("1295x550+230+220")

        ############## variable #############3333

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_ref=StringVar()
        self.var_category=StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_details = StringVar()



        ########### TITLE ################

        lb1_title = Label(self.root, text="ICECREAME", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)

        ########## LOGO ###########
        img2 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page1.jpeg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        limage = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        limage.place(x=5, y=2, width=100, height=40)

        #### LABELE FRAME #####
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text=" Icecreame",font=("arial", 12, "bold"),padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        ################# LABEL AND ENTRYS #########################

    # Product ref

        lb1_pro_ref= Label(labelframeleft, text="Product No", font=("arial", 12, "bold"), padx=2,pady=6)
        lb1_pro_ref.grid(row=0,column=0,sticky=W)


        enty_ref = ttk.Entry(labelframeleft,textvariable= self.var_ref, width=29,font=("arial", 13, "bold"))
        enty_ref.grid(row=0,column=1)

        # Gender combo box

        lb1_category = Label(labelframeleft, text="Category :", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_category.grid(row=1, column=0, sticky=W)
        combo_category = ttk.Combobox(labelframeleft, textvariable=self.var_category, font=("arial", 12, "bold"), width=27,state="readonly")
        combo_category["value"] = ("Icecreame")
        combo_category.current(0)
        combo_category.grid(row=1, column=1)

        # product name

        pname= Label(labelframeleft, text="Product Name :", font=("arial", 12, "bold"), padx=2,pady=6)
        pname.grid(row=2,column=0,sticky=W)
        txtpname = ttk.Entry(labelframeleft,textvariable= self.var_pname, width=29,font=("arial", 13, "bold"))
        txtpname.grid(row=2,column=1)
 #  Price

        lb1price= Label(labelframeleft, text="Price:", font=("arial", 12, "bold"), padx=2,pady=6)
        lb1price.grid(row=3,column=0,sticky=W)
        txtprice = ttk.Entry(labelframeleft,textvariable= self.var_price, width=29,font=("arial", 13, "bold"))
        txtprice.grid(row=3,column=1)

 # Quantity

        lb1quantity = Label(labelframeleft, text="Quantity:", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1quantity.grid(row=4, column=0, sticky=W)
        txtquantity = ttk.Entry(labelframeleft, textvariable=self.var_quantity, width=29, font=("arial", 13, "bold"))
        txtquantity.grid(row=4, column=1)

        # Details

        lb1details= Label(labelframeleft, text="Details:", font=("arial", 12, "bold"), padx=2,pady=6)
        lb1details.grid(row=5,column=0,sticky=W)
        txtdetails = ttk.Entry(labelframeleft,textvariable= self.var_details, width=29,font=("arial", 13, "bold"))
        txtdetails.grid(row=5,column=1)


        ################# BUTTONS ################

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=60, y=300, width=205, height=35)


        btnreset = Button(btn_frame,command=self.reset,text="Reset", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnreset.grid(row=0, column=3, padx=1)

        btnOrderNow = Button(btn_frame, text="Order Now", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnOrderNow.grid(row=0, column=4, padx=1, sticky=W)

        ########### TABLE FRAME  SEARCH #################################
        Tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Food Product", font=("arial", 12, "bold"), padx=2)
        Tableframe.place(x=435, y=50, width=860, height=490)

        lbsearch= Label(Tableframe , text="Search by:", font=("arial", 12, "bold"), bg="red",fg="white")
        lbsearch.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(Tableframe,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("ProductNo", "PName")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch = ttk.Entry(Tableframe,textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2,padx=2)

        btnsearch = Button(Tableframe,command=self.search, text="Search", font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(Tableframe, text="Show all", command=self.fetch_data,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=4, padx=1)

       ################### SHOW DATA TABLE #######################



        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.food_Details_table=ttk.Treeview(details_table,columns=("ref","category","pname","price","quantity","details"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.food_Details_table.xview)
        scroll_y.config(command=self.food_Details_table.yview)

        self.food_Details_table.heading("ref",text="Product No")
        self.food_Details_table.heading("category",text="Category")
        self.food_Details_table.heading("pname", text="Product Name")
        self.food_Details_table.heading("price", text="Price")
        self.food_Details_table.heading("quantity", text="Quantity")
        self.food_Details_table.heading("details", text="Details")


        self.food_Details_table["show"]="headings"
        self.food_Details_table.column("ref",width=100)
        self.food_Details_table.column("category",width=100)
        self.food_Details_table.column("pname",width=100)
        self.food_Details_table.column("quantity", width=100)
        self.food_Details_table.column("price", width=100)
        self.food_Details_table.column("details",width=100)


        self.food_Details_table.pack(fill=BOTH,expand=1)
        self.food_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #
    # def add_data(self):
    #     if self.var_category.get()=="" or self.var_pname.get()=="" or self.var_price.get()=="" :
    #         messagebox.showerror("Error","All fields are required",parent=self.root)
    #     else:
    #          try:
    #              conn=mysql.connector.connect(host="localhost",user="root",password="sejal@0712",database="food_order", auth_plugin="mysql_native_password")
    #              my_cursor=conn.cursor()
    #              my_cursor.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_category.get(),self.var_pname.get(),self.var_price.get(),self.var_quantity.get(),self.var_details.get()))
    #
    #              conn.commit()
    #              self.fetch_data()
    #              conn.close()
    #              messagebox.showinfo("Success","Product has been added",parent=self.root)
    #          except Exception as es:
    #              messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


  # fetch button is not workinb
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sejal@0712",database="food_order",auth_plugin="mysql_native_password")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from icecreame")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.food_Details_table.delete(*self.food_Details_table.get_children())
            for i in rows:
                self.food_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.food_Details_table.focus()
        content=self.food_Details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_category.set(row[1]),
        self.var_pname.set(row[2]),
        self.var_price.set(row[3]),
        self.var_quantity.set(row[4]),
        self.var_details.set(row[5]),

# update button is not working


#==========================  Update BUtton ================================
    # def update(self):
    #     if self.var_ref.get()=="":
    #         messagebox.showerror("Error","Please enter Product number",parent=self.root)
    #     else:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",database="food_order", auth_plugin="mysql_native_password")
    #         my_cursor = conn.cursor()
    #         my_cursor.execute("update product set Category=%s,PName=%s,Price=%s,Quantity=%s,Details=%s where ProductNo=%s",(
    #                                                                                                                                          self.var_category.get(),
    #                                                                                                                                          self.var_pname.get(),
    #                                                                                                                                          self.var_price.get(),
    #                                                                                                                                          self.var_quantity.get(),
    #                                                                                                                                          self.var_details.get(),
    #                                                                                                                                          self.var_ref.get(),
    #
    #                                                                                                                                          ))
    #
    #         conn.commit()
    #         self.fetch_data()
    #         conn.close()
    #         messagebox.showinfo("Update", "product Details has been updated successfully !.", parent=self.root)
    #
    # def mDelete(self):
    #     mDelete=messagebox.askyesno("food ordering management","Do you want to delete this product details",parent=self.root)
    #     if mDelete>0:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712",database="food_order", auth_plugin="mysql_native_password")
    #         my_cursor = conn.cursor()
    #         query="delete from product where ProductNo=%s"
    #         value=(self.var_ref.get(),)
    #         my_cursor.execute(query,value)
    #     else:
    #         if not mDelete:
    #             return
    #     conn.commit()
    #     self.fetch_data()
    #     conn.close()


    def reset(self):

        self.var_category.set(""),
        self.var_pname.set(""),
        self.var_price.set(""),
        self.var_quantity.set(""),
        self.var_details.set("")
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="sejal@0712", database="food_order", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from icecreame where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.food_Details_table.delete(*self.food_Details_table.get_children())
            for i in rows:
                self.food_Details_table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ =="__main__":
     root=Tk()
     obj=Ifood(root)
     root.mainloop()
