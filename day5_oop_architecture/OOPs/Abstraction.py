from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

class SBIATM(ATM):

    def withdraw(self):
        print("Cash withdrawn")

s = SBIATM()
s.withdraw()