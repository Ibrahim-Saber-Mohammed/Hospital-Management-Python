import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as sctext
from tkinter import messagebox as tkMessageBox
import os
import glob

def SelectAppointment(ID):
	global top1, selecctedDate
	global Department, Doctor
	top1.destroy()
	date = selecctedDate.get()
	file = open("../Appointments/"+str(ID)+".txt", "a")
	file.write(str(date) +"\n")
	file.close()
	f2=open("../Departments/"+str(Department)+".txt", "r")
	Lines = f2.readlines()
	f2.close()
	index = Lines.index(str(Doctor))
	DOC_ID = Lines[index+1][:-1]
	file = open("../Doctors/"+str(DOC_ID)+".txt", "r")
	Data = file.readlines()
	file.close()
	count = 0
	os.remove("../Doctors/"+str(DOC_ID)+".txt")
	file2 = open("../Doctors/"+str(DOC_ID)+".txt", "a")
	for line in Data:
		if line ==date and count == 0 :
			count =1
		else :
			file2.write(line)

	file2.close()
	
def sellectinggAvailableTimes(ID):
	global Department, Doctor, selecctedDate
	Department = Read_Depar.get()
	Doctor= Patient_Doctor.get()
	selecctedDate=tk.StringVar()
	global top1
	top1 = tk.Toplevel()
	top1.title("Selecting appointment")
	top1.geometry("450x300+550+350")
	Frame= ttk.LabelFrame(top1)
	Label1 = tk.Label(Frame, text = "Choose An appointment",width=40,background = "green",foreground = "white").grid(row = 1,
													column = 0, 
													sticky = tk.W
													)
	appointmentChoosen = ttk.Combobox(Frame,width =40,textvariable=selecctedDate, state = 'readonly')
	appointmentChoosen.grid(column = 0, row = 2)
	f2=open("../Departments/"+str(Department)+".txt", "r")
	Lines = f2.readlines()
	f2.close()
	index = Lines.index(str(Doctor))
	DOC_ID = Lines[index+1][:-1]
	file = open("../Doctors/"+str(DOC_ID)+".txt", "r")
	Data = file.readlines()
	searchline ="------\n"
	line_index = Data.index(searchline)
	index = line_index+1
	Appointments = list()
	while index < len(Data):
		Appointments.append(Data[index])
		index+=1
	appointmentChoosen['values'] = Appointments
	appointmentChoosen.current(0)
	BtnFrame=ttk.LabelFrame(Frame)
	DoneBtn= tk.Button(BtnFrame, text = "Done",bg = "green",fg = "white",command =lambda:SelectAppointment(ID)).grid(row = 3, column = 3)
	BtnFrame.grid(row = 3, column = 2,padx=30, pady = 15)
	Frame.grid(row = 0, column = 2,padx=30, pady = 15)
	for child in Frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)

def Done():
	global top
	top.destroy()

def SaveAppointment(ID):
	file = open("../Doctors/"+str(ID)+".txt", "a")
	day = Doctor_Appointment_Day.get()
	hour = Doctor_Appointment_Hour.get()
	minuit = Doctor_Appointment_min.get()
	if int(hour)>12 or ( int(hour)==12 and int(minuit) >0) :
		appointment = str(day)+",	 "+str(  int(hour)-12  )+" : "+str(minuit)+" PM"
	else:
		appointment = str(day)+",	 "+str( int(hour) )+" : "+str(minuit)+" AM"
	file.write(appointment+"\n")
	file.close()
def settingAvailableTimes(ID):
	global top
	top = tk.Toplevel()
	top.title("Availabe times")
	Frame= ttk.LabelFrame(top)
	global Doctor_Appointment_Day
	Doctor_Appointment_Day = tk.StringVar()
	global Doctor_Appointment_Hour
	Doctor_Appointment_Hour = tk.StringVar()
	global Doctor_Appointment_min
	Doctor_Appointment_min = tk.StringVar()
	
	Text = "Doctor Appointment" 

	Label1 = tk.Label(Frame, text = "Day",width=15,background = "green",foreground = "white").grid(row = 1,
													column = 0, 
													sticky = tk.W
													)
	DayChoosen = ttk.Combobox(Frame,width =15,textvariable=Doctor_Appointment_Day, state = 'readonly')
	DayChoosen.grid(column = 0, row = 2)
	Days=["Saturday", "Sunday","Monday", "Tusday","Wednesday","Thursday","Friday"]
	DayChoosen['values'] = Days
	DayChoosen.current(0)
	PD_Label = tk.Label(Frame, text = Text,width=60,background = "green",foreground = "white").grid(row = 0,
													column = 0, 
													columnspan = 6,
													sticky = tk.W
													)
	Label2 = tk.Label(Frame, text = "Hour",width=15,background = "green",foreground = "white").grid(row = 1,
													column = 2, 
													sticky = tk.W
													)
	HourChoosen = ttk.Combobox(Frame,width =15,textvariable=Doctor_Appointment_Hour, state = 'readonly')
	HourChoosen.grid(column = 2, row = 2)
	counter = 10
	Hours=["01","02","03","04","05","06","07","08","09"]
	
	while counter<=24:
		Hours.append(str(counter))
		counter+=1
	HourChoosen['values'] = Hours
	HourChoosen.current(0)
	Label3 = tk.Label(Frame, text = "minuits",width=15,background = "green",foreground = "white").grid(row = 1,
													column = 3, 
													sticky = tk.W
													)
	MinChoosen = ttk.Combobox(Frame,width =15,textvariable=Doctor_Appointment_min, state = 'readonly')
	MinChoosen.grid(column = 3, row = 2)
	counter = 10
	Min=["00","01","02","03","04","05","06","07","08","09"]
	while counter<=60:
		Min.append(str(counter))
		counter+=1
	MinChoosen['values'] = Min
	MinChoosen.current(0)
	BtnFrame=ttk.LabelFrame(Frame)
	Done_Btn = tk.Button(BtnFrame, text = "Done",bg = "green",fg = "white",command =Done).grid(row = 3, column = 2)
	insert_Btn= tk.Button(BtnFrame, text = "Insert",bg = "green",fg = "white",command =lambda:SaveAppointment(ID)).grid(row = 3, column = 3)
	BtnFrame.grid(row = 3, column = 2,padx=30, pady = 15)
	Frame.grid(row = 0, column = 2,padx=30, pady = 15)
	for child in Frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)





#====================================================================================================
def StoreNewData(option):
	global Add_pop
	ID = Read_ID.get() 
	age= Read_Age.get()
	Department = Read_Depar.get()
	Name =Read_name.get()
	Gender = Read_Gender.get()
	Doctor= Patient_Doctor.get()
	if option !="A":
		Describtion = Details.get('1.0', 'end')
		Address= Read_Address.get()
		PPhone =Read_Phone.get()
	if option == "P":
		try :
			file = open("../patients/"+str(ID)+".txt", "r")
		except:
			Add_pop.destroy()
			popfinal.destroy()
			file = open("../patients/"+str(ID)+".txt", "w")
			file.write("*ID : "+str(ID)+"\n" )
			file.write("*Name : "+str(Name)+"\n" )
			file.write("*Phone number: "+str(PPhone)+"\n" )
			file.write("*Gender : "+str(Gender)+"\n" )
			file.write("*Age : "+str(age)+"\n" )
			file.write("*Address : "+str(Address)+"\n" )
			file.write("*Doctor : "+str(Doctor) )
			file.write("*Department : "+str(Department)+"\n" )
			file.write("*Describtion : "+str(Describtion) )
			file.write("------\n" )
			file.close()	
		else:
			file.close()
			tkMessageBox.showerror("Error", "This Id had been Taken Before")
	elif option == "D":
		try :
			file = open("../Doctors/"+str(ID)+".txt", "r")
		except:
			Add_pop.destroy()
			popfinal.destroy()
			file = open("../Doctors/"+str(ID)+".txt", "w")
			file.write("*ID : "+str(ID)+"\n" )
			file.write("*Name : "+str(Name)+"\n" )
			file.write("*Phone number: "+str(PPhone)+"\n" )
			file.write("*Gender : "+str(Gender)+"\n" )
			file.write("*Age : "+str(age)+"\n" )
			file.write("*Address : "+str(Address)+"\n" )
			file.write("*Department : "+str(Department)+"\n" )
			file.write("*Describtion : "+str(Describtion) )
			file.write("------\n" )
			file.close()	
			f2=open("../Departments/"+str(Department)+".txt", "a")
			f2.write(str(Name)+"\n" )
			f2.write(str(ID)+"\n" )
			f2.close()
			settingAvailableTimes(ID)
		else:
			file.close()
			tkMessageBox.showerror("Error", "This Id had been Taken Before")
	elif option == "A":
		try :
			file = open("../Appointments/"+str(ID)+".txt", "r")
		except:
			Add_pop.destroy()
			popfinal.destroy()
			file = open("../Appointments/"+str(ID)+".txt", "w")
			file.write("*ID : "+str(ID)+"\n" )
			file.write("*Name : "+str(Name)+"\n" )
			file.write("*Gender : "+str(Gender)+"\n" )
			file.write("*Age : "+str(age)+"\n" )
			file.write("*Department : "+str(Department)+"\n" )
			file.write("*Doctor : "+str(Doctor) )
			file.write("*Appointment\n" )
			file = open("../Appointments/"+str(ID)+".txt", "a")
			file.write("------\n" )
			file.close()
			sellectinggAvailableTimes(ID)
		else:
			file.close()
			tkMessageBox.showerror("Error", "This Id had been Taken Before")	
		
		
		
def WriteEditedData(option):
	global ID
	age= Read_Age.get()
	Department = Read_Depar.get()
	Doctor= Patient_Doctor.get()
	Name =Read_name.get()
	Gender = Read_Gender.get()
	if option!="A":
		PPhone =Read_Phone.get()
		Describtion = Details.get('1.0', 'end')
		Address= Read_Address.get()
	else :
		pass
	Add_pop.destroy()
	popfinal.destroy()
	if option =="P":
		file = open("../patients/"+str(ID)+".txt", "w")
		file.write("*ID : "+str(ID)+"\n" )
		file.write("*Name : "+str(Name)+"\n" )
		file.write("*Phone number: "+str(PPhone)+"\n" )
		file.write("*Gender : "+str(Gender)+"\n" )
		file.write("*Age : "+str(age)+"\n" )
		file.write("*Address : "+str(Address)+"\n" )
		file.write("*Doctor : "+str(Doctor) )
		file.write("*Department : "+str(Department)+"\n" )
		file.write("*Describtion : "+str(Describtion) )
		file.write("------\n" )
		file.close()		
	elif option == "D":
		updateDoctorsnames(ID)
		file = open("../Doctors/"+str(ID)+".txt", "w")
		file.write("*ID : "+str(ID)+"\n" )
		file.write("*Name : "+str(Name)+"\n" )
		file.write("*Phone number: "+str(PPhone)+"\n" )
		file.write("*Gender : "+str(Gender)+"\n" )
		file.write("*Age : "+str(age)+"\n" )
		file.write("*Address : "+str(Address)+"\n" )
		file.write("*Department : "+str(Department)+"\n" )
		file.write("*Describtion : "+str(Describtion) )
		file.write("------\n" )
		file.close()	
		f2=open("../Departments/"+str(Department)+".txt", "a")
		f2.write(str(Name)+"\n" )
		f2.write(str(ID)+"\n" )
		f2.close()
		settingAvailableTimes(ID)
	elif option == "A":
		f2=open("../Departments/"+str(Department)+".txt", "r")
		Lines = f2.readlines()
		f2.close()
		index = Lines.index(str(Doctor))
		DOC_ID = Lines[index+1][:-1]
		f1 = open("../Appointments/"+str(ID)+".txt", "r")
		Lines = f1.readlines()
		f1.close()
		file = open("../Doctors/"+str(DOC_ID)+".txt", "a")
		file.write(str(Lines[-2]) )
		file.close()
		file = open("../Appointments/"+str(ID)+".txt", "w")
		file.write("*ID : "+str(ID)+"\n" )
		file.write("*Name : "+str(Name)+"\n" )
		file.write("*Gender : "+str(Gender)+"\n" )
		file.write("*Age : "+str(age)+"\n" )
		file.write("*Department : "+str(Department)+"\n" )
		file.write("*Doctor : "+str(Doctor) )
		file.write("------\n" )
		file.close()	
		sellectinggAvailableTimes(ID)


def Gui_build2(op,call):
	if op =="P":
		title = "Patient Details"
	elif op == "D":
		title = "Doctor Details"
	elif op == "A":
		title = "Appointment Details"
	name = Read_name.get().strip()
	add = Read_Address.get()
	if name=="":
		tkMessageBox.showerror("Error", "missed data 'name' field is empty" )
		
	else:
		try:
			age= int(Read_Age.get())
		except:
			tkMessageBox.showerror("Error", "Age Must be numeric value ")
		
		else :
			if op !="A":
				if add=="":
					tkMessageBox.showerror("Error", "missed data 'address' field is empty" )
				else:
					pass
				try : 
					PPhone = int(Read_Phone.get())
				except :
					tkMessageBox.showerror("Error", "Phone Number can't contain characters")
				else :
					Gui_build2_Handeler(op,call,title)
			else:
				Gui_build2_Handeler(op,call,title)
		
def Gui_build2_Handeler(op,call,title):
		
	global popfinal
	global Add_pop
	Add_pop.destroy()
	popfinal = tk.Toplevel()
	popfinal.geometry("480x350+350+250")
	popfinal.title(title)
	popfinal.grab_set()
	popfinal.resizable(False, False)
	Frame = ttk.LabelFrame(popfinal,text =title)
	BtnFrame = ttk.LabelFrame(popfinal)
	#==========================================================================
	if op =="P" or op =="A" :
		file = open("../Departments/"+Read_Depar.get()+".txt","r")
		AllLines = file.readlines()
		List_Doctors = list()
		i= 0
		while i <len(AllLines):
			List_Doctors.append(AllLines[i])
			i+=2
			
		file.close()
		DocChoosen = ttk.Combobox(Frame,width =12,textvariable=Patient_Doctor, state = 'readonly')
		DocChoosen.grid(column = 1, row = 1)
		DocChoosen['values'] = List_Doctors
		DocChoosen.current(0)
		PD_Label = tk.Label(Frame, text = "Doctor Name",width=20,background = "green",foreground = "white").grid(row = 1,
														column = 0, 
														sticky = tk.W
														)
	else:
		pass
		
	if op!="A":
		PDesc_Label = tk.Label(Frame, text = "Describtion",width=20,background = "green",foreground = "white").grid(row = 2,
															column = 0, 
															sticky = tk.W
															)
		global Details
		Details= sctext.ScrolledText(Frame,width=30, height = 4, wrap=tk.WORD)													
		Details.grid(column = 0, columnspan =2)
	else:
		pass
		
	if call == "add":
		Done_Btn = tk.Button(BtnFrame, text = "Done",bg = "green",fg = "white",command =lambda:StoreNewData(op))
		ID_Label = tk.Label(Frame, text = "ID",width = 20,background = "green",foreground = "white").grid(row = 0,
												column = 0, 
												sticky = tk.W
												)
		PID = ttk.Entry(Frame,textvariable = Read_ID, width = 40)
		PID.focus()
		PID.grid(row = 0,column = 1,sticky = tk.W)
	elif call == "edit":
		Done_Btn = tk.Button(BtnFrame, text = "Done",bg = "blue",fg = "white",command = lambda:WriteEditedData(op))
	else :
		pass
	Done_Btn.grid(row = 9, column = 1)
	Frame.grid(row = 1, column = 2,padx=30, pady = 15)
	BtnFrame.grid(row = 2, column = 2,padx=30, pady = 15)
	for child in Frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)
	
				

def Gui_build1(data):
	global Add_pop
	global Patientpop ,BtnFrame,Frame
	Patientpop.destroy()
	Add_pop = tk.Toplevel()
	Add_pop.geometry("600x450+350+250")
	if data == "P":
		title = "Patient Details"
	elif data == "D":
		title = "Doctor Details"
	elif data == "A":
		title = "Appointment Details"
	Add_pop.title(title)
	Add_pop.grab_set()
	Frame = ttk.LabelFrame(Add_pop,text =title)
	BtnFrame = ttk.LabelFrame(Add_pop)
	global Read_name 
	Read_name   = tk.StringVar()
	global Read_ID
	Read_ID     = tk.StringVar()
	global Patient_Doctor
	Patient_Doctor = tk.StringVar()
	global Read_Depar
	Read_Depar  = tk.StringVar()
	global Read_Depart
	Read_Depart =tk.StringVar()
	global Read_Age
	Read_Age    = tk.StringVar()
	global Read_Phone
	Read_Phone    = tk.StringVar()
	global Read_Address
	Read_Address = tk.StringVar()
	global Read_Gender
	Read_Gender = tk.StringVar()

	Name_Label = tk.Label(Frame, text = "Name",width = 20,background = "green",foreground = "white").grid(
													row = 0, 
													column = 0,
													sticky = tk.W
													)
	global PName
	PName = ttk.Entry(Frame, textvariable = Read_name, width = 40)
	PName.focus()
	PName.grid(row = 0,column =1,sticky = tk.W)
	
	if data !="A":
	
		Phone_Label = tk.Label(Frame, text = "Phone Number",width = 20,background = "green",foreground = "white").grid(
													row = 1, 
													column = 0,
													sticky = tk.W
													)
		global Phone
		Phone = ttk.Entry(Frame, textvariable = Read_Phone, width = 40)
		Phone.focus()
		Phone.grid(row = 1,column =1,sticky = tk.W)
		Address_Label = tk.Label(Frame, text = "Address",width = 20,background = "green",foreground = "white").grid(
														row = 2, 
														column = 0,
														sticky = tk.W
													)
		global PAddress
		PAddress = ttk.Entry(Frame, textvariable = Read_Address, width = 40)												
		PAddress.focus()
		PAddress.grid(row = 2,column =1,sticky = tk.W)
		PDEP_Label = tk.Label(Frame,width = 20 ,text = "Department Name",background = "green",foreground = "white").grid(row = 3,
															column = 0, 
															sticky = tk.W
															)	
															
	DepChoosen = ttk.Combobox(Frame,width =20,textvariable=Read_Depar,state = 'readonly' )
	DepChoosen.grid(column = 1, row = 3)
	DepChoosen['values']= ("Cardiology","Critical Care","Gynecology","Orthopaedics")
	DepChoosen.current(0)
	
	PGend_Label = tk.Label(Frame, text = "Gender",width = 20,background = "green",foreground = "white").grid(row = 4,
														column = 0, 
														sticky = tk.W
														)
	Gend = ttk.Combobox(Frame,width =20,textvariable=Read_Gender,state = 'readonly' )
	Gend.grid(column = 1, row = 4)
	Gend['values']= ("Male", "Female")
	Gend.current(0)
	PAge_Label = tk.Label(Frame, text = "Age",width = 20,background = "green",foreground = "white").grid(row = 5,
														column = 0, 
														sticky = tk.W
														)
	global PAge
	PAge = ttk.Entry(Frame,textvariable = Read_Age, width = 40)
	PAge.focus()
	PAge.grid(row = 5,column =1,sticky = tk.W)
	
#---------------------------------------------------------------------------
def ADD(op):
	Gui_build1(op)	
	global BtnFrame
	Next_Btn = tk.Button(BtnFrame, text = "Next",bg = "blue", fg = "white",command = lambda:Gui_build2(op,"add"))
	Next_Btn.grid(row = 10, column = 1)
	Frame.grid(row = 1, column = 2,padx=30, pady = 15)
	BtnFrame.grid(row = 2, column = 2,padx=30, pady = 15)
	for child in Frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)
		
#==============================================================================================================

def EDIT_Gui(name):
	if name == "P":
		global ID
		ID = Read_ID.get()
		try :
			file = open("../patients/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "Enter the correct ID")
		else:
			Edit_pop.destroy()
			global EDIT_pop2
			Gui_build1(name)													
			Next_Btn = tk.Button(BtnFrame, text = "Next",bg = "green",fg = "white",command =lambda:Gui_build2(name,"edit"))
			Next_Btn.grid(row = 10, column = 1)
			Frame.grid(row = 1, column = 2,padx=30, pady = 15)
			BtnFrame.grid(row = 2, column = 2,padx=30, pady = 15)
			for child in Frame.winfo_children():
				child.grid_configure(padx = 10, pady = 10)
				
	elif name == "D":
		ID = Read_ID.get()
		try :
			file = open("../Doctors/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "Enter the correct ID")
		else:
			Edit_pop.destroy()
			global EDIT_pop2
			Gui_build1(name)													
			Next_Btn = tk.Button(BtnFrame, text = "Next",bg = "green",fg = "white",command =lambda:Gui_build2(name,"edit"))
			Next_Btn.grid(row = 10, column = 1)
			Frame.grid(row = 1, column = 2,padx=30, pady = 15)
			BtnFrame.grid(row = 2, column = 2,padx=30, pady = 15)
			for child in Frame.winfo_children():
				child.grid_configure(padx = 10, pady = 10)
	elif name == "A":
		ID = Read_ID.get()
		try :
			file = open("../Appointments/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "Enter the correct ID")
		else:
			Edit_pop.destroy()
			global EDIT_pop2
			Gui_build1(name)													
			Next_Btn = tk.Button(BtnFrame, text = "Next",bg = "green",fg = "white",command =lambda:Gui_build2(name,"edit"))
			Next_Btn.grid(row = 10, column = 1)
			Frame.grid(row = 1, column = 2,padx=30, pady = 15)
			BtnFrame.grid(row = 2, column = 2,padx=30, pady = 15)
			for child in Frame.winfo_children():
				child.grid_configure(padx = 10, pady = 10)
		

def EDIT_DELETE_DISP_GUI(who,call):
	global Patientpop 
	global Edit_pop
	global Read_ID
	global PID
	global Enter
	global Btn2Frame
	Read_ID = tk.StringVar()
	Patientpop.destroy()
	Edit_pop = tk.Toplevel()
	Edit_pop.geometry("450x140+500+300")
	if who == "P":
		title = "Patient Details"
	elif who == "D":
		title = "Doctor Details"
	elif who == "A":
		title = "Appointment Details"
	Edit_pop.title(title)
	Edit_pop.grab_set()
	Edit_pop.resizable(False, False)
	Btn2Frame = ttk.LabelFrame(Edit_pop)
	ID_Label = tk.Label(Btn2Frame,width = 20,background = "green",foreground = "white", text = "ID").grid(row = 0,
													column = 0,
													sticky = tk.W
													)
	PID = ttk.Entry(Btn2Frame,textvariable = Read_ID, width = 30)
	PID.focus()
	PID.grid(row = 0,column = 1,sticky = tk.W,columnspan=2)
	if call == "edit":
		Enter = tk.Button(Btn2Frame, text = "Submit",command = lambda:EDIT_Gui(who),bg = "green",fg = "white")
	elif call == "Delete":
		Enter = tk.Button(Btn2Frame, text = "Submit",command = lambda:DELTE_Data(who),bg = "green",fg = "white")
	elif call == "Display":
		Enter = tk.Button(Btn2Frame, text = "Submit",command = lambda:DISPLAY_Data(who),bg = "green",fg = "white")
	
	Enter.grid(row = 1, column = 0)
	Btn2Frame.grid(row = 2, column = 2,padx=30, pady = 15)
	for child in Btn2Frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)

def DELTE_Data(op):	
	global Read_ID
	ID = Read_ID.get()
	if op == "P":
		try :
			file = open("../patients/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "ID is not Found")
		else:
			file.close()
			Edit_pop.destroy()
			os.remove("../patients/"+str(ID)+".txt")
	elif op =="D":
		try :
			file = open("../Doctors/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "ID is not Found")
		else:
			file.close()
			updateDoctorsnames(ID)
			Edit_pop.destroy()
			os.remove("../Doctors/"+str(ID)+".txt")
	elif op =="A":
		try :
			file = open("../Appointments/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "ID is not Found")
		else:
			Edit_pop.destroy()
			Lines = file.readlines()
			file.close()
			Department = Lines[4][14:-1]
			Doctor = Lines[5][10:]
			f2=open("../Departments/"+str(Department)+".txt", "r")
			Lines = f2.readlines()
			f2.close()
			index = Lines.index(str(Doctor))
			DOC_ID = Lines[index+1][:-1]
			f1 = open("../Appointments/"+str(ID)+".txt", "r")
			Lines = f1.readlines()
			f1.close()
			file = open("../Doctors/"+str(DOC_ID)+".txt", "a")
			file.write(str(Lines[-2]) )
			file.close()
			os.remove("../Appointments/"+str(ID)+".txt")
			
def updateDoctorsnames(ID):
	file = open("../Doctors/"+str(ID)+".txt", "r")
	Data = file.readlines()
	Name=Data[1][8:]
	Department = Data[6][14:-1]
	file.close()	
	f2=open("../Departments/"+str(Department)+".txt", "r")
	lines=f2.readlines()
	f2.close()
	count = 0
	os.remove("../Departments/"+str(Department)+".txt")
	file2 = open("../Departments/"+str(Department)+".txt", "a")
	for line in lines:
		if (line == Name and count == 0):
			count =1
		elif (line[:-1] == str(ID) and count == 1 ):
			count=2
		else :
			file2.write(line)

	file2.close()
	
def DISPLAY_Data(op):
	global Read_ID
	global Details
	ID = Read_ID.get()
	if op == "P":
		try :
			file = open("../patients/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "ID is not Found")
		else:
			Edit_pop.destroy()
			Data_List = file.readlines()
			Edit1_pop = tk.Toplevel()
			Edit1_pop.grab_set()
			Edit1_pop.geometry("600x450+350+250")
			Edit1_pop.title("Patient Details")
			Frame = ttk.LabelFrame(Edit1_pop,text ="Patient Details")
			Frame.grid(row = 1, column = 2,padx=30, pady = 15)
			Details= sctext.ScrolledText(Frame,width=50, height = 15, wrap=tk.WORD, font = ("Times New Roman", 15))
			Details.grid(column = 0, columnspan =4,pady = 10, padx = 10)
			for line in Data_List:
				Details.insert(tk.INSERT,line)
			Details.configure(state ='disabled')
	elif op == "D":
		try :
			file = open("../Doctors/"+str(ID)+".txt", "r")
		except:
			tkMessageBox.showerror("Error", "ID is not Found")
		else:
			Edit_pop.destroy()
			Data_List = file.readlines()
			Edit1_pop = tk.Toplevel()
			Edit1_pop.grab_set()
			Edit1_pop.geometry("600x450+350+250")
			Edit1_pop.title("Doctor Details")
			Frame = ttk.LabelFrame(Edit1_pop,text ="Doctor Details")
			Frame.grid(row = 1, column = 2,padx=30, pady = 15)
			Details= sctext.ScrolledText(Frame,width=50, height = 15, wrap=tk.WORD, font = ("Times New Roman", 15))
			Details.grid(column = 0, columnspan =4,pady = 10, padx = 10)
			for line in Data_List:
				Details.insert(tk.INSERT,line)
			Details.configure(state ='disabled')

def DisplayAll(op):
	Patientpop.destroy()
	myFiles = list()
	title = ""
	Data = list()
	if op =="P":
		title = "Patients Details"
		os.chdir(r'../patients/')
		myFiles = glob.glob('*.txt')
		for file in myFiles:
			file1 = open("../patients/"+str(file), "r")
			Data.append(file1.read())
			file1.close()
			Data.append("********************************************\n\n")
	elif op == "D":
		title = "Doctors Details"
		os.chdir(r'../Doctors/')
		myFiles = glob.glob('*.txt')
		for file in myFiles:
			file1 = open("../Doctors/"+str(file), "r")
			Data.append(file1.read())
			file1.close()
			Data.append("********************************************\n\n")
	elif op == "H":
		title = "Departments Details"
		file1 = open("../Departments/Hospital.txt", "r")
		Data.append(file1.read())
		file1.close()
	Edit1_pop = tk.Toplevel()
	Edit1_pop.grab_set()
	Edit1_pop.geometry("1050x450+350+250")
	Edit1_pop.title(title)
	Frame = ttk.LabelFrame(Edit1_pop,text =title)
	Frame.grid(row = 1, column = 2,padx=30, pady = 15)
	Details= sctext.ScrolledText(Frame,width=95, height = 15, wrap=tk.WORD, font = ("Times New Roman", 15))
	Details.grid(column = 0, columnspan =4,pady = 10, padx = 10)
	for line in Data:
		Details.insert(tk.INSERT,line)
	Details.configure(state ='disabled')
		
		
		
def StartGui(List):
	global Patientpop 
	Patientpop = tk.Toplevel()
	#grab_set() to disable dealing withe main Window
	Patientpop.grab_set()
	# configuring the Size of the pop Window
	Patientpop.minsize(400, 250)
	Patientpop.geometry("400x100+550+300")
	#setting the title of the pop Window
	Patientpop.title(List[1])
	Buttons_frame = ttk.LabelFrame(Patientpop)
	Add_Button = tk.Button(Buttons_frame,text = List[2],
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:ADD(List[0])
							)
	Edit_Button = tk.Button(Buttons_frame,text = List[3],
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:EDIT_DELETE_DISP_GUI(str(List[0]),"edit")
							)
	Delete_Button = tk.Button(Buttons_frame,text = List[4],
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:EDIT_DELETE_DISP_GUI(str(List[0]),"Delete")
							)						
	if List[0] !="A":	
		Display_Button = tk.Button(Buttons_frame,text = List[5],
								bg = "green",
								fg = "white",
								width = 20,
								command = lambda:EDIT_DELETE_DISP_GUI(str(List[0]),"Display")
								)
		Display_Button.grid(row = 3, column = 3, sticky = tk.W)
		
	Add_Button.grid(row = 1, column = 1, sticky = tk.W)
	Edit_Button.grid(row = 1, column = 3, sticky = tk.W)
	Delete_Button.grid(row = 3, column = 1, sticky = tk.W)
	Buttons_frame.grid(row = 1, column = 2, padx=30, pady = 30)
	for child in Buttons_frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)
	
#======================================================================================================================

	
def Manage(call):
	Patient_Buttons = ["P","Manage Patients","Add Patient","Edit Patient","Delete Patient","Display Patient" ]
	Doctors_Buttons = ["D","Manage Doctors","Add Doctor","Edit Doctor","Delete Doctor","Display Doctor" ]
	Appointment_Buttons = ["A","Manage Appointments","Book Appointment","Edit Appointment","Cancel Appointment"]
	if call == "P":
		StartGui(Patient_Buttons)
	elif call== "D":
		StartGui(Doctors_Buttons)
	elif call== "A":
		StartGui(Appointment_Buttons)
#================================================================================================================	
def User():
	global Patientpop 
	Patientpop = tk.Toplevel()
	#grab_set() to disable dealing withe main Window
	Patientpop.grab_set()
	# configuring the Size of the pop Window
	Patientpop.minsize(400, 250)
	Patientpop.geometry("400x100+550+300")
	#setting the title of the pop Window
	Patientpop.title("User Options")
	Buttons_frame = ttk.LabelFrame(Patientpop)
	
	DisplayAllP_Button = tk.Button(Buttons_frame,text = "View All Patients",
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:DisplayAll("P")
							)
	DisplayH_Button = tk.Button(Buttons_frame,text = "All Hospital Departments",
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:DisplayAll("H")
							)
	DisplayAllD_Button = tk.Button(Buttons_frame,text = "View All Doctors",
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:DisplayAll("D")
							)
	DisplayP_Button = tk.Button(Buttons_frame,text = "View Patient",
							bg = "green",
						    fg = "white",
							width = 20,
							command = lambda:EDIT_DELETE_DISP_GUI("P","Display")
							)						
	
	DisplayD_Button = tk.Button(Buttons_frame,text = "View Doctor",
								bg = "green",
								fg = "white",
								width = 20,
								command = lambda:EDIT_DELETE_DISP_GUI("D","Display")
								)
	DisplayD_Button.grid(row = 3, column = 3, sticky = tk.W)
		
	DisplayAllP_Button.grid(row = 1, column = 1, sticky = tk.W,columnspan= 2)
	DisplayAllD_Button.grid(row = 1, column = 3, sticky = tk.W,columnspan= 2)
	DisplayP_Button.grid(row = 3, column = 1, sticky = tk.W,columnspan= 2)
	DisplayH_Button.grid(row = 4, column = 2, sticky = tk.W,columnspan= 2)
	Buttons_frame.grid(row = 1, column = 2, padx=30, pady = 30)
	for child in Buttons_frame.winfo_children():
		child.grid_configure(padx = 10, pady = 10)
	

