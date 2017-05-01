#!/usr/bin/env python3

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PassSys import PassSys

class gui(Tk):
	def __init__(self, master):

		self.ps = PassSys('u.txt')

		#color config
		self.gui_background = 'gray24'			#background color
		self.gui_foreground = 'white'			#foreground in the context
												#of this program refers to text color
												#foreground is naming convention

		#allows referencing parent object of whole gui from within class
		#Tk parent object is basically the window
		self.master = master
		master.title("PassSafe")

		#on mouseclick call 'BackOnClick,' passes event to 'BackOnClick'
		master.bind("<Button-1>", self.BackOnClick)

		#create drawable element(canvas) in window
		self.background = Canvas()
		self.background.configure(highlightthickness=0,background=self.gui_background,width=800,height=500)
		self.background.pack(fill=BOTH, expand=YES)	#fill window at initialization, resize with window resize


		self.errors = []

		self.back = Label(text = "back")
		self.back.configure(background = 'black', fg=self.gui_foreground)
		#define array to store all widgets(window elements)
		#I did not add background to widgets list as canvas will always be present
		self.widgets = []

		self.initialize()

	def initialize(self):
		#destroy all non-permanent objects(see def clear)
		self.clear()
		self.back.destroy()

		self.back = Label(text = "↶")
		self.back.configure(background = 'black', fg=self.gui_foreground)

		self.UserList = self.ps.getUsers()

		#reset background canvas to clear anything drawn to it
		#(in case of back clicked, clears back button)
		self.background.delete("all")
		
		#################################################################################
		#make a set of label objects for all UserList									#
		#Label is Tkinter onject that displays text 									#
		#and has some config settings such as text and background color 				#
																						#
		counter = 0																		#
		while counter < len(self.UserList):												#
			user = Label(text = self.UserList[counter])									#
			self.widgets.append(user)													#
			user.configure(bg=self.gui_background, fg=self.gui_foreground)				#
			user.bind("<Button-1>", self.UserOnClick)									#
																						#
			x_pos = (counter+1)/10 - (len(self.UserList)+1)/20 + .5						#
																						#
			user.place(width = 50, height = 50,relx=x_pos, rely=0.5, anchor=CENTER)		#
			counter += 1																#
		#################################################################################

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)
		new_user.bind("<Button-1>", self.NewUserOnClick)
		new_user.configure(bg=self.gui_background, fg=self.gui_foreground)
		new_user.place(width = 80, height = 15,relx=.5, rely=0.55, anchor=CENTER)

	def UserOnClick(self, event):
		#ugly way to get widget value, I used a better solution elsewhere
		#though its not working for clicking on user label
		#to login atm, this works
		caller = event.widget
		self.login(caller["text"])

	def NewUserOnClick(self, event):
		self.clear()

		self.errors = []

		#create_polygon draws to canvas, takes (x1, y1, x2, y2, x3, y3...)
		self.background.create_polygon((0,0,0,50,50,0), fill='black')
		self.back.place(width = 10, height = 10,x = 10, y = 10, anchor='nw')

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)	#add label widget to widget lists
		new_user.bind("<Button-1>", self.NewUserOnClick)	#bind mouseclick listener, call NewUserOnClick on click
		new_user.configure(bg=self.gui_background, fg=self.gui_foreground)
		new_user.place(width = 80, height = 15,relx=.5, rely=0.45, anchor=CENTER)

		self.username = Label(text = "enter username:")	#set text to new_username Entry text
		self.widgets.append(self.username)	#add label widget to widget lists
		self.username.configure(background = self.gui_background, fg=self.gui_foreground)
		self.username.place(width = 100, height = 15,relx=.35, rely=0.52, anchor=CENTER)

		#Entry is a text box that accepts input
		self.new_username = Entry()
		self.widgets.append(self.new_username)	#add label widget to widget lists
		self.new_username.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_username.bind('<Return>', self.NewUser) #bind to enter, call NewUser

	def NewUser(self, event):
		self.username.destroy()

		password = Label(text = "enter password:")	#set text to new_username Entry text
		self.widgets.append(password)	#add label widget to widget lists
		password.configure(background = self.gui_background, fg=self.gui_foreground)
		password.place(width = 100, height = 15,relx=.35, rely=0.52, anchor=CENTER)

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		user = Label(text = self.new_username.get())	#set text to new_username Entry text
		user.configure(background = self.gui_background, fg=self.gui_foreground)
		self.widgets.append(user)	#add label widget to widget lists
		user.place(width = 80, height = 15,relx=.5, rely=0.45, anchor=CENTER)

		#Entry is a textbox with event listeners
		self.new_password = Entry(show="*")
		self.widgets.append(self.new_password)	#add to widgets list
		self.new_password.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_password.bind('<Return>', self.NewPassword)

	def NewPassword(self, event):
		#ENCRYPT AND STORE PASSWORD
		self.ps.addUser(self.new_username.get(), self.new_password.cget("text"))
		self.clear()
		self.initialize()



	def BackOnClick(self, event):

		#gets cursor coords in window
		x=self.master.winfo_pointerx()-self.master.winfo_rootx()
		y=self.master.winfo_pointery()-self.master.winfo_rooty()

		#if a click event is triggered in top left window corner
		#go back to main screen
		if x < 50-y and y < 50-x:
			self.clear()
			self.initialize()

	def login(self,username):
		self.clear()

		#binds 'username' to global var
		#otherwise referencing username results in unwanted recursion
		#not entirely sure why though i believe it has to do with how the argument
		#was passed(indirectly) from an event
		self.username = username

		#create_polygon draws to canvas, takes (x1, y1, x2, y2, x3, y3...)
		self.background.create_polygon((0,0,0,50,50,0), fill='black')
		self.back.place(width = 10, height = 10,x = 10, y = 10, anchor='nw')

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		user = Label(text = username)
		self.widgets.append(user)		#add to widgets list
		user.configure(bg=self.gui_background, fg=self.gui_foreground)		#set background/foregroung
		user.place(width = 50, height = 15,relx=.5, rely=0.48, anchor=CENTER)

		#Entry is a textbox with event listeners
		self.password = Entry(show="*");
		self.widgets.append(self.password)		#add to widgets list
		self.password.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.password.bind('<Return>', self.OnEnter)

	def clear(self):
		#iterate though widgets, and remove each from memory
		for widget in self.widgets:
			widget.destroy()
		self.widgets = []	#clear widgets list to reflect all widget objects were destroyed
							#note that destroy() does not remove these from list as list
							#affectively contains a pointer to the object, which is not destroyed

	def OnEnter(self, event):
		#__ obfuscates variable name in memory,
		#used to tell programmers not to mess
		#with outside of function, though it is possible with enough work
		#python forgoes the false sense of security other
		#languages like java give with this, as one can alter
		#variables from a different method with enough work in java
		self.__password = self.password.get()
		self.password.delete(0, END)	#clear Entry object password's textbox(possibly not neccessary)

		self.show_passwords()
		#self.clear()					#remove all non-permanent widgets
		#self.passwords()

	def show_passwords(self):
		self.passwords = []
		self.names = self.ps.getNames(self.username, self.__password)
		for name in self.names:
			self.passwords.append(self.ps.getPassword(self.username, self.__password, name))
		passwords = self.passwords
		self.clear();
		self.y_offset = .15
		i = 0
		while i < len(self.names):
			rown = Label(text = self.names[i], anchor="w")														
			self.widgets.append(rown)
			rown.configure(background = self.gui_background, fg=self.gui_foreground)
			rown.place(width = 200, height = 15, relx = .1, rely = self.y_offset, anchor = 'nw')
			rown.bind('<Button-1>', self.editPassword)

			rowp = Label(text = passwords[i], anchor="w")														
			self.widgets.append(rowp)
			rowp.configure(background = self.gui_background, fg=self.gui_foreground)
			rowp.place(width = 200, height = 15, relx = .3, rely = self.y_offset, anchor = 'nw')

			i += 1
			self.y_offset += .03

		name_label = Label(text = "name")
		self.widgets.append(name_label)
		name_label.configure(background = self.gui_background, fg=self.gui_foreground)
		name_label.place(width = 60, height = 15, relx = 0.25, rely = 0.1, anchor=CENTER)

		pass_label = Label(text = "password")
		self.widgets.append(pass_label)
		pass_label.configure(background = self.gui_background, fg=self.gui_foreground)
		pass_label.place(width = 60, height = 15, relx = 0.55, rely = 0.1, anchor=CENTER)

		self.new_name = Entry()
		self.widgets.append(self.new_name)	#add label widget to widget lists
		self.new_name.place(width = 100, height = 15,relx=.35, rely=0.1, anchor=CENTER)

		self.new_password = Entry()
		self.widgets.append(self.new_password)	#add label widget to widget lists
		self.new_password.place(width = 100, height = 15,relx=.65, rely=0.1, anchor=CENTER)
		self.new_password.bind('<Return>', self.setPassword)

	def setPassword(self, event):
		name = (self.new_name.get()[:15]) if len(self.new_name.get()) > 15 else self.new_name.get()
		name = name.strip()
		for e in self.errors:
			e.destroy()
		if(name in self.names or (len(name) < 1)):
			error = Label(text = "invalid username", anchor=CENTER)														
			self.errors.append(error)
			error.configure(background = self.gui_background, fg=self.gui_foreground)
			error.place(width = 200, height = 15, relx = .5, rely = .05, anchor = CENTER)
		else:
			self.ps.addPassword(self.username, 
				self.__password, 
				name, 
				self.new_password.get())
			self.y_offset += .03

			self.show_passwords()


	def editPassword(self, event):

		caller = event.widget
		self.name = (caller["text"])

		self.edit_password = Entry()
		self.widgets.append(self.edit_password)	#add to widgets list
		self.edit_password.place(width = 100, height = 15,relx=.5, rely=.95, anchor=CENTER)
		self.edit_password.bind('<Return>', self.editPasswords)

		self.editLabel = Label(text = "EDIT:", anchor=CENTER)					
		self.editLabel.configure(background = self.gui_background, fg=self.gui_foreground)
		self.editLabel.place(width = 50, height = 15, relx = .4, rely = .95, anchor = CENTER)

		self.deleteLabel = Label(text = "DELETE", anchor=CENTER)					
		self.deleteLabel.configure(background = self.gui_background, fg=self.gui_foreground)
		self.deleteLabel.place(width = 50, height = 15, relx = .6, rely = .95, anchor = CENTER)
		self.deleteLabel.bind('<Button-1>', self.delPassword)
	def editPasswords(self,event):
		self.ps.editPassword(self.username, self.__password, self.name, self.edit_password.get())

		self.editLabel.destroy()
		self.deleteLabel.destroy()
		self.edit_password.destroy()
		self.show_passwords()

	def delPassword(self,event):
		self.editLabel.destroy()
		self.deleteLabel.destroy()
		self.edit_password.destroy()
		self.ps.deletePassword(self.username, self.__password, self.name)
		self.show_passwords()




#when run from command line, the default arguments(none)
#call __main__
#create parent Tk object and send to 'gui'
#start gui loop(google 'event driven gui')
#basically it will "loop"(not really for performance reasons but it has same functionality)
#waiting for an eventListener to trigger, where it will exit the loop
#(again not really, it actually sleeps the thread I believe)
#whereby the eventListener will wake the thread and call the relevant listener object
if __name__ == "__main__":
	root = Tk()
	GUI = gui(root)
	root.mainloop()
	