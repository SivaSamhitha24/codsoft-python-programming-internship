import random
import string

def generate_password(length, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, digits, special_chars)

    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()