from tkinter import *
import webbrowser
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.w1=Text(root,)
