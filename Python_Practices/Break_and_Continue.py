# Break Statement

for i in "DevOps":
    print(i)
    if (i == "O"):
        print("Found my data.")
        break
print("Out of the loop")

# Continue Statement

for i in "DevOps":
    if (i == "O"):
        print("Found my data.")
        continue # Skip and do the rest, it will continue printing the sequence until it finishes
    print(f"Value of i is {i}.")
print("Out of the loop")


