"""

This script will implement our knowledge on
conditions and different datatypes

"""

print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised Values:")
DevOps = ["Jenkins", "Ansible", "Bash", "Python3", "Puppet", "Docker", "Kubernetes", "Terraform"] # List
Development = ("NodeJS", "AngularJS", "Java", ".net", "Python") # Tuple
cntr_emp1 = {"Name":"Santa", "Skill": "Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill": "AI", "Code":1218}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

# Check in the database if we have this skill

if (usr_skill in DevOps):
    print(f"We have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()): # this will check the values of the dictionary.
    print(f"We have contract employes with {usr_skill} skill")
else:
    print("Skill not found.")
    print("Please check if you have entered value in capitalize or check the spelling.")