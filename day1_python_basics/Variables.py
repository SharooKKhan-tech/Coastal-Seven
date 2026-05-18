## Variables
## -->Variables are containers for storing data values. 
## Creating variables
## -->A variable is created the moment you first assign a value to it.

x = 5
y = "Hello, World!"
print(x)
print(y)
## Variable names can only contain letters, numbers and underscores.
## -->Variables must start with a letter or the underscore character.               
## -->Variable names are case-sensitive.
## Assigning Multiple Values
## -->Python allows you to assign values to multiple variables in one line:
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
#Casting
## -->If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'       
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
#Get the Type
## -->You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))
print(type(z))
