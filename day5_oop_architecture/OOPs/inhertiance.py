class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print(self):
        print(self.a,self.b)
class sub(add):
    def sum(self):
        print(self.a + self.b)
obj = sub(5, 10)
obj.print()
obj.sum()