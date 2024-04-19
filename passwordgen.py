import random

def generate_password(length=10):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Password Generator\n")
    length = int(input("Enter the length of the password you want to generate: \n"))
    
    if length <= 0:
        print("Invalid length. Password length should be greater than 0.")
    else:
        password = generate_password(length)
        print("Your generated password is:", password)

if __name__ == "__main__":
    main()
