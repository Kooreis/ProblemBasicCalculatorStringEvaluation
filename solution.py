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