from Tool import Tool, Variable, Function

class Main(Tool):
    events = Variable("equation")
    total = Variable("equation")
    probability = Variable("number")

    @Function
    def calc(self):
        self.probability = self.events / self.total