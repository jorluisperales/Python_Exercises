planet1="Closest to Sun"
print(planet1)

print(planet1[0]) # Printing the first index (left to right)
print(planet1[1])
print(planet1[2])

print(planet1[-1]) # Printing the indexes from right to left)
print(planet1[-2])
print(planet1[-3])

# Slicing a string, get a substring from a string

print(planet1[1:4])
print(planet1[:]) # print everything
print(planet1[:7]) # till the 7 Characters
print(planet1[11:])

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
# With tuples, each value is also indexed.

print(devops[0])
print(devops[4])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0]) # Slice the tuple and extrac the first index of that new list
print(devops[2:5][0][5:11]) # Slice further already sliced list and value "Bash script"
print(devops[2:5][0][5:11][-1])

devops1 = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
# With Lists, each value is also indexed.

print(devops1[0])
print(devops1[4])
print(devops1[-1])
print(devops1[2:5])
print(devops1[2:5][0]) # Slice the tuple and extrac the first index of that new list
print(devops1[2:5][0][5:11]) # Slice further already sliced list and value "Bash script"
print(devops1[2:5][0][5:11][-1])

#Dictionary Example

Skills = {"Devops":("AWS", "Jenkins", "Python", "Ansible"), "Development":["Java", "NodeJS", ".net"]} # This dic contains a tupple and a list
print(Skills["Devops"])
print(Skills["Development"])

#Slicing further

print(Skills["Development"][-1])
print(Skills["Development"][-1][3])