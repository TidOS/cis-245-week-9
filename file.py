#!/usr/bin/env python3

# Assignment 10.1 - Stock Dicitionary
# CIS 245 - Jordan Thomas
# February 20, 2021
#

'''
This week we will create a program that performs file processing activities.  
Your program this week will use the OS library in order to validate that a 
directory exists before creating a file in that directory.  Your program will 
prompt the user for the directory they would like to save the file in as well 
as the name of the file.  The program should then prompt the user for their name, 
address, and phone number.  Your program will write this data to a comma separated 
line in a file and store the file in the directory specified by the user. 
Once the data has been written your program should read the file you just wrote to 
the file system and display the file contents to the user for validation purposes. 
Submit a link to your Github repository.
'''
import os
import re

def printFile(f):
    for line in f:
        print(line)

def writeFile(f, name, address, phone):
    """Write "name,address,phone" to file f"""
    # we will encapsulate each field in " marks so we can have commas in our address
    f.write("\"" + name + "\",\"" + address + "\",\"" + phone + "\"")


def checkPath(path) -> bool:
    """check if a path exists"""
    return os.path.isdir(path)

def createPath(path) -> bool:
    """attempt to create a path path, return True if successful
    return False if unsuccessful"""
    try:
        os.makedirs(path)
        return True
    except OSError:
        return False

def main():
    validPath = False
    while not validPath:
        path = input("Directory to save file into? ")
        if not checkPath(path):
            print("Path does not exist, trying to create it.")
            if not createPath(path):
                print("Could not make path, try another.")
            else:
                validPath = True
        else:
            validPath = True
    # If our path doesn't end in / it could still be valid 
    # but we need to have a / as the last character so we can
    # add our file name
    if path[-1] != "/":
        path = path + "/"
    
    filename = input("Filename? ")
    fp = path + filename
    
    name = input("Your name: ")
    address = input("Your address: ")
    # crazy regex to check for phone numbers
    # don't know how great it is but whatever
    phonecheck = re.compile("^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?$")

    validPhone = False
    while not validPhone:
        number = input("Your phone number: ")
        if phonecheck.match(number):
            validPhone = True
        else:
            print("Try another number please. ")

    # write file
    f = open(fp,"w")
    writeFile(f,name,address,number)
    f.close()

    # reopen file and print it
    f = open(fp,"r")
    printFile(f)
    f.close()

if __name__ == "__main__":
    main()