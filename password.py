#!/usr/bin/python

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class gui(Tk):
	def __init__(self, master):
		self.master = master
		master.title("PassSafe")
		master.bind("<Button-1>", self.BackOnClick)

		self.background = Canvas()
		self.background.configure(highlightthickness=0,background='gray24',width=800,height=500)
		self.background.pack(fill=BOTH, expand=YES)

		self.widgets = []

		self.file = open("users.txt", 'r+')
		self.UserList = self.file.read().split(' ')

		self.initialize()

	def initialize(self):

		self.file.seek(0)
		self.UserList = self.file.read().split(' ')
		self.background.delete("all")
		
		counter = 0
		while counter < len(self.UserList):
			user = Label(text = self.UserList[counter])
			self.widgets.append(user)
			user.configure(bg='gray24')
			user.bind("<Button-1>", self.UserOnClick)

			x_pos = (counter+1)/10 - (len(self.UserList)+2)/20 + .5

			user.place(width = 50, height = 10,relx=x_pos, rely=0.5, anchor=CENTER)
			counter += 1

		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)
		new_user.bind("<Button-1>", self.NewUserOnClick)
		new_user.configure(bg='gray24')
		new_user.place(width = 80, height = 10,relx=.5, rely=0.55, anchor=CENTER)

	def UserOnClick(self, event):
		caller = event.widget
		self.login(caller["text"])

	def NewUserOnClick(self, event):
		self.clear()
		self.background.create_polygon((0,0,0,50,50,0), fill='black')

		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)
		new_user.bind("<Button-1>", self.NewUserOnClick)
		new_user.configure(bg='gray24')
		new_user.place(width = 80, height = 10,relx=.5, rely=0.45, anchor=CENTER)

		self.new_username = Entry()
		self.widgets.append(self.new_username)
		self.new_username.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_username.bind('<Return>', self.NewUser)

	def NewUser(self, event):
		user = Label(text = self.new_username.get())
		user.configure(background = 'gray24')
		self.widgets.append(user)
		user.place(width = 80, height = 10,relx=.5, rely=0.45, anchor=CENTER)

		self.new_password = Entry()
		self.widgets.append(self.new_password)
		self.new_password.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_password.bind('<Return>', self.NewPassword)

	def NewPassword(self, event):
		#ENCRYPT AND STORE PASSWORD
		print(self.new_password.get())
		self.file.write(" " + self.new_username.get())
		self.clear()
		self.initialize()



	def BackOnClick(self, event):

		#gets cursor coords in window, there is probably a better way to do this
		x=self.master.winfo_pointerx()-self.master.winfo_rootx()
		y=self.master.winfo_pointery()-self.master.winfo_rooty()

		if x < 50-y and y < 50-x:
			self.clear()
			self.initialize()

	def login(self,username):
		self.clear()

		self.username = username	#this is ugly I know, will (hopefully) clean up later

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
		self.clear()
		self.passwords()

	def passwords(self):
		user = Label(text = self.username)
		self.widgets.append(user)
		user.configure(background = 'gray24')
		user.place(width = 100, height = 20,relx=.5, rely=0.05, anchor=CENTER)

		groups = ['Social Media', 'Entertainment', 'Education', 'Gaming', 'Other']

		counter = 0
		while counter < len(groups):
			passwords = ScrolledText()
			self.widgets.append(passwords)
			#to disable/enable editing use state='normal' and state='disabled' respectively
			passwords.configure(background = 'gray24', highlightthickness=0,borderwidth=0)
			
			#removes scrollbar
			passwords.vbar.forget()

			passwords.tag_config('justified', justify=CENTER)
			passwords.insert(INSERT, groups[counter], 'justified')
			x_offset = (counter+1)/(len(groups)+1)
			passwords.place(width = 120, height = 400,relx=x_offset, rely=0.5, anchor=CENTER)


			counter += 1


if __name__ == "__main__":
	root = Tk()
	GUI = gui(root)
	root.mainloop()
	