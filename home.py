from tkinter import *
from tkinter import font as tkFont
import sqlite3

root = Tk()

#root.geometry('800x600')
root.title("Student Database")

currFont = tkFont.Font(family='Helvetica', size=15)

def showall():
	conn = sqlite3.connect(r'database/stud.db')

	c = conn.cursor()

	c.execute("SELECT * FROM '20192023'")
	outputs = c.fetchall()
	print(outputs)

	#loop
	print_output = ''
	'''
	for output in outputs:
		print_output += str(output[0]) + "\t\t" + str(output[1]) + "\t\t" + str(output[2]) + "\t\t" + str(output[3]) + "\t\t" + str(output[4]) + "\t\t" + str(output[5]) + "\t\t" + str(output[6]) + "\t\t" + str(output[7]) + "\t\t" + str(output[8]) + "\t\t" +"\n"

	text1 = Label(frame1, text=print_output, padx=10, pady=10)
	text1.grid(row=1,column=1)
	'''

	
	for output in outputs:
		print_output += str(output) + "\n"

	text1 = Label(frame1, text=print_output, padx=10, pady=10)
	text1.grid(row=1,column=1)

	conn.commit()

	conn.close()

	return

	# end show all

def showmarks():
	conn = sqlite3.connect(r'database/stud.db')

	c = conn.cursor()

	c.execute("SELECT * FROM 'sem1'")
	outputs = c.fetchall()
	print(outputs)

	#loop
	print_output = ''

	for output in outputs:
		print_output += str(output) + "\n"

	text2 = Label(frame1, text=print_output, padx=10, pady=10)
	text2.grid(row=2,column=1)



	conn.commit()

	conn.close()

	return


button1 = Button(root, text="Show All Student Info", width=100, command=showall)
button2 = Button(root, text="Student Marks", width=100, command=showmarks)

clicksem = StringVar()
clicksem.set("Sem1")

drop = OptionMenu(root, clicksem, "Sem1", "Sem2", "Sem3", "Sem4", "Sem5", "Sem6")


button1['font']=currFont
button2['font']=currFont

frame1 = LabelFrame(root, text="Details Here...")




button1.pack(pady=(5,10))
button2.pack(pady=(5,10))
drop.pack(pady=(5,10))
frame1.pack(fill="both", expand="yes")

root.mainloop()