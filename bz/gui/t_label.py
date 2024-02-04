#encoding=gbk
'''
测试gui label
'''
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.label01=Label(self,text="first label",width=10,height=2,bg="black",fg="white")
        self.label01["text"]="ccc"
        self.label01.config(fg="red",bg="green")
        self.label01.pack()
        self.label02=Label(self,text="lst",width=10,height=2,bg="blue",fg="white",font=("黑体",30))
        self.label02.pack()
        global photo
        photo=PhotoImage(file="./01.png")
        self.label03=Label(self,image=photo)
        self.label03.pack()
        self.label04=Label(self,text="label040000000000000",borderwidth=5,relief="groove",justify="right")
        self.label04.pack()
if __name__=="__main__":
    root=Tk()
    root.geometry("400x460+200+300")
    app=Application(master=root)
    root.mainloop()