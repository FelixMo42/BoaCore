import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import types

i = 0
def id():
	global i
	i += 1
	return i

class Variable():
	i = id()

	def setUp(self, tool, name):
		self.name = name

		label = tk.LabelFrame(tool.frame, text=name.replace("_"," "))
		label.grid(row=self.i, column=0)
		entry = tk.Entry(label, width=25)
		entry.pack(padx=2, pady=2)

def Function(func):
	setattr(func, "ui_func", id())

	return func

class Alert():
	pass

class Tool():
	title = "default title"
	variables = {}
	i = 0

	root = 3
	frame = None

	def __init__(self):	

		# setup ui frame
		self.root = tk.Toplevel()
		self.frame = tk.Frame(self.root)
		self.frame.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		self.frame.pack(pady=10, padx=10)

		# setup variables
		for key in dir(self):
			value = getattr(self, key)
			if isinstance(value, Variable):
				self.variables[key] = value
				self.variables[key].setUp(self, key)

			if hasattr(value, "ui_func"):
				self.i += 1
				tk.Button(self.frame, text=key, command=value).grid(row=getattr(value, "ui_func"), column=0)

		self.root.mainloop()

	def __getattr__(self, name):
		return self.__dict__[name]

	def __setattr__(self, name, value):

		self.__dict__[name] = value