# For loop, follows a sequence

PLANET = "Earth"

for i in PLANET:
    print("Value of i is now ",i)

print("Rest of the code.")


dogs_breeds = ("Bulldog", "Golden", "Chihuahua", "Doberman", "Boxer") # Tuple with dog breeds

for dogs in dogs_breeds:
    print(f"{dogs} is a dog breed")

print("Rest of the code.")

dogs_breeds = ["Bulldog", "Golden", "Chihuahua", "Doberman", "Boxer"] # List with dog breeds

for dogs in dogs_breeds:
    print(f"{dogs} is a dog breed")

print("Rest of the code.")


# While loop, looks for conditions

x = 0

while (x <= 10):
    print("Value of X is:", x)
    print("Looping")
    x += 1
    # also works x = x+1

print("Rest of the code.")

