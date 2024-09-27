class Calculation:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.operation = op

    def get_res(self):
        return self.operation(self.a, self.b)