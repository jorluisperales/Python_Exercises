# Defining Fuction

##### Example 1

def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add (2, 3)
print(out)
print(add(10,30)) #Printing directly


##### Example 2

def adder(arg1, arg2): # two arguments
    total = arg1 + arg2
    print(total)

adder(10, 50)
print(adder(10 ,50))


##### Example 3
# this is an example of a sum taking the multipole values within the argumment

def sum (arg):
    x = 0
    for i in arg:
        x +=i
    return x

out = sum([10, 20, 30])
print(out)

##### Example 4

def greetings(MSG):
    print (f"Good {MSG}")
    print(f"Welcome to the function.")

greetings("Morning")

##### Example 5

def greetings(MSG="Morning"): #ARG is giving a value 
    print (f"Good {MSG}")
    print(f"Welcome to the function.")

greetings()
greetings("Evening")

##### Example 6

def dogs(breed, size):
    print(f" A {breed} has the following size {size}.")
    if (size > 20) and (size < 50):
        print("This is a small size dog")
    elif (size >= 50) and (size <=90):
        print("This is a medium size dog")
    elif (size > 100):
        print("This is a large size dog")

dogs("Bulldog", 50)

# Orders are important, if we don't care about the order, we can define the arguments
# Example:

dogs(size=120, breed="Golden")