from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.btn01=Button(root,text="login",width=6,height=3,anchor=NE,command=self.login)
        self.btn01.pack()
        global photo
        photo=PhotoImage(file="./01.png")
        self.btn02=Button(root,image=photo,command=self.login)
        self.btn02.pack()
        self.btn02.config(state="disabled")
    def login(self):
        messagebox.showinfo("clic system","login success")
if __name__=="__main__":
    root=Tk()
    root.geometry("400x130+200+300")
    app=Application(master=root)
    root.mainloop()