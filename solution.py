class Calculator:
    def __init__(self):
        self.operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }