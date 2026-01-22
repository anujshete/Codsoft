import random
import string

print("===================================")
print("        PASSWORD GENERATOR          ")
print("===================================")

length = int(input("Enter password length: "))

print("\nChoose what to include in password:")
print("1. Letters (A-Z, a-z)")
print("2. Numbers (0-9)")
print("3. Symbols (!@#$%^&*)")

use_letters = input("Include letters? (yes/no): ").lower()
use_numbers = input("Include numbers? (yes/no): ").lower()
use_symbols = input("Include symbols? (yes/no): ").lower()

characters = ""

if use_letters == "yes":
    characters = characters + string.ascii_letters

if use_numbers == "yes":
    characters = characters + string.digits

if use_symbols == "yes":
    characters = characters + string.punctuation

if characters == "":
    print("\nError: You must select at least one character type.")
else:
    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    print("\nGenerated Password:")
    print(password)

print("\nThank you for using Password Generator!")
