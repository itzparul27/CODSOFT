
import random
 
def get_characters(upper, lower, digits, symbols):
    characters = ""
 
    if upper:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
    if lower:
        characters += "abcdefghijklmnopqrstuvwxyz"
 
    if digits:
        characters += "0123456789"
 
    if symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
 
    return characters
 
def get_yes_no(message):
    while True:
        answer = input(message).lower()
 
        if answer == "y" or answer == "yes":
            return True
 
        elif answer == "n" or answer == "no":
            return False
 
        else:
            print("Please enter y or n.")
 
def generate_password(length, characters):
    password = ""
 
    for i in range(length):
        password += random.choice(characters)
 
    return password
 
def main():
    print("=== Password Generator ===")
 
    while True:
        try:
            length = int(input("Password length (minimum 4): "))
 
            if length >= 4:
                break
            else:
                print("Length must be at least 4.")
 
        except ValueError:
            print("Please enter a valid number.")
 
    upper = get_yes_no("Include uppercase letters? (y/n): ")
    lower = get_yes_no("Include lowercase letters? (y/n): ")
    digits = get_yes_no("Include digits? (y/n): ")
    symbols = get_yes_no("Include symbols? (y/n): ")
 
    characters = get_characters(upper, lower, digits, symbols)
 
    if characters == "":
        print("You must select at least one character category.")
        return
 
    while True:
        password = generate_password(length, characters)
 
        print("Generated password:", password)
 
        again = get_yes_no("Generate another password? (y/n): ")
 
        if again == False:
            break
 
    print("Goodbye!")
 
main()
