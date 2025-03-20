name = input("What's your name: ")

import re

while not re.search("^[a-zA-Z]{3,}$",name):
  name = input("Invalid name ,please try again: ")

email = input("Enter your Email: ")

while not re.search("^[a-zA-Z1-9_.]{3,}@[a-z]+.[a-z]{3,}$",email):
  email = input("Invalid Email ,please try again: ")


print(f"Welcome {name} Your email is {email}")
