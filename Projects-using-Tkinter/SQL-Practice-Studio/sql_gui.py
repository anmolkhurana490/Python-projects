import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as tmsg
from sql_backend import create_conn, run_input_queries, get_database_schema, close_conn

connected_db=None
original_db="data.db"
results=None

def run_all_queries(app):
	#tmsg.showwarning("Warning!", "running queries")
	inputVal=app.textInput.get(1.0, tk.END)
	app.clearResults()
	if connected_db:
		global results
		results=run_input_queries(app.conn, inputVal)
		if results:
			app.show_results(results)
		else:
			app.outputLabel.configure(text="Query Executed Successfully, but Result is Empty.")
		
	else:
		app.outputLabel.configure(text="No Database Connection Found!")
	

def connect_database(app):
	db=app.dbpath.get()
	app.statusBar.configure(text="Connecting...")
	
	global connected_db
	if connected_db:
		close_conn(app.conn)
	app.conn=create_conn(db)
	
	connected_db=db
	app.statusBar.configure(text=f"CONNECTED - {connected_db}")

		
class SQL_GUI(tk.Tk):
	def __init__(self, title):
		super().__init__()
		self.title(title)
		self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
		
	def create_submenu(self, menu, sublist):
		for submenu in sublist:
			if type(submenu)==tuple:
				menu.add_command(label=submenu[0], command=submenu[1])
			elif type(submenu)==dict:
				sub=tk.Menu(menu)
				self.create_submenu(menu, sublist)
				# menu.add_cascade(label=label, menu=sub)
				menu.add_cascade(label=submenu, menu=sub)

	def create_menu(self, menus):
		self.mainMenu=tk.Menu(self)
		
		for label, sublist in menus.items():
			m1=tk.Menu(self.mainMenu)
			self.create_submenu(m1, sublist)
			self.mainMenu.add_cascade(label=label, menu=m1)
		
		self.config(menu=self.mainMenu)
	
	def create_connection_view(self):
		self.connectFrame=tk.Frame(self, borderwidth=3, relief=tk.SUNKEN)
		self.connectFrame.pack(fill=tk.BOTH)
		
		self.connectLabel=tk.Label(self.connectFrame, text="Database Connection")
		self.connectLabel.pack(anchor="nw")
		
		self.connectLabel=tk.Label(self.connectFrame, text="Database Path:")
		self.connectLabel.pack(side=tk.LEFT)
		
		self.dbpath=tk.StringVar()
		self.dbpath.set(original_db)
		self.dbInput=tk.Entry(self.connectFrame, textvariable=self.dbpath)
		self.dbInput.pack(side=tk.LEFT, fill=tk.X)
		
		self.runButton=tk.Button(self.connectFrame, fg="white", bg="blue", text="Connect", command=lambda: connect_database(app))
		self.runButton.pack(side=tk.LEFT)
	
	def create_editor(self):
		self.editorFrame=tk.Frame(self, borderwidth=3, relief=tk.SUNKEN)
		self.editorFrame.pack(fill=tk.X)
		
		self.label_button_frame=tk.Frame(self.editorFrame)
		self.label_button_frame.pack(fill=tk.X)
		
		self.editorLabel=tk.Label(self.label_button_frame, text="Query Editor")
		self.editorLabel.pack(side=tk.LEFT)
		
		self.runButton=tk.Button(self.label_button_frame, fg="white", bg="blue", text="Run Query", command=lambda: run_all_queries(self))
		self.runButton.pack(side=tk.RIGHT)
		
		self.editor_scrollbar=tk.Scrollbar(self.editorFrame, width=20)
		self.editor_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		
		self.textInput=tk.Text(self.editorFrame)
		self.textInput.pack(fill=tk.BOTH, expand=True)
		self.textInput.insert(tk.END, "--Enter Your Queries Here--\n")
		
		self.textInput.config(yscrollcommand=self.editor_scrollbar.set)
		self.editor_scrollbar.config(command=self.textInput.yview)
		
	
	def create_result_section(self):
		self.resultFrame=tk.Frame(self, borderwidth=3, relief=tk.SUNKEN)
		self.resultFrame.pack(fill=tk.BOTH, expand=True)
		
		self.resultLabel=tk.Label(self.resultFrame, text="Result Viewer")
		self.resultLabel.pack(anchor="nw")
		
		self.outputFrame=ctk.CTkScrollableFrame(self.resultFrame)
		self.outputFrame.pack(fill=tk.BOTH, expand=True)
		
		self.outputLabel=tk.Label(self.outputFrame, bg="white", text="Result is Empty", wraplength=750)
		self.outputLabel.pack(anchor="nw", fill=tk.X)
		
	def create_table(self, data):
		self.tableFrame=tk.Frame(self.outputFrame)
		self.tableFrame.pack(fill=tk.BOTH, expand=True, padx=10, pady=20)
		
		self.table=ttk.Treeview(self.tableFrame, height=len(data["data"]))
		#self.style.configure('Treeview', rowheight=40)
		
		self.table_yscroll=tk.Scrollbar(self.tableFrame, orient="vertical", width=20, command=self.table.yview)
		self.table_xscroll=tk.Scrollbar(self.tableFrame, orient="horizontal", width=20, command=self.table.xview)
		
		self.table_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
		self.table.pack(anchor="nw", fill=tk.BOTH)
		self.table_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
		
		self.table.configure(yscrollcommand=self.table_yscroll.set, xscrollcommand=self.table_xscroll.set)
		
		self.table["columns"]=tuple(data["column_names"])
		self.table.column("#0", width=0, stretch=tk.NO)
		for i,col_name in enumerate(data["column_names"]):
			self.table.column(col_name, stretch=True)
			self.table.heading(col_name, text=col_name)
		
			
		for i,row in enumerate(data["data"]):
			if i%2==0:
				self.table.insert(parent='', index='end', iid=i, values=row, tags=("oddrow",))
			else:
				self.table.insert(parent='', index='end', iid=i, values=row, tags=("evenrow",))
		
		self.table.tag_configure('evenrow', background="lightgray")
		
		for col in data["column_names"]:
			col_data=self.table.column(col)
			#width=len(max(col_data, key=len))
			self.table.column(col, width=col_data["width"]-30)
	
	def show_results(self, results):
		for result in results:
			self.outputLabel.configure(text="Query Executed Successfully!")
			
			if "error" in result:
				self.outputLabel.configure(text=f"Error: {result['error']}")
			else:
				self.create_table(result)
		
		app.outputLabel=tk.Label(self.outputFrame, bg="white", wraplength=750)
		app.outputLabel.pack(anchor="nw", fill=tk.X, padx=10, pady=20)
	
	def create_footer(self):
		self.footer=tk.Frame(self, borderwidth=3, relief=tk.SUNKEN)
		self.footer.pack(side=tk.BOTTOM, fill=tk.X)
		
		self.statusBar=tk.Label(self.footer, text=f"DISCONNECTED")
		self.statusBar.pack(anchor="sw")
	
	def show_schema(self):
		self.schema_frame=tk.Frame(self, borderwidth=3, relief=tk.SUNKEN)
		self.schema_frame.pack(fill=tk.BOTH, expand=True)
		
		self.style=ttk.Style()
		self.schema_tree=ttk.Treeview(self.schema_frame)
		self.style.configure('Treeview', rowheight=40)
		
		self.schema_vsb=tk.Scrollbar(self.schema_frame, orient="vertical", command=self.schema_tree.yview)
		self.schema_hsb=tk.Scrollbar(self.schema_frame, orient="horizontal", command=self.schema_tree.xview)
		self.schema_tree.configure(yscrollcommand=self.schema_vsb.set, xscrollcommand=self.schema_hsb.set)
		
		self.schema_vsb.pack(side=tk.RIGHT, fill=tk.Y)
		self.schema_tree.pack(fill=tk.BOTH, expand=True)
		self.schema_hsb.pack(side=tk.BOTTOM, fill=tk.X)
		
		if connected_db:
			tables=get_database_schema(self.conn)
			self.schema_tree.heading("#0", text="Database Schema", anchor="nw")
			for i, (table, table_schema) in enumerate(tables.items()):
				self.schema_tree.column("#0")
				self.schema_tree.insert(parent='', index='end', iid=i, text=table, tags=("table_name",))
				
				for attribute in table_schema:
					attribute_name=f"{attribute[1]} "
					attribute_info=f"[{attribute[2]}] {'[PRIMARY KEY]' if attribute[5] else ''}"
					
					self.schema_tree.insert(parent=i, index='end', text=f"{attribute_name} {attribute_info}")
			
			#self.schema_tree.tag_configure("table_name", font=("Arial", 10, "bold"))
			
	def new_query(self):
		self.clear()
		self.textInput.insert(tk.END, "--Enter Your Queries Here--\n")
	
	def open_query(self):
		filename=fd.askopenfilename(filetypes=[("SQL files", "*.sql"), ("All files", "*.*")])
		with open(filename, 'r') as file:
			query=file.read()
		
		self.clear()
		self.textInput.insert(tk.END, query)
	
	def save_query(self):
		filename=fd.asksaveasfilename(initialfile="Untitled.sql", filetypes=[("SQL files", "*.sql"), ("All files", "*.*")])
		query=self.textInput.get(1.0, tk.END)
		with open(filename, 'w') as file:
			file.write(query)
	
	def export_result(self):
		if results:
			filename=fd.asksaveasfilename(initialfile="Untitled.txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
			with open(filename, 'w') as file:
				file.write(str(results))
	
	def exit(self):
		if connected_db:
			close_conn(self.conn)
		quit()
	
	def cut(self):
		self.textInput.event_generate("<<Cut>>")
	
	def copy(self):
		self.textInput.event_generate("<<Copy>>")
	
	def paste(self):
		self.textInput.event_generate("<<Paste>>")
	
	def delete(self):
		self.textInput.event_generate("<BackSpace>")
	
	def clear(self):
		self.textInput.delete(1.0, tk.END)
	
	def find(self):
		pass
	
	def selectAll(self):
		self.textInput.tag_add("sel", 1.0, tk.END)
	
	def clearResults(self):
		for widget in self.outputFrame.winfo_children():
			widget.destroy()
		
		app.outputLabel=tk.Label(app.outputFrame, bg="white", text="Result is Empty", wraplength=750)
		app.outputLabel.pack(anchor="nw", fill=tk.X)
	
	def db_schema(self):
		if connected_db:
			self.schema_frame.destroy()
			self.editorFrame.pack_forget()
			self.resultFrame.pack_forget()
			self.show_schema()
		else:
			tmsg.showerror("Error", "No Database Connection Found!\n Please Connect to Database to\n view schema")
	
	
	def queryEditor(self):
		self.schema_frame.pack_forget()
		self.resultFrame.pack_forget()
		self.editorFrame.pack(fill=tk.X)
		self.resultFrame.pack(fill=tk.BOTH, expand=True)
	
	def resultViewer(self):
		self.schema_frame.pack_forget()
		self.editorFrame.pack_forget()
	
	def about(self):
		tmsg.showinfo("About Us", "I am Anmol and I have developed this \nSQL Interface using Tkinter module in \nPython. Please support me for more \nSoftware Development.")
	
	def contact(self):
		tmsg.showinfo("Contact Us", "Contact details")
	

if __name__=="__main__":
	app=SQL_GUI('SQL Practice Studio: Interactive Querying for Beginners')
	
	#Menu Bar
	menus={
		"File": [
			("New Query", app.new_query),
			("Open Query", app.open_query),
			("Save Query", app.save_query),
			("Export Results", app.export_result),
			("Exit", app.exit)
		],
		"Edit": [
			("Cut", app.cut),
			("Copy", app.copy),
			("Paste", app.paste),
			("Delete", app.delete),
			("Clear", app.clear),
			("Find", app.find),
			("Select All", app.selectAll),
			("Clear Results", app.clearResults)
		],
		"View": [
			("Database Schema", app.db_schema),
			("Query Editor", app.queryEditor),
			("Result Viewer", app.resultViewer)
		],
		"Help": [
			("About Us", app.about),
			("Contact Us", app.contact)
		]
	}
	
	app.create_menu(menus)
	
	#Database Connection
	app.create_connection_view()
	
	#Query Editor frame
	app.create_editor()
	
	#Result Viewer frame
	app.create_result_section()
	
	#Database Schema
	app.show_schema()
	app.schema_frame.pack_forget()
	
	#Status Bar
	app.create_footer()
	
	app.mainloop()
	# close_conn(app.conn)