import random
import string

def generate_password(c, l):
    password = "".join(random.choices(c, k=l))
    return f"Generate password: {password}"

length = int(input("Enter password length: "))
letters = input("Include letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
special = input("Include special characters? (y/n): ")
if letters == "y" and numbers == "y" and special == "y":
    characters = string.ascii_letters + string.digits + string.punctuation
    print(generate_password(characters, length))
elif letters == "y" and numbers == "y" and special == "n":
    characters = string.ascii_letters + string.digits
    print(generate_password(characters, length))
elif letters == "n" and numbers == "y" and special == "y":
    characters = string.digits + string.punctuation
    print(generate_password(characters, length))
elif letters == "y" and numbers == "n" and special == "y":
    characters = string.ascii_letters + string.punctuation
    print(generate_password(characters, length))
elif letters == "n" and numbers == "y" and special == "n":
    characters = string.digits
    print(generate_password(characters, length))
elif letters == "y" and numbers == "n" and special == "n":
    characters = string.ascii_letters
    print(generate_password(characters, length))
elif letters == "n" and numbers == "n" and special == "y":
    characters = string.punctuation
    print(generate_password(characters, length))
else:
    print("Please input valid answers")
