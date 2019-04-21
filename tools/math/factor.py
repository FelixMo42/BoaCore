from Tool import Tool, Variable, Function, Alert
import math

def Main():
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
            if self.a and self.b != None and self.c != None:
                if self.b ** 2 - 4 * self.a * self.c < 0:
                    Alert("Does not support imaginary roots at this time! Sorry :(")
                    return

                sqrtpart = math.sqrt(self.b ** 2 - 4 * self.a * self.c)

                self.zero_1  = (-self.b - sqrtpart) / (2 * self.a)
                self.zero_2  = (-self.b + sqrtpart) / (2 * self.a)
            elif self.zero_1 and self.zero_2:
                self.a = 1
                self.b = self.zero_1 + self.zero_2
                self.c = self.zero_1 * self.zero_2

            self.equation = "{}x² + {}x + {}".format("" if self.a == 1.0 else self.a, self.b, self.c)
            
            asqrt = math.sqrt(self.a)
            xchar =  str("" if asqrt == 1.0 else asqrt) + "x"

            full = ""

            if self.zero_1 == 0:
                full += xchar
            if self.zero_1 < 0:
                full += "({} + {})".format(xchar, abs(self.zero_1))
            if self.zero_1 > 0:
                full += "({} - {})".format(xchar, abs(self.zero_1))

            if self.zero_2 == 0:
                full += xchar
            if self.zero_2 < 0:
                full += "({} + {})".format(xchar, abs(self.zero_2))
            if self.zero_2 > 0:
                full += "({} - {})".format(xchar, abs(self.zero_2))

            self.factored_equation = full

    return Main()