import string 
import random

def generate_password(length, include_uppercase, include_numbers, include_special):
    # Validate password length against criteria
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError('Password length is too short for the specified criteria.')
  
    password = ''

    # Ensure at least one character from each selected category
    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    # Create a pool of characters to fill the rest of the password
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Fill the remaining length with random characters
    for _ in range(length - len(password)):
        password += random.choice(characters)

    # Shuffle the password to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    # Get user input for password criteria
    length = int(input('Enter password length: '))
    include_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
    include_special = input('Include special characters? (y/n): ').lower() == 'y'
    
    try:
        # Generate and display the password
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(password)
    except ValueError as e:
        print(e)  # Handle errors


if __name__ == '__main__':
    main()  # Run the program