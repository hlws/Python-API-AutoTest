#encoding=gbk
'''
经典的gui程序写法，使用面向对象的方式
'''
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    '''
    一个经典的gui程序写法
    '''
    def __int__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.btn01=Button(self)
        self.btn01["text"]="send flower"
        self.btn01.pack()
        self.btn01["command"]=self.songhua
        self.btnQuit=Button(self,text="退出",command=root.destroy)
        self.btnQuit.pack()
    def songhua(self):
        messagebox.showinfo("send flower","999")
if __name__=='__main__':
    root=Tk()
    root.geometry("500x500+200+200")
    root.title("one classic gui windows")
    app=Application(master=root)
    root.mainloop()