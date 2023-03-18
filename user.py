from tkinter import*
from PIL import Image ,  ImageTk

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")

        #### BG Image #######
        self.bg = ImageTk.PhotoImage(file="login.jpg")
        self.bg_Image=Label(self.root,image=self.bg).place(x=0,y=o,relheight=1)