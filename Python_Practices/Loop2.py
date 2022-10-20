dogs_breeds = ["Bulldog", "Golden", "Chihuahua", "Doberman", "Boxer"] # List with dog breeds

for dogs in dogs_breeds:
    print("")
    print("I would like to get a ")
    for i in dogs: # Nested loop, will print the name of the dog breeds verticaly
        print(i)



# This is an example of infinite loops

x = 2
import time #importing the module time
while (True):
    print("Value of X is:", x)
    print("Looping")
    x *= 2
    time.sleep(1) # wait for two seconds before performing the task again