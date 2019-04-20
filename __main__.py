import tkinter as tk
import pydoc
import os

class BaseApp():
	def __init__(self):
		self.root = tk.Tk()
		self.frame = tk.Frame(self.root)
		self.frame.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		self.frame.pack(pady=10, padx=10)

		i = 1
		for module in os.listdir("tools"):
			tk.Button(self.frame, text=module, command=self.setModule(module)).grid(row=i, column=0)
			i += 1

		self.root.mainloop()

	def clearModule(self):
		for element in self.frame.grid_slaves():
			if int(element.grid_info()["column"]) > 0:
				element.grid_forget()

	def setModule(self, module):
		def callback():
			self.clearModule()
			self.module = module
			i = 1
			for file in os.listdir("tools/" + module):
				if file == "__pycache__":
					continue
				tool = file.replace(".py", "")
				tk.Button(self.frame, text=tool, command=self.run(tool)).grid(row=i, column=1)
				i += 1

		return callback

	def run(self, tool):
		return lambda: pydoc.locate("tools.{}.{}.Main".format(self.module, tool))()

if __name__ == "__main__":
	baseapp = BaseApp()