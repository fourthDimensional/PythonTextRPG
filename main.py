# 86 Inspired Python RPG v0.1

# Imports:

import os
import sys as sus
import time
import json

# Variables

# Preliminary Classes:
class items:
    def __init__(self, itemid, name, value, marketable, description):
        self.itemid = itemid
        self.name = name
        self.value = value
        self.marketable = marketable
        self.description = description
        
    def sellItem(self, modifier):
        pass
        
class units:
    def __init__(self, unitid):
        self.unitid = unitid
        pass
    
class legion(units):
    pass
class friendly(units):
    pass
        
print("\n86 Python RPG v0.1 \n")
print("1) Login\n")
print("2) Create Account\n")
print("3) Exit\n")

while True:
    answer = int(input("Input: "))
    
    if answer == 1:
        break
    elif answer == 2:
        print("\nEnter a username and password\n")
        username = input("Username: ")
        confirmPassword1 = input("Password: ")
        confirmedPassword2 = input("Confirm Password: ")
        if confirmPassword1 == confirmedPassword2:
            password = confirmPassword1 
            with open(username + ".save", "w") as file:
                file.writelines(username + "\n")
                file.writelines(password + "\n")
        break
    elif answer == 3:
        os.system("CLS")
        print("Confirm Exit?\n")
        while True:
            answer = input("Input: ")
            if answer.lower() == "yes" or answer.lower() == "exit":
                sus.exit()
            elif answer.lower() == "no":
                os.system("CLS")
                print("86 Python RPG v0.1 \n")
                print("1) Login\n")
                print("2) Create Account\n")
                print("3) Exit\n")
                break
            else:
                print("Invalid Answer, Please Input 'yes' or 'no'\n")       
    else:
        print("Invalid Answer, Please Input '1' or '2'")
   

print("Enter your username and password\n")
username = input("Username: ")
password = input("Password: ")
print("game")