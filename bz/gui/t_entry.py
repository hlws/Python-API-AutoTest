#encoding=gbk
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.laber01=Label(self,text="�û���")
        self.laber01.pack()
        v1=StringVar()
        self.entry01=Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())
        #���������
        self.laber02=Label(self,text="����")
        self.laber02.pack()
        v2=StringVar()
        self.entry02=Entry(self,textvariable=v2,show="*")
        self.entry02.pack()
        Button(self,text="��¼",command=self.login).pack()
    def login(self):
        username=self.entry01.get()
        pwd=self.entry02.get()
        print("�Ա��û�������")
        print("�û���"+username)
        print("����"+pwd)
        if username=="lst" and pwd=="123456":
            messagebox.showinfo("clic","welcome")
        else:
            messagebox.showinfo("clic","login error")
if __name__=="__main__":
    root=Tk()
    root.geometry("400x130+200+300")
    app=Application(root)
    root.mainloop()