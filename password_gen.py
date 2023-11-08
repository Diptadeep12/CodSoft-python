import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length > 0:
                return length
            else:
                print("Length must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    length = get_user_input()
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
