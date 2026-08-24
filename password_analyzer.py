import getpass
import random
import string
print("================================")
print("   SECUREPASS - PASSWORD TOOL")
print("================================")

password = getpass.getpass("Enter your password: ")

score = 0
common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "123456789",
    "admin",
    "password123",
    "qwerty123"
]

suggestions = []
if " " in password:
    suggestions.append("Avoid using spaces in your password.")
name = input("Enter your name: ")

if name.lower() in password.lower():
    suggestions.append("Avoid using your name in the password.")
if password.lower() in common_passwords:
    suggestions.append("This is a commonly used password. Choose a more unique password.")

if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

if any(char.isupper() for char in password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter.")

if any(char.islower() for char in password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter.")

if any(char.isdigit() for char in password):
    score += 1
else:
    suggestions.append("Add at least one number.")

if any(char in "!@#$%^&*()_+-=" for char in password):
    score += 1
else:
    suggestions.append("Add at least one special character.")

print("\nPassword Analysis")
print("-----------------")
print("Score:", score, "/ 5")
if password.lower() in common_passwords:
    print("Strength: 🔴 WEAK")
elif score <= 2:
    print("Strength: 🔴 WEAK")
elif score <= 4:
    print("Strength: 🟡 MEDIUM")
else:
    print("Strength: 🟢 STRONG")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("- " + suggestion)
else:
    print("\nYour password meets all basic requirements!")

def generate_password(length=12):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = uppercase + lowercase + digits + special

    for i in range(length - 4):
        password.append(random.choice(all_characters))
 
    random.shuffle(password)

    return ''.join(password)
length = int(input("\nEnter password length: "))

if length < 8:
    print("\nPassword length should be at least 8 characters.")
else:
    print("\nGenerated Strong Password:")
    print(generate_password(length))