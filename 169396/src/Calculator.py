class Calculator:

    def add(self,a,b):
        return a+b

    def substract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b == 0:
            raise ZeroDivisionError
        return a/b







