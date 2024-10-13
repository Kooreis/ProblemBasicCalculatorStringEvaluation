Here is a Python console application that implements a basic calculator to evaluate a string with +, -, *, / and parentheses.

```python
class Calculator:
    def __init__(self):
        self.operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def calculate(self, expression):
        stack = []
        number = ''
        for char in expression:
            if char in '0123456789.':
                number += char
            elif char in self.operators:
                if number:
                    stack.append(float(number))
                    number = ''
                while (stack and stack[-1] in self.operators and
                       self.precedence(char) <= self.precedence(stack[-1])):
                    self.compute(stack)
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                if number:
                    stack.append(float(number))
                    number = ''
                while stack[-1] != '(':
                    self.compute(stack)
                stack.pop()
        if number:
            stack.append(float(number))
        while len(stack) != 1:
            self.compute(stack)
        return stack[0]

    def compute(self, stack):
        num2 = stack.pop()
        op = stack.pop()
        num1 = stack.pop()
        stack.append(self.operators[op](num1, num2))

    def precedence(self, operator):
        if operator in '+-':
            return 1
        if operator in '*/':
            return 2
        return 0

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


if __name__ == "__main__":
    calculator = Calculator()
    while True:
        expression = input("Enter an expression to calculate (or 'q' to quit): ")
        if expression.lower() == 'q':
            break
        print(calculator.calculate(expression))
```

This console application will continuously prompt the user to enter an expression to calculate until the user enters 'q' to quit. The calculator can handle +, -, *, /, and parentheses. It also handles operator precedence and parentheses correctly.