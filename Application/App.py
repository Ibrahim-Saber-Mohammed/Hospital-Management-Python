#===================================
# @author ibrahim saber Muhammed 
#===================================
#===================================
# import
#===================================
import tkinter as tk
from tkinter import ttk
import Api
from tkinter import messagebox as tkMessageBox
from tkinter import scrolledtext as sctext
import Api


tries = 0 
Hospital_Depatments = ["Cardiology","Critical Care","Gynecology","Orthopaedics"]
# create instense 
Win = tk.Tk()

#=================================
# the window configurations
#=================================
Win.title("Hospital Mangements Systems ")

# setting the Window width and hieght and the x - point , y - point
Win.geometry("550x350+500+150")
#disable resizing 
Win.resizable(False, False)
#changing the grid rows and columns default size
i= 0
while i<12:
	Win.grid_rowconfigure(i, minsize = 20)
	Win.grid_columnconfigure(i, minsize = 10)
	i+=1
	

#===================================================================
	
#=========================================================
def Manage():
	global frame
	#create Button instense to go to Patients window 
	Patient_Button = tk.Button(frame,width=20,bg = "green",fg = "white",text = "Manage Patients",command = lambda:Api.Manage("P"))
	#create Button instense to perform Canceling the current info from user
	doctors_Button = tk.Button(frame,width=20,bg = "green",fg = "white", text = "Manage Doctors", command = lambda:Api.Manage("D"))
	#adding the Buttons to the pop Window
	Appointment_Button = tk.Button(frame,width=20,bg = "green",fg = "white",text = "Appointments",command = lambda:Api.Manage("A"))
	Patient_Button.grid(row = 5, column = 1,sticky = tk.W,padx = 10, pady = 10)
	doctors_Button.grid(row = 5, column = 3,sticky = tk.W,padx = 10, pady = 10)
	Appointment_Button.grid(row = 5, column = 2,sticky = tk.W,padx = 10, pady = 10)

 
#======================================================
def Login():
	global tries
	username = name.get()
	passcode = password.get()
	if tries == 3 :
		Sumbit.configure(state = "disabled")
		tkMessageBox.showinfo("System Locked", "You have finished your valid tries")
		LoginPop.destroy()
	elif username.lower() == "admin" :
		if passcode == "1234" :
			# call the admin page
			LoginPop.destroy()
			Button_Admin.configure(state = "disabled")
			Manage()
			
		else :
			tries+=1
			password_input.delete(0,'end')
			tkMessageBox.showinfo("Login Failed","Password is incorrect..")
	else:
		tkMessageBox.showinfo("Login Failed","User name is incorrect..")
		UserName_input.delete(0,'end')
		password_input.delete(0,'end')
		tries+=1


def Canceling():
	UserName_input.delete(0,'end')
	password_input.delete(0,'end')
	LoginPop.destroy()
		
#Button_Admin lick event Handler
def Admin():
	# create new top Window 
	global LoginPop 
	global Label_UserName 
	global Label_password
	global UserName_input
	global password_input, frame
	LoginPop = tk.Toplevel()
	#grab_set() to disable dealing withe main Window
	LoginPop.grab_set()
	# configuring the Size of the pop Window
	LoginPop.minsize(400, 180)
	#setting the title of the pop Window
	LoginPop.title("Login")
	LoginPop.geometry("300x100+600+300")
	LoginPop.resizable(False, False)
	frame1 = ttk.LabelFrame(LoginPop)
	# create label to describe the Entry to the username field 
	Label_UserName = tk.Label(frame1,width = 15,text ="User name",background = "green",foreground = "white")
	# create label to describe the Entry to the password field  
	Label_password = tk.Label(frame1,width = 15,text ="Password",background = "green",foreground = "white")
	#create Entry field to take input from user representing the user name 
	UserName_input = ttk.Entry(frame1,width=20, textvariable = name)
	# display cursor iniside the Entry field 
	UserName_input.focus()
	#create Entry field to take input from user representing the password
	password_input = ttk.Entry(frame1,width=20,show = "*",textvariable = password)
	# display cursor iniside the Entry field 
	password_input.focus()
	UserName_input.delete(0,'end')
	password_input.delete(0,'end')
	#adding the instenses to the pop window
	Label_UserName.grid(row = 0, column = 0, sticky = tk.W)
	Label_password.grid(row = 2, column = 0, sticky = tk.W)
	UserName_input.grid(row = 0, column = 2, sticky = tk.W)
	password_input.grid(row = 2, column = 2, sticky = tk.W)
	
	#create Button instense to perform Login in to the system
	global Sumbit 
	Sumbit = tk.Button(frame1, text = "Login",command = Login,bg = "green",fg = "white")
	UserName_input.focus()
	#create Button instense to perform Canceling the current info from user
	Cancel = tk.Button(frame1, text = "Cancel", command = Canceling,bg = "green",fg = "white")
	#adding the Buttons to the pop Window
	Sumbit.grid(row = 3, column = 1,sticky = tk.W)
	Cancel.grid(row = 3, column = 2,sticky = tk.W)
	frame1.grid(row = 0, column = 0, padx = 10, pady = 15)
	for child in frame1.winfo_children():
		child.grid_configure(padx = 10, pady = 10)

	
# callback function of the Button_Close 
def Exit():
	# show message and ask if the user want to close the system
	if tkMessageBox.askyesno("Close","Are you sure you want to close") == True :
		# exite the system
		exit()
	else:
		# No operation
		pass	

frame = ttk.LabelFrame(Win, width=50)
# add Label to display Welcome message
Label_start = ttk.Label(frame,
					   text ="Welcome to our Hospital Mangement system",
					   background = "green",
					   foreground = "white",font = ("Times New Roman",15) )
Label_start.grid (row = 0, column = 1, columnspan = 3)

# add Label to display Welcome message
Label_start2 = ttk.Label(frame,
					   text ="Are you Admin ?",
					   background = "green",
					   font = ("Times New Roman",15),
					   foreground = "white"
					  )
Label_start2.grid (row = 1, column = 1, columnspan = 3)
Button_Close = tk.Button(frame, 
						  text = "Exit", 
						  command = Exit,
						  fg = "darkblue",
						  bg = "red" ,
						  width = 20
						  
						  )

Button_Close.grid(row = 4, column = 1,sticky = tk.W)


# variables used in tkinter Entry instenses
name = tk.StringVar()
password = tk.StringVar()


#add Button indicates for admin mode
Button_Admin = tk.Button(frame, 
						  text = "ADMIN", 
						  command = Admin,
						  bg = "blue",
						  fg = "white",
						  width = 20
						  )					  
Button_Admin.grid(row = 4, column = 2,sticky = tk.W)

Button_User = tk.Button(frame, 
						  text = "USER",
						  command = Api.User,
						  bg = "blue",
						  fg = "white",
						  width = 20
						  )					  
Button_User.grid(row = 4, column = 3,sticky = tk.W,)
frame.grid(row = 0, column = 0, padx = 10, pady = 15)
for child in frame.winfo_children():
	child.grid_configure(padx = 10, pady = 10)


# start Gui
Win.mainloop()