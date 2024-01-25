# from tkinter import *
# from PIL import Image,ImageTk
# from menu import order
# from register import Register
# # from details import DetailsRoom
#
#
#
#
# class food:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("Food Ordering System")
#         self.root.geometry("1500x800+0+0")
#
#
#         img1=Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page9.jpg")
#         img1 = img1.resize((1550, 1400), Image.ANTIALIAS)
#         self.photoimg1= ImageTk.PhotoImage(img1)
#
#         limage = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
#         limage.place(x=0, y=0,width=1550, height=140)
#
#         ########## LOGO ###########
#         img2 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page12.jpeg")
#         img2 = img2.resize((230, 140), Image.ANTIALIAS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)
#
#         limage = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
#         limage.place(x=0, y=0, width=230, height=140)
#
#        ########### TITLE ################
#
#
#
#         lb1_title = Label(self.root, text="FOOD ORDERING SYSTEM", font=("times new roman",40,"bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
#         lb1_title.place(x=0, y=140, width=1550, height=50)
#
#         #############  FRAME ##############
#
#         main_frame = Frame(self.root, bd=4, relief=RIDGE)
#         main_frame.place(x=0, y=190, width=1550, height=620)
#
#
#         lb1_menu = Label(main_frame, text="MENU", font=("times new roman",20,"bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
#         lb1_menu.place(x=0, y=0, width=230)
#
#
#       ############ BTN ##################
#
#         btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
#         btn_frame.place(x=0, y=35, width=228, height=190)
#
#         ####### BUTTON ############
#         Orderbtn = Button(btn_frame, text="ORDER NOW",command=self.orderBtn,width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
#         Orderbtn.grid(row=0, column=0,pady=1)
#
#         registerbtn = Button(btn_frame, text="REGITERATION",command=self.registerBtn, width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
#         registerbtn.grid(row=1, column=0,pady=1)
#
#         memberbtn = Button(btn_frame, text="MEMBER LOGIN",width=22,font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
#         memberbtn.grid(row=2 ,column=0,pady=1)
#
#         Adminbtn = Button(btn_frame, text="ADMIN LOGIN",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
#         Adminbtn.grid(row=3, column=0,pady=1)
#
#         logout_btn = Button(btn_frame, text="LOGOUT",width=22, font=("times new roman",14,"bold"), bg="black", fg="gold", bd=0,cursor="hand1")
#         logout_btn.grid(row=4, column=0,pady=1)
#
#        ########### RIGHT HAND SIDE IMAGE ###############
#
#         img3 = Image.open(r"C:\Users\Sejal\Desktop\hotelphotos\page4.jpg")
#         img3 = img3.resize((1310, 590), Image.ANTIALIAS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)
#
#         limage1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
#         limage1.place(x=225, y=0, width=1310, height=590)
#
#         img4 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page9.jpg")
#         img4 = img4.resize((230, 210), Image.ANTIALIAS)
#         self.photoimg4 = ImageTk.PhotoImage(img4)
#
#         limage2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
#         limage2.place(x=0, y=225, width=230, height=210)
#
#         img5 = Image.open(r"C:\Users\Sejal\Desktop\foodphotos\page11.jpg")
#         img5 = img5.resize((230, 190), Image.ANTIALIAS)
#         self.photoimg5 = ImageTk.PhotoImage(img5)
#
#         limage3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
#         limage3.place(x=0, y=420, width=230, height=190)
#
#
#     def orderBtn(self):
#       self.new_window = Toplevel(self.root)
#       self.app = order(self.new_window)
#
#     def registerBtn(self):
#       self.new_window = Toplevel(self.root)
#       self.app = Register(self.new_window)
#
#
# if __name__ =="__main__":
#     root=Tk()
#     obj=food(root)
#     root.mainloop()

