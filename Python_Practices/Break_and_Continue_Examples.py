import random
dogs_breeds = ["Bulldog", "Golden", "Chihuahua", "Doberman", "Boxer"] # list with dog breeds

random.shuffle(dogs_breeds)
print(dogs_breeds)

doggie = random.choice(dogs_breeds)
print(doggie)

for dog in dogs_breeds:
    print(f"****** Checking {dog}.")
    if dog == doggie:
        print("#######################################")
        print(f"{doggie} is the best dog breed for you")
        print("#######################################")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    print("Not a matching dog breed")
    print("XXXXXXXXXXXXXXXXXXXXXXXX")


for dog in dogs_breeds:
    print(f"****** Checking {dog}.")
    if dog == doggie:
        print("#######################################")
        print(f"{doggie} is the best dog breed for you")
        print("#######################################")
        print()
        break
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    print("Not a matching dog breed")
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
