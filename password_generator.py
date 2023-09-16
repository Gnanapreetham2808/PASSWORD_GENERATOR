import random
import string

# Function to generate a random password of the specified length
def generate_password(length):
    # Define the characters to use for the password (letters, digits, and special characters)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use a list comprehension to create a password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function to interact with the user
def main():
    while True:
        try:
            # Prompt the user for the desired password length
            length = int(input("Enter the desired password length: "))
            
            # Check if the user provided a valid positive integer
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                # Generate the password
                password = generate_password(length)
                
                # Display the generated password
                print("Generated Password:", password)

            # Ask the user if they want to generate another password
            another_password = input("Generate another password? (yes/no): ").lower()
            
            # Check if the user wants to generate another password
            if another_password != "yes":
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
