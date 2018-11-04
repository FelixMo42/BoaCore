from tkinter import *
from tools.RSA import RSA

class App():
	def __init__(self, tools):
		self.window = Tk()
		self.window.title("CTF Sleuth")

		self.frame = Frame(self.window)
		self.frame.grid(column=0, row=0, sticky=(N,W,E,S))
		self.frame.columnconfigure(0, weight=1)
		self.frame.rowconfigure(0, weight=1)
		self.frame.pack(pady=10, padx=10)

		Label(self.frame, text=" ~ tools ~ ").grid(row=0, column=0)

		i = 1
		for tool in tools:
			Button(self.frame, text=tool.title, command=self.runer(tool)).grid(row=i, column=0)
			i += 1

		self.window.mainloop()

	def runer(self, tool):
		return lambda: tool()

if __name__ == "__main__":
	App([RSA])