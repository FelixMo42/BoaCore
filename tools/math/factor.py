from Tool import Tool, Variable, Function
import math

class Main(Tool):
    a = Variable("number")
    b = Variable("number")
    c = Variable("number")

    zero_1 = Variable("number")
    zero_2 = Variable("number")

    equation = Variable("string")
    factored_equation = Variable("string")

    @Function
    def factor(self):
        sqrtpart = math.sqrt(self.b ** 2 - 4 * self.a * self.c)

        self.zero_1  = (-self.b - sqrtpart) / (2 * self.a)
        self.zero_2  = (-self.b + sqrtpart) / (2 * self.a)

        self.equation = "{}x² + {}x + {}".format(self.a == 1 and "" or self.a, self.b, self.c)
        
        asqrt = math.sqrt(self.a)
        xchar =  str(asqrt == 1.0 and "" or asqrt) + "x"

        full = ""

        if self.zero_1 == 0:
            full += xchar
        if self.zero_1 < 0:
            full += "({} + {})".format(xchar, -self.zero_1)
        if self.zero_1 > 0:
            full += "({} - {})".format(xchar, -self.zero_1)

        if self.zero_2 == 0:
            full += xchar
        if self.zero_2 < 0:
            full += "({} + {})".format(xchar, -self.zero_2)
        if self.zero_2 > 0:
            full += "({} - {})".format(xchar, -self.zero_2)

        self.factored_equation = full
