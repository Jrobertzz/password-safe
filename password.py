#!/usr/bin/python

from tkinter import *

class gui(Tk):
    def __init__(self, master):
        self.master = master
        master.title("PassSafe")
        master.configure(width=800, height=500,background = 'gray24')
        self.widgets = []
        self.UserList = ["USER1", "USER2", "USER3"]
        self.initialize()

    def initialize(self):
        background = Frame()
        counter = 0
        while counter < len(self.UserList):
        	user = Label(text = self.UserList[counter])
        	self.widgets.append(user)
        	user.configure(bg='gray24')
        	user.bind("<Button-1>", self.OnClick)

        	x_pos = (counter+1)/10 - (len(self.UserList)+1)/20 + .5

        	user.place(width = 50, height = 10,relx=x_pos, rely=0.5, anchor=CENTER)
        	counter += 1


    def OnClick(self, event):
    	caller = event.widget
    	self.login(caller["text"])

    def login(self,username):
    	self.clear()
    	i = 0
    	user = Label(text = username)
    	self.widgets.append(user)
    	user.configure(bg='gray24')
    	user.place(width = 50, height = 10,relx=.5, rely=0.48, anchor=CENTER)

    	self.password = Entry();
    	self.widgets.append(self.password)
    	self.password.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
    	self.password.bind('<Return>', self.OnEnter)

    def clear(self):
    	for widget in self.widgets:
    		widget.destroy()
    	self.widgets = []

    def OnEnter(self, event):
    	__password = self.password.get()
    	self.password.delete(0, END)
    	print(__password)



if __name__ == "__main__":
	root = Tk()
	GUI = gui(root)
	root.mainloop()