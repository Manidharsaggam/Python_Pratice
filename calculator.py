'''Calculator function using OOPs'''
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed."

num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

calc = Calculator(num1, num2)

print(f"Addition: {calc.add()}")
print(f"Subtraction: {calc.subtract()}")
print(f"Multiplication: {calc.multiply()}")
print(f"Division: {calc.divide()}")
