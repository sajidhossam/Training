import random as rnd
import string as str_lib

def generate_password(length, use_special_chars, use_numbers, use_uppercase):
    # Define the character sets
    characters = str_lib.ascii_lowercase  # Start with lowercase letters
    if use_special_chars:
        characters += str_lib.punctuation  # Add special characters
    if use_numbers:
        characters += str_lib.digits  # Add digits
    if use_uppercase:
        characters += str_lib.ascii_uppercase  # Add uppercase letters

    # Ensure password length is valid
    if length < 8:
        return "Password length should be at least 8 characters."

    # Generate the password
    password = ''.join(rnd.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        # Collect user-defined criteria
        try:
            length = int(input("Enter the length for your password: "))
        except ValueError:
            print("Invalid length. Please enter a valid number.")
            continue

        use_special_chars = input("Do you want to include special characters? (y/n): ").lower() == 'y'
        use_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
        use_uppercase = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_special_chars, use_numbers, use_uppercase)
        if "Password length should be at least" in password:
            print(password)
        else:
            print(f"Your generated password is: {password}")

        # Ask if the user wants to generate another password
        response = input("Do you want to generate another password? (y/n): ").lower()
        if response != 'y':
            print("Exiting the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
