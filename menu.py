from tkinter import *
from PIL import Image,ImageTk
from GujratiFood import Gfood
from Breakfast import Bfood
from Icecreame import Ifood




class order:
    def __init__(self,root):
        self.root=root
        self.root.title("Food Ordering System")
        self.root.geometry("1500x800+0+0")


        img11=Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page9.jpg")
        img11 = img11.resize((1550, 1400), Image.ANTIALIAS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        limage = Label(self.root, image=self.photoimg11, bd=4, relief=RIDGE)
        limage.place(x=0, y=0,width=1550, height=140)

        ########## LOGO ###########
        img12 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page12.jpeg")
        img12 = img12.resize((230, 140), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        limage12 = Label(self.root, image=self.photoimg12, bd=4, relief=RIDGE)
        limage12.place(x=0, y=0, width=230, height=140)

       ########### TITLE ################



        lb1_title = Label(self.root, text="FOOD ORDERING SYSTEM", font=("times new roman",40,"bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=140, width=1550, height=50)

        #############  FRAME ##############

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)


        lb1_menu = Label(main_frame, text="MENU", font=("times new roman",20,"bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb1_menu.place(x=0, y=0, width=230)


      ############ BTN ##################

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        ####### BUTTON ############
        Orderbtn = Button(btn_frame, text="ORDER NOW",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
        Orderbtn.grid(row=0, column=0,pady=1)

        registerbtn = Button(btn_frame, text="REGITERATION",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
        registerbtn.grid(row=1, column=0,pady=1)

        memberbtn = Button(btn_frame, text="MEMBER LOGIN",width=22,font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
        memberbtn.grid(row=2 ,column=0,pady=1)

        Adminbtn = Button(btn_frame, text="ADMIN LOGIN",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
        Adminbtn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
        logout_btn.grid(row=4, column=0,pady=1)

       ########### RIGHT HAND SIDE IMAGE ###############

        img1 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\gujrati.jpg")
        img1 = img1.resize((230, 210), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        limage1 = Label(main_frame, image=self.photoimg1, bd=4, relief=RIDGE)
        limage1.place(x=225, y=0, width=230, height=210)
        lb1_gujrati = Button(main_frame, text="Gujrati Food",command=self.GBtn, font=("times new roman",20,"bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb1_gujrati.place(x=225, y=210, width=230)

        # chineese food
        img2 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\chineese.jpg")
        img2 = img2.resize((230, 210), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        limage2 = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        limage2.place(x=550, y=0, width=230, height=210)

        lb2_chineese = Button(main_frame, text="Chineese Food", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb2_chineese.place(x=550, y=210, width=230)



        # tamil food

        img3 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\tamil.jpg")
        img3 = img3.resize((230, 210), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        limage3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        limage3.place(x=875, y=0, width=230, height=210)

        lb3_tamil = Button(main_frame, text="Sounth Food", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb3_tamil.place(x=875, y=210, width=230)



        # maharastrian food

        img6 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\mumbai.jpeg")
        img6 = img6.resize((250, 250), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        limage6 = Label(main_frame, image=self.photoimg6, bd=4, relief=RIDGE)
        limage6.place(x=1200, y=0, width=250, height=250)

        lb6_maharastrian = Button(main_frame, text="Maharastrian Food", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb6_maharastrian.place(x=1200, y=210, width=250)


        #=================================== BELOW ====================================================

        # italian food

        img7 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\italian.jpg.")
        img7 = img7.resize((230, 210), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        limage7 = Label(main_frame, image=self.photoimg7, bd=4, relief=RIDGE)
        limage7.place(x=225, y=330, width=230, height=210)

        lb7_italian = Button(main_frame, text="Italian Food", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb7_italian.place(x=225, y=540, width=230)

        # Breakfast

        img8 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\breakfast.jpg")
        img8 = img8.resize((230, 210), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        limage8 = Label(main_frame, image=self.photoimg8, bd=4, relief=RIDGE)
        limage8.place(x=550, y=330, width=230, height=210)

        lb8_breakfast = Button(main_frame, text="Breakfast",command=self.BFBtn, font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb8_breakfast.place(x=550, y=540, width=230)

        # Juice and soft drinks


        img9 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\fresh-juice.jpg")
        img9 = img9.resize((230, 210), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        limage9 = Label(main_frame, image=self.photoimg9, bd=4, relief=RIDGE)
        limage9.place(x=875, y=330, width=230, height=210)

        lb9_tamil = Button(main_frame, text="Fresh Juice ", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb9_tamil.place(x=875, y=540, width=230)

        # Icecreame

        img10 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\icecream.jpg")
        img10 = img10.resize((230, 210), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        limage10 = Label(main_frame, image=self.photoimg10, bd=4, relief=RIDGE)
        limage10.place(x=1200, y=330, width=230, height=210)

        lb10_icecreame = Button(main_frame, text="Icecreame",command=self.IBtn, font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lb10_icecreame.place(x=1200, y=540, width=230)



        ########### LEFT HAND SIDE IMAGE ###############

        img4 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page9.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        limage4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        limage4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page11.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        limage5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        limage5.place(x=0, y=420, width=230, height=190)

    def GBtn(self):
            self.new_window = Toplevel(self.root)
            self.app = Gfood(self.new_window)

    def BFBtn(self):
        self.new_window = Toplevel(self.root)
        self.app = Bfood(self.new_window)

    def IBtn(self):
         self.new_window = Toplevel(self.root)
         self.app = Ifood(self.new_window)


if __name__ =="__main__":
    root=Tk()
    obj=order(root)
    root.mainloop()

