import random
import string

print("====================================")
print("        PASSWORD GENERATOR")
print("====================================")

again = "y"

while again == "y":

    length = int(input("\nEnter password length: "))

    print("\nSelect what to include in password:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols")

    choice = input("Enter choice (1/2/3): ")

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if choice == "1":
        chars = letters
    elif choice == "2":
        chars = letters + numbers
    elif choice == "3":
        chars = letters + numbers + symbols
    else:
        print("Invalid choice, using letters only.")
        chars = letters

    password = ""
    for i in range(length):
        password = password + random.choice(chars)

    print("\n------------------------------------")
    print("Your Password:", password)
    print("------------------------------------")

    again = input("\nGenerate another password? (y/n): ")

print("\nThank you for using Password Generator!")