str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers
num1 = 123
flt1 = 2.0

#List / Collection of multi datatype, enclosed in square brackets (Mutable) []

first_list = [str1, "DevOps", 47, num1, 1.5]

print(first_list)

#Tuples / Collection of multi datatype, enclosed in roud bracket (inmutable) ()

first_tuple = (str1, "DevOps", 47, num1, 1.5)

print(first_tuple)

# Dictionary / Elements in the dictionary are always in pairs (Key:Value, curly brackets.)

first_dictionary = {"Name":"JP", "Age":30, "Hobbies":["Dancing, Gaming, learning"]}

print(first_dictionary)

print("Variable first_list is a:",type(first_list))
print("Variable first_tuple is a:", type(first_tuple))
print("Variable first_dictionary is a:",type(first_dictionary))

# Boolean

x = True
y = False

#printing boolean
print(x)
print(y)

print(type(x))
print(type(y))