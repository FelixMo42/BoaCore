from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

i = 0

def Alert(val):
	messagebox.showwarning("problem", val)
	raise Exception(val)

class Var():
	def __init__(self, type="string"):
		global i
		self.i = i
		i += 1

		self.type = type

	def cheak(self):
		if self.entry.get() == "":
			return setattr(self.tool,self.name,None)

		if self.type == "string" or self.type == "s":
			setattr(self.tool,self.name,self.entry.get())
		if self.type == "number" or self.type == "n":
			setattr(self.tool,self.name,float(self.entry.get()))

class Tool():
	title = "page"
	var = []

	def __init__(self):
		self.window = Tk()
		self.window.title(self.title)
		
		self.frame = Frame(self.window)
		self.frame.grid(column=0, row=0, sticky=(N,W,E,S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		self.frame.pack(pady=10, padx=10)

		for key in dir(self):
			if isinstance(getattr(self,key), Var):
				self.var.append(getattr(self,key))
				self.addVar(key, getattr(self,key), i)

		Button(self.window, text="GO", command=self.pack).pack(padx=2, pady=2)

		self.window.mainloop()

	def pack(self):
		for var in self.var:
			var.cheak()

		val = self.main()
		messagebox.showinfo("Results", val)


	def addVar(self, key, var, i):
		label = LabelFrame(self.frame, text=" " + key.replace("_"," ") + " ")
		label.grid(row=var.i, column=0)
		entry = Entry(label, width=25)
		entry.pack(padx=2, pady=2)

		var.tool = self
		var.name = key
		var.entry = entry