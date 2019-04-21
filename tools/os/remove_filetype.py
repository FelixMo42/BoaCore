from Tool import Tool, Variable, Function
import glob
import os

class Main(Tool):
    filetype = Variable("string")
    root_directory = Variable("directory")

    @Function
    def clear(self):
        for filename in glob.iglob('{}/**/*.{}'.format(self.root_directory, self.filetype), recursive=True):
            os.remove(filename)
