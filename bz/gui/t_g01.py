#encoding=gbk
from tkinter import *
from  tkinter import messagebox
root=Tk()
root.geometry("500x400+100+200")
btn01=Button(root)
btn01.pack()
btn01["text"]="�����ͻ�"
def songhua(e):
    messagebox.showinfo("message","give you a flower")
    print("this is flower")
btn01.bind("<Button-1>",songhua)
root.mainloop()