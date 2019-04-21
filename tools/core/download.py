from Tool import Alert
import tkinter as tk
import requests
import json

class Main():
    def __init__(self):
        # setup ui frame
        self.root = tk.Toplevel()
        self.root.title("Download")
        self.frame = tk.Frame(self.root)
        self.frame.grid(column=0, row=0, sticky=(tk.N,tk.W,tk.E,tk.S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.pack(pady=10, padx=10)

        response = requests.get("https://boa-core.herokuapp.com/api/users")

        if response.ok:
            data = json.loads(response.content.decode("utf-8"))

            i = 0
            for user in data:
                i += 1
                tk.Button(
                    self.frame,
                    text=user,
                    command=self.setUser(user, i),
                    width=10
                ).grid(row=i, column=0)

                if user == "core":
                    self.setUser(user, i)()

            tk.Label(self.frame, text="module / user").grid(row=0, column=0)
            tk.Label(self.frame, text="tools").grid(row=0, column=2)
        else:
            Alert("conection to server failed!")

    def clear(self):
        for element in self.frame.grid_slaves():
            if int(element.grid_info()["column"]) > 0 and int(element.grid_info()["row"]) > 0:
                element.grid_forget()

    def setUser(self, user, pos):
        def setIt():
            self.clear()
            self.user = user
            tk.Label(self.frame, text=">").grid(row=pos, column=1)

            response = requests.get("https://boa-core.herokuapp.com/api/user/" + user)
            data = json.loads(response.content.decode("utf-8"))

            i = 0
            for tool in data:
                tool = tool.replace(".py", "")
                i += 1
                tk.Button(
                    self.frame,
                    text=tool,
                    command=self.downloadTool(user, tool),
                    width=10
                ).grid(row=i, column=2)

        return setIt

    def downloadTool(self, user, tool):
        def downloadIt():
            response = requests.get("https://boa-core.herokuapp.com/api/file/{}/{}".format(user, tool))

            with open("tools/{}/{}.py".format(user, tool), "w") as file:
                file.write(response.content.decode("utf-8"))

        return downloadIt