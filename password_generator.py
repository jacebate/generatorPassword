import random
import string
import pyperclip

print("=== Advanced Password Generator ===\n")

#Get password length
while True:
        length_input =input("Enter password length (mininum 8):  ".strip())
        if length_input.isdigit():
            length = int(length_input)
            if length >= 8:
                break
            else:
                print("please enter a number 8 or higher.")
        else:
            print("Please enter a valid number.")

#Get user prefeces 
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special symbols? (y/n): ").lower() == 'y'

#Get how many passwords to generate
while True:
    try:
        quantity = int(input ("How many passwords do you want to generate? "))
        if quantity > 0:
            break
        print("Please enter at least 1. ")
    except ValueError:
        print("Please enter a valid number. ")

#Build the character pool based on user choices
char_pool = ""

if use_lower:
    char_pool += string.ascii_lowercase
if use_upper:
    char_pool += string.ascii_uppercase
if use_numbers:
    char_pool += string.digits
if use_symbols:
    char_pool += string.punctuation

# Safety check
if not char_pool:
    print("You must select at least one character type!")
    exit()

# Generate passwords
print(f"\nGeneratin {quantity} password(s)... \n")

passwords = [] 

for i in range(quantity):
    password = ''.join(random.choice(char_pool) for _ in range(length))
    passwords.append(password)
    print(f"Password {i+1}: {password}")

#copy the first password to clipboard
if quantity == 1:
    pyperclip.copy(passwords[0])
    print("\nPassword has been copied to clipboard!")
else:
    #copy the first one and notify
    pyperclip.copy(passwords[0])
    print("\nFirst password has been copied to clipboard!")