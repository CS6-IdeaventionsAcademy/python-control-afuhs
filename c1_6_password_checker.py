# Alexandra Fuhs
# 11/15/17
# Python Beginnings
# 6 Password Checker

import time
username = "Pusheen"
password = "tuRk3y"
print("starting up...")
time.sleep(3)

name = input("What is your username?")
pw = input ("What is the password?")

if name == username:
    if pw == password:
        print ("Access granted!")
    else:
        print ("Incorrect!")
else:
    print ("Incorrect!")

