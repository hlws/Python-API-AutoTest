from tkinter import *
root=Tk()
btn01=Button(root)
btn01["text"]="点我送花"
def songhua(e):
    messagebox.showinfo("Message","送你一朵玫瑰花，请你爱上我")