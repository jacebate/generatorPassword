import random
import string
import pyperclip

def main():
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

#Present modes
print("\nChoose password type:")
print("1. strong (Upper, lower, numbers, symbols)")
print("2.medium (upper, lower, Numbers)")
print("3. simple (letters only)")

while True:
    choice = input("\nEnter your choice (1/2/3): ").strip()
    if choice in ["1", "2", "3"]:
        break
    print("Please enter 1, 2, or 3.")

#set character requirements based on choice
if choice == "1":
    char_pool= string.ascii_letters + string.digits + string.punctuation
    print("Mode: Strong" )
elif choice == "2":
    char_pool = string.ascii_letters + string.digits
    print("Mode: Medium")
else:
    char_pool = string.ascii_letters
    print("Mode: Simple")

#Get how many passwords to generate
while True:
    try:
        quantity = int(input ("How many passwords do you want to generate? "))
        if quantity > 0:
            break
        print("Please enter at least 1. ")
    except ValueError:
        print("Please enter a valid number. ")

# Generate passwords and display them
print(f"\nGenerating {quantity} password(s)... \n")

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

# this line runs the main function when you run the script
if __name__ == "__main__":
    main()

