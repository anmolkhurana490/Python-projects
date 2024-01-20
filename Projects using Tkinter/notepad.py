import tkinter as tk
from tkinter import messagebox as tmsg
from tkinter import filedialog as fd
from datetime import datetime
from tkinter import simpledialog as sd

size=7
defsize=7
filename=None
saved=None

root=tk.Tk()

root.title(f"Notepad")
root.geometry("600x400")
root.minsize(30,20)

class FontDialog(sd.Dialog):
	def body(self, master):
		self.title("Fonts")
		tk.Label(master, text="Font Family:").grid(row=0)
		tk.Label(master, text="Font Size:").grid(row=1)
		
		self.familyInput=tk.StringVar()
		self.sizeInput=tk.IntVar()
		self.boldInput=tk.IntVar()
		self.italicInput=tk.IntVar()
		self.underlineInput=tk.IntVar()
		
		self.entry_family=tk.Entry(master, textvariable=self.familyInput)
		self.entry_size=tk.Entry(master, textvariable=self.sizeInput)
		self.check_bold=tk.Checkbutton(master, text="Bold", variable=self.boldInput)
		self.check_italic=tk.Checkbutton(master, text="Italic", variable=self.italicInput)
		self.check_underline=tk.Checkbutton(master, text="Underline", variable=self.underlineInput)
		
		self.entry_family.grid(row=0, column=1)
		self.entry_size.grid(row=1, column=1)
		self.check_bold.grid(row=2)
		self.check_italic.grid(row=3)
		self.check_underline.grid(row=4)
		
	def apply(self):
		self.result=(self.familyInput.get(),
								self.sizeInput.get(),
								self.boldInput.get(),
								self.italicInput.get(),
								self.underlineInput.get()
							)
		
def newfile():
	global filename, saved
	clear()
	filename=None
	saved=None

def openfile():
	global filename, saved
	filename=fd.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	with open(filename, "r") as file:
		filetext=file.read()
		
	clear()
	text.insert(tk.END, filetext)
	root.title(f"Notepad - {filename}")
	saved=filetext
	
def save():
	global filename, saved
	if filename:
		filetext=text.get(1.0, tk.END)
		with open(filename, "w") as file:
			file.write(filetext)
		
		saved=filetext
	
def saveasfile():
	global filename, saved
	filename=fd.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	filetext=text.get(1.0, tk.END)
	with open(filename, "w") as file:
		file.write(filetext)
		
	root.title(f"Notepad - {filename}")
	saved=filetext
	
def exit():
	global filename, saved
	if filename and saved==text.get(1.0, tk.END):
		quit()
	elif filename:
		ans=tmsg.askyesnocancel("File not saved!", f"The file {filename} is not saved! Due to Save before Exit?")
		if ans==True:
			save()
			quit()
		elif ans==False:
			quit()
		else:
			return
	elif text.get(1.0, tk.END).strip():
		saveasfile()
	else:
		quit()
	
def cut():
	text.event_generate('<<Cut>>')
	
def copy():
	text.event_generate('<<Copy>>')
	
def paste():
	text.event_generate('<<Paste>>')
	
def undo():
	text.event_generate('<<Undo>>')
	
def redo():
	text.event_generate('<<Redo>>')
	
def select(start="1.0", end=tk.END):
	text.tag_add("sel", start, end)

def delete():
	text.event_generate('<BackSpace>')

def clear():
	text.delete(1.0, tk.END)

def timedate():
	dttext=datetime.now().strftime("%d-%m-%y %H:%M:%S")
	text.insert(tk.END, dttext)

def wordwrap():
	text.config(wrap=tk.WORD)

def unwrap():
	text.config(wrap=tk.NONE)

def fonts():
	global size
	fontbox=FontDialog(root)
	if not fontbox.result:
		return
	family, newsize, bold, italic, underline=fontbox.result
	font=family
	if size>0:
		font=font+" "+str(newsize)
	else:
		font+=f" {size}"
	if bold==1:
		font+=" bold"
	if italic==1:
		font+=" italic"
	if underline==1:
		font+=" underline"
	text.config(font=font)

def zoomin():
	global size
	size+=1
	text.configure(font=f"sans {size}")
	
def zoomout():
	global size
	size-=1
	text.configure(font=f"sans {size}")
	
def defaultzoom():
	global size, defsize
	size=defsize
	text.configure(font=f"sans {size}")
	
def help():
	tmsg.showinfo("Help", "Sure, I will help you!")
	
def about():
	tmsg.showinfo("About us", "I am Anmol and I have developed this \nNotepad using Tkinter module in Python. \nPlease support me for more Software\n Development.")

def currIndex():
	index=text.index(tk.CURRENT).split(".")
	return f"line {index[0]} char {index[1]}"

mainmenu=tk.Menu(root)

m1=tk.Menu(mainmenu)
m1.add_command(label="New", command=newfile)
m1.add_command(label="Open...", command=openfile)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save as", command=saveasfile)
m1.add_separator()
m1.add_command(label="Page Setup")
m1.add_command(label="Print")
m1.add_separator()
m1.add_command(label="Exit", command=exit)
mainmenu.add_cascade(label="File", menu=m1)

m2=tk.Menu(mainmenu)
m2.add_command(label="Undo", command=undo)
m2.add_command(label="Redo", command=redo)
m2.add_separator()
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Delete", command=delete)
m2.add_command(label="Clear", command=clear)
m2.add_separator()
m2.add_command(label="Find")
m2.add_command(label="Find Next")
m2.add_command(label="Replace")
m2.add_command(label="Go To...")
m2.add_separator()
m2.add_command(label="Select All", command=select)
m2.add_command(label="Date/Time", command=timedate)
mainmenu.add_cascade(label="Edit", menu=m2)

m3=tk.Menu(mainmenu)
m3.add_command(label="Word Wrap", command=wordwrap)
m3.add_command(label="Unwrap", command=unwrap)
m3.add_command(label="Font...", command=fonts)
mainmenu.add_cascade(label="Format", menu=m3)

m4=tk.Menu(mainmenu)

m4m1=tk.Menu(m4)
m4m1.add_command(label="Zoom In", command=zoomin)
m4m1.add_command(label="Zoom Out", command=zoomout)
m4m1.add_command(label="Restore Default Zoom", command=defaultzoom)
m4.add_cascade(label="Zoom", menu=m4m1)

m4.add_command(label="Status Bar")
mainmenu.add_cascade(label="View", menu=m4)

m5=tk.Menu(mainmenu)
m5.add_command(label="View Help", command=help)
m5.add_separator()
m5.add_command(label="About Us", command=about)
mainmenu.add_cascade(label="Help", menu=m5)

root.config(menu=mainmenu)

entryframe=tk.Frame(root)
entryframe.pack(fill=tk.BOTH, expand=True)

yscroll=tk.Scrollbar(entryframe)
yscroll.pack(side=tk.RIGHT, fill=tk.Y)


text=tk.Text(entryframe)
text.pack(fill=tk.BOTH, expand=True)
val=text.get(1.0, tk.END)

xscroll=tk.Scrollbar(entryframe, orient=tk.HORIZONTAL)
xscroll.pack(side=tk.BOTTOM, fill=tk.X)

yscroll.config(command=text.yview)
text.config(yscrollcommand=yscroll.set)
xscroll.config(command=text.xview)
text.config(xscrollcommand=xscroll.set)

footer=tk.Frame(root)
footer.pack(side=tk.BOTTOM, fill=tk.X)
l1=tk.Label(footer, text="Ready")
l1.pack(side=tk.LEFT, anchor="nw")
l2=tk.Label(footer, text=currIndex())
l2.pack(anchor="n")

root.mainloop()