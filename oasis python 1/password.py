import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generates a random password based on user preferences."""
    if not (use_letters or use_numbers or use_symbols):
        raise ValueError("At least one character type must be selected.")
    
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
