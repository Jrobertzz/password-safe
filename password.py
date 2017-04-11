#!/usr/bin/python

from tkinter import *

class gui(Tk):
	def __init__(self, master):
		self.master = master
		master.title("PassSafe")
		master.bind("<Button-1>", self.BackOnClick)

		self.background = Canvas()
		self.background.configure(highlightthickness=0,background='gray24',width=800,height=500)
		self.background.pack(fill=BOTH, expand=YES)

		self.widgets = []
		self.UserList = ["USER1", "USER2", "USER3"]
		self.initialize()

	def initialize(self):

		self.background.delete("all")
		
		counter = 0
		while counter < len(self.UserList):
			user = Label(text = self.UserList[counter])
			self.widgets.append(user)
			user.configure(bg='gray24')
			user.bind("<Button-1>", self.UserOnClick)

			x_pos = (counter+1)/10 - (len(self.UserList)+1)/20 + .5

			user.place(width = 50, height = 10,relx=x_pos, rely=0.5, anchor=CENTER)
			counter += 1

	def UserOnClick(self, event):
		caller = event.widget
		self.login(caller["text"])

	def BackOnClick(self, event):

		#gets cursor coords in window, there is probably a better way to do this
		x=self.master.winfo_pointerx()-self.master.winfo_rootx()
		y=self.master.winfo_pointery()-self.master.winfo_rooty()

		if x < 50-y and y < 50-x:
			self.clear()
			self.initialize()

	def login(self,username):
		self.clear()

		self.background.create_polygon((0,0,0,50,50,0), fill='black')

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

if __name__ == "__main__":
	root = Tk()
	GUI = gui(root)
	root.mainloop()
	