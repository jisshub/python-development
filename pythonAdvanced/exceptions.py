# import math

import math


class Calculator:
    def __init__(self, n1, n2):
        self.n = n1
        self.p = n2
        print(self.n, self.p)

    def check_parameters(self):
        try:
            if self.n < 0 or self.p < 0:
                # raise a custom exception
                raise Exception
            else:
                return math.pow(self.n, self.p)
        except Exception:
            print("should use non-negative numbers")


try:
    # if no exception, object is instantiated and function is invoked
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))
    c1 = Calculator(num1, num2)
    print(c1.check_parameters())
except Exception:
    print("wrong type")


