from tkinter import *
import sqlite3

root = Tk()

#create conn and db
conn = sqlite3.connect(r'database/stud.db')

c = conn.cursor()

conn.commit()

conn.close()


root.mainloop()