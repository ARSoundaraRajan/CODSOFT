#import random module from the python library
import random

#import string module from the python library
import string

#Creating variables for each type of character
letters = string.ascii_letters
numbers = string.digits

# Combining all characters for password generation
total_characters = letters + numbers

# Getting the desired password length from the user
length = int(input("Enter the length of the password: "))

# Generating the password
password = "".join(random.choices(total_characters, k=length))

# Printing the generated password
print("The password is:", password)
