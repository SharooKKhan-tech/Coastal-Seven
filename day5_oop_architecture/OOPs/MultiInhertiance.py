class father:
    def __init__(self, fname):
        self.fname = fname

    def displayFather(self):
        print("father name is ", self.fname)
class mother:
    def __init__(self, mname):
        self.mname = mname

    def displayMother(self):
        print("mother name is ", self.mname)
class child(father, mother):
    def __init__(self, fname, mname):
        father.__init__(self, fname)
        mother.__init__(self, mname)

obj = child("Raju", "Sita")
obj.displayFather()
obj.displayMother()