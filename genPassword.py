# Generate Password

import random
import string
import os

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure at least one of each character type is included
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    all_chars = lower + upper + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to a string
    final_password = ''.join(password)
    
    return final_password

def save_password_to_file(password, file_path="password.txt"):
    try:
        with open(file_path, 'w') as f:
            f.write(password)
        print(f"Password saved to {os.path.abspath(file_path)}")
    except IOError as e:
        print(f"Failed to save password to file: {e}")

# Example usage
password_length = 15  # You can set this to any length
password = generate_password(password_length)
print(f"Generated Password: {password}")

# Ask user if they want to save the password
save_option = input("Would you like to save the password to a file? (yes/no): ").strip().lower()

if save_option == 'yes':
    file_path = input("Enter the file path to save the password (default: password.txt): ").strip()
    if not file_path:
        file_path = "password.txt"  # Default file path
    save_password_to_file(password, file_path)
else:
    print("Password not saved to file.")
