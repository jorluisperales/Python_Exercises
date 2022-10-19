#Arithmetic Operators
x = 2
y = 7

total = x + y #
print(total)

total = x - y #
print(total)

total = x * y #Multiplication
print(total)

total = x / y # Division
print(total)

total = y % x #Remanent
print(total)

total = y**x # Exponential / to the power
print(total)

# Comparison Operators

a = 30
b = 50

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b) #Equal
print(out)

out = (a != b) # Not Equal
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)

# Assigment Operators

c = 0
d = 1

c+=d # c = c+d 
print(c) #value of c is now 1

b = 0
e = 1

b-=e
print(b)


# Logical Operators

# and
# or

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y) # True because the first one is True
print(out)

out = (a > b) or (x < y)
print(out)

out = (a > b) or (x > y)
print(out)

out = (a > b) and (x < y) # for AND, all have to be True, if not, it will be False
print(out)

out = (a < b) and (x < y) # for AND, all have to be True, if not, it will be False
print(out)

out = not(x < y) # adding not will change the value negating the value
print(out)

# Membership Operator

first_tuple = ("ITO", "DevOps", 47, 89, 1.5)

ans = "DevOps" in first_tuple # check if it finds DevOps in the tuple
print(ans)

ans = "DevOps" not in first_tuple # Negates the existance of DevOps in the tuple
print(ans)

ans = 47 in first_tuple
print(ans)

ans = 67 not in first_tuple
print(ans)

# Identity Operators

a = 12
b = 15

results = a is b
print (results)

results = a is not b
print (results)