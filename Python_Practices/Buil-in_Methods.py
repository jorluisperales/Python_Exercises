# String Build in Methods/Functions

message = "dog breeds are very important when it comes to choosing a dog"
print(message)
print(message.capitalize()) # String a inmutable, you'll have to store it into a new variable
Message = message.capitalize()
print(Message)

# dir() function, it will print all of the available funtions for the datatype
print(dir(message))
print(dir([]))
print(dir({}))

print(message.upper()) # All values of the string are changed to uppercase
print(message.islower()) # useful for data validation, to check if someone used the specific value.
print(message.isupper())

print(message.find("comes")) # check if it exists and returns the index where is stored
print(message[38:43])
print(message.find("cat")) # it prints a -1 if it does not find the expected value

seq1 = ("192", "168", "0", "1")
print(".".join(seq1)) # Joins each value with . (dots)

mountains = ["Everest", "Himalaya", "Alps", "k2"]
print(mountains)

mountains.append("Oregon Mount")
print(mountains)

mountains.extend(["Mt Raininer", "Satpuda"]) # extends the existing list adding new values
print(mountains)

mountains.insert(2, "Mt Abu") # this inserted the value in the 2 index
print(mountains)

mountains.pop(5) # will remove the value in the 5 index
print(mountains) # will remote Oregon mount which is the one in the 5 index

cntr_emp1 = {"Name":"Santa", "Skill": "Blockchain", "Code":1024}
print(cntr_emp1.keys()) # Prints only the keys
print(cntr_emp1.values()) # Prints only the values

cntr_emp1.clear() # removes the content from the dictionary
print(cntr_emp1)


