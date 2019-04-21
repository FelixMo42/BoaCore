import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import types
import math

i = 0
def id():
	global i
	i += 1
	return i

class Variable():
	def __init__(self, t = "string"):
		self.type = t
		self.i = id()

	def setUp(self, tool, name):
		self.name = name

		self.value = tk.StringVar()

		label = tk.LabelFrame(tool.frame, text=name.replace("_"," "))
		label.grid(row=self.i, column=0)
		entry = tk.Entry(label, textvariable=self.value, width=25)
		entry.pack(padx=2, pady=2)

	def get(self):
		value = self.value.get()

		if value == "":
			return None

		if self.type == "number":
			return float(value)

		return value

	def set(self, value):
		return self.value.set(value)

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
		self.root.title(self.title)
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
				delattr(self.__class__, key)

			if hasattr(value, "ui_func"):
				self.i += 1
				tk.Button(self.frame, text=key, command=value).grid(row=getattr(value, "ui_func"), column=0)

		self.root.mainloop()

	def __getattr__(self, name):
		if name in self.variables.keys():
			return self.variables[name].get()
		else:
			return self.__dict__[name]

	def __setattr__(self, name, value):
		if name in self.variables.keys():
			self.variables[name].set(value)
		else:
			self.__dict__[name] = value