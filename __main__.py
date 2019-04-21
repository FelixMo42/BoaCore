import tkinter as tk
import pydoc
import os

class BaseApp():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("BoaCore")
		self.frame = tk.Frame(self.root)
		self.frame.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		self.frame.pack(pady=10, padx=10)

		i = 1
		for module in os.listdir("tools"):
			tk.Button(
				self.frame,
				text=module,
				command=self.setModule(module, i),
				width=10
			).grid(row=i, column=0)
			if module == "core":
				self.setModule(module, i)()
			i += 1

		tk.Label(self.frame, text="modules").grid(row=0, column=0)
		tk.Label(self.frame, text="tools").grid(row=0, column=2)
	
		self.root.mainloop()

	def clearModule(self):
		for element in self.frame.grid_slaves():
			if int(element.grid_info()["column"]) > 0 and int(element.grid_info()["row"]) > 0:
				element.grid_forget()

	def setModule(self, module, pos):
		def callback():
			self.clearModule()
			self.module = module
			tk.Label(self.frame, text=">").grid(row=pos, column=1)
			i = 1
			for file in os.listdir("tools/" + module):
				if file == "__pycache__":
					continue
				tool = file.replace(".py", "")
				tk.Button(
					self.frame,
					text=tool.replace("_", " "),
					command=self.run(tool),
					width=10
				).grid(row=i, column=2)
				i += 1

		return callback

	def run(self, tool):
		return lambda: pydoc.locate("tools.{}.{}.Main".format(self.module, tool))()

if __name__ == "__main__":
	baseapp = BaseApp()