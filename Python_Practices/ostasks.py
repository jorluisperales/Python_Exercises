#!/usr/bin/python3

import os

userlist = ["Gina", "Greg", "Gil", "JP"]
print("Adding users to system")
print("##################################################################")


# Loop to add user from userlist
for user in userlist:
    exitcode = os.system(f"id {user}")
    if exitcode != 0:
        print(f"User {user} does not exist. Adding it.")
        print("#######################################")
        print()
        os.system(f"useradd {user}")
    else:
        print(f"The user {user} exists already, skipping it")
        print("#######################################")
        print()

#Condition to check if group exists or not, ad if not exist.

exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group Science does not exist. Adding it")
    print("#######################################")
    print ()
    os.system("groupadd science")
else:
    print("Group Science already exist, skipping it")
    print("#######################################")
    print()

for user in userlist:
    print(f"Adding user {user} in the science group")
    print("#######################################")
    print()
    os.system(f"usermod -G science {user}")

print("Adding directory")
print("#######################################")
print()

if os.path.isdir("/opt/science_dir"):
    print("Directory already exist, skipping it")
else:
    os.mkdir("/opt/science_dir")

print("Assigning permission and ownership to the directory")
print("###################################################")
print()

os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")