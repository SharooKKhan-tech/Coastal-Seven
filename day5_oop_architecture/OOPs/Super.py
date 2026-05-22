class College:
    def __init__(self, name):
        self.name = name
    def printCollege(self):
        print("College Name:", self.name)     
class Student(College):
    def __init__(self, name, location, ):
        super().__init__(name)
        self.location = location
    def printLocation(self):
        print("Location:", self.location)
obj = Student("VVIT", "Guntur")
obj.printCollege()
obj.printLocation()