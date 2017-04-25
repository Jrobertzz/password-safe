#!/usr/bin/python

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class gui(Tk):
	def __init__(self, master):

		#color config
		self.gui_background = 'gray24'						#background color
		self.gui_foreground = 'black'						#foreground in the context
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

		#define array to store all widgets(window elements)
		#I did not add background to widgets list as canvas will always be present
		self.widgets = []

		self.file = open("users.txt", 'r+')
		self.UserList = self.file.read().split(' ')

		self.initialize()

	def initialize(self):
		#destroy all non-permanent objects(see def clear)
		self.clear()

		#set head to start of file and split by space
		#(to be changed, split by space for quick prototyping)
		self.file.seek(0)
		self.UserList = self.file.read().split(' ')

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
			user.place(width = 50, height = 10,relx=x_pos, rely=0.5, anchor=CENTER)		#
			counter += 1																#
		#################################################################################

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)
		new_user.bind("<Button-1>", self.NewUserOnClick)
		new_user.configure(bg=self.gui_background, fg=self.gui_foreground)
		new_user.place(width = 80, height = 10,relx=.5, rely=0.55, anchor=CENTER)

	def UserOnClick(self, event):
		#ugly way to get widget value, I used a better solution elsewhere
		#though its not working for clicking on user label
		#to login atm, this works
		caller = event.widget
		self.login(caller["text"])

	def NewUserOnClick(self, event):
		self.clear()

		#create_polygon draws to canvas, takes (x1, y1, x2, y2, x3, y3...)
		self.background.create_polygon((0,0,0,50,50,0), fill='black')

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		new_user = Label(text = "NEW USER")
		self.widgets.append(new_user)	#add label widget to widget lists
		new_user.bind("<Button-1>", self.NewUserOnClick)	#bind mouseclick listener, call NewUserOnClick on click
		new_user.configure(bg=self.gui_background, fg=self.gui_foreground)
		new_user.place(width = 80, height = 10,relx=.5, rely=0.45, anchor=CENTER)

		#Entry is a text box that accepts input
		self.new_username = Entry()
		self.widgets.append(self.new_username)	#add label widget to widget lists
		self.new_username.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_username.bind('<Return>', self.NewUser) #bind to enter, call NewUser

	def NewUser(self, event):
		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		user = Label(text = self.new_username.get())	#set text to new_username Entry text
		user.configure(background = self.gui_background, fg=self.gui_foreground)
		self.widgets.append(user)	#add label widget to widget lists
		user.place(width = 80, height = 10,relx=.5, rely=0.45, anchor=CENTER)

		self.new_password = Entry()
		self.widgets.append(self.new_password)
		self.new_password.place(width = 100, height = 20,relx=.5, rely=0.52, anchor=CENTER)
		self.new_password.bind('<Return>', self.NewPassword)

	def NewPassword(self, event):
		#ENCRYPT AND STORE PASSWORD
		self.file.write(" " + self.new_username.get()) #store new_username Entry text
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

		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		user = Label(text = username)
		self.widgets.append(user)		#add to widgets list
		user.configure(bg=self.gui_background, fg=self.gui_foreground)		#set background/foregroung
		user.place(width = 50, height = 10,relx=.5, rely=0.48, anchor=CENTER)

		#Entry is a textbox with event listeners
		self.password = Entry();
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
		__password = self.password.get()
		self.password.delete(0, END)	#clear Entry object password's textbox(possibly not neccessary)
		self.clear()					#remove all non-permanent widgets
		self.passwords()

	def passwords(self):
		#Label is Tkinter onject that displays text
		#and has some config settings such as text and background color
		user = Label(text = self.username)
		self.widgets.append(user)		#add to widgets list
		user.configure(background = self.gui_background, fg=self.gui_foreground)
		user.place(width = 100, height = 20,relx=.5, rely=0.05, anchor=CENTER)

		#temporary, TODO: replace with customizable list
		groups = ['Social Media', 'Entertainment', 'Education', 'Gaming', 'Other']

		#############################################################################################
		#make a set of label objects for all password groups										#
		#Label is Tkinter onject that displays text 												#
		#and has some config settings such as text and background color 							#
																									#
		counter = 0																					#
		while counter < len(groups):																#
			#ScrolledText is a Tkinter object that is affectively									#
			#a textbox widget paired with scrollbar													#
			#packed in its own frame																#
			#a frame is basically a parent object that												#
			#can contain other Tkinter objects														#
			passwords = ScrolledText()		 														#
			self.widgets.append(passwords)															#
			self.widgets.append(passwords.frame)													#
			#to disable/enable editing use state='normal' and state='disabled' respectively			#
			passwords.configure(background = self.gui_background,									#
								fg=self.gui_foreground,												#
								highlightthickness=0,												#
								borderwidth=0)														#
			#removes scrollbar																		#
			passwords.vbar.forget()																	#
																									#
			#ScrollText handles test like a text editor does with 'justified'						#
			#text formatting is defined with 'tag_config'											#
			passwords.tag_config('justified', justify=CENTER)										#
			passwords.insert(INSERT, groups[counter], 'justified')									#
			x_offset = (counter+1)/(len(groups)+1)													#
			passwords.place(width = 120, height = 400,relx=x_offset, rely=0.5, anchor=CENTER)		#
																									#
			counter += 1																			#
		#############################################################################################

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
	