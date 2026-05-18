int  = int(input("enter a number: "))
fact = 1
for i in range(1, int + 1):
    fact *= i   
print("The factorial of", int, "is", fact)