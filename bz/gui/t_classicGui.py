#encoding=gbk
'''
�����gui����д����ʹ���������ķ�ʽ
'''
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    '''
    һ�������gui����д��
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
        self.btnQuit=Button(self,text="�˳�",command=root.destroy)
        self.btnQuit.pack()
    def songhua(self):
        messagebox.showinfo("send flower","999")
if __name__=='__main__':
    root=Tk()
    root.geometry("500x500+200+200")
    root.title("one classic gui windows")
    app=Application(master=root)
    root.mainloop()