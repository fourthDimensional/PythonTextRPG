# 86 Inspired Python RPG v0.1

# Imports:

import os
import sys as sus
import time
import json
import pickle as pk 

# Variables

# Preliminary Classes:

    # 'Templates' for accounts
class account:
    def __init__(self, username, password, money):
        self.username = username
        self.password = password
        self.money = money

class unit:
    def __init__(self, health, armor, ammo, skill):
        self.health = health
        self.armor = armor
        self.ammo = ammo
        self.skill = skill

class items:
    def __init__(self, itemid, name, value, marketable, description):
        self.itemid = itemid
        self.name = name
        self.value = value
        self.marketable = marketable
        self.description = description
        
    def sellItem(self, modifier):
        pass
    
class legion(units):
    pass
class friendly(units):
    pass
        
print("\n86 Python RPG v0.1 \n")
print("1) Login\n")
print("2) Create Account\n")
print("3) Exit\n")
print("4) Play w/o account\n")

while True:
    answer = int(input("Input: "))
    
    if answer == 1:
        
        print("\nEnter your username and password\n")
        
        username = input("Username: ")
        password = input("Password: ")
        
        openFile = open(username + ".save", "r")
        
        if password == openFile.read(1):
            
            print("Successfully logged in.")
            
        else: 
            print("\nInvalid Password, Please Try Again")
        break
    
    elif answer == 2:
        print("\nEnter a username and password\n")
        username = input("Username: ")
        confirmPassword1 = input("Password: ")
        confirmedPassword2 = input("Confirm Password: ")
        if confirmPassword1 == confirmedPassword2:
            password = confirmPassword1 
            file = open(username + ".save", "w")
            pk.dump(password, file)
            file.close
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
                print("4) Play w/o account\n")
                
                break
            
            else:
                print("Invalid Answer, Please Input 'yes' or 'no'\n")     
    elif answer == 4:
        break
    else:
        print("Invalid Answer, Please Input '1' or '2'")
        
# Main Game Features/Loop:
    # Gathering intel
    # Defending against legion attacks
    # Attacking the legion
    # Repairing own units
    # Expanding base
    # Resource management

while True:
    
    print("\nGameplay\n")
    print("1) Intel\n")
    print("3) Military Actions\n")
    print("3) Units\n")
    print("4) Homebase\n")
    
    answer = input("Action #: ")
    
    while True:
        if answer == 1:
            
            print("\nIntel Tab\n")
            print("1) Recon\n")
            print("2) Legion\n")
            print("3) Allies\n")
            
            answer = input("Action #: ")
            
            if answer == 1:
                
            elif answer == 2:
                
            elif answer == 3:
                
            else:
                
        elif answer == 2:
            
        elif answer == 3:
            
        elif answer == 4:
            
        else: