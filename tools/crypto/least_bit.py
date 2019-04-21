from Tool import Tool, Variable, Function
import os
import re

class Main(Tool):
    file = Variable("file")
    match = Variable("string")
    output = Variable("string")

    @Function
    def search(self):
        for i in range(16):
            with open(self.file, "rb") as file:
                data = file.read()
                data = data[i:]

                bits = ""
                for c in data:
                    lsb = str(c & 0x1)
                    bits += lsb

                bytess = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
                lsbstr = "".join(bytess)


                match = re.search(self.match, lsbstr)
                if match:
                    self.output = match.group(0)