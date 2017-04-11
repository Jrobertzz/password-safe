#!/usr/bin/python

from tkinter import *

class gui(Tk):
    def __init__(self, master):
        self.master = master
        master.title("PassSafe")
        master.configure(width=800, height=500,background = 'gray24')
        self.labels = []
        self.UserList = ["USER1", "USER2", "USER3"]
        self.initialize()

    def initialize(self):
        background = Frame()
        counter = 0
        while counter < len(self.UserList):
        	user = Label(text = self.UserList[counter])
        	self.labels.append(user)
        	user.configure(bg='gray24')
        	user.bind("<Button-1>", self.OnClick)

        	x_pos = (counter+1)/10 - (len(self.UserList)+1)/20 + .5

        	user.place(width = 50, height = 10,relx=x_pos, rely=0.5, anchor=CENTER)
        	counter += 1


    def OnClick(self, event):
    	caller = event.widget
    	self.login(caller["text"])

    def login(self,username):
    	print(username)
    	i = 0
    	for label in self.labels:
    		label.destroy()
    	user = Label(text = username)
    	user.configure(bg='gray24')
    	user.place(width = 50, height = 10,relx=.5, rely=0.4, anchor=CENTER)




if __name__ == "__main__":
	root = Tk()
	GUI = gui(root)
	root.mainloop()