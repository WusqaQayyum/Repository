import random
import string

def generate_password(length, num_letters, num_digits, num_special):
    if length < num_letters + num_digits + num_special:
        print(
            "Error: The total length should be equal to or greater than the sum of letters, digits, and special characters.")
        return None

    chars = string.ascii_letters + string.digits + string.punctuation

    password_letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))

    password_digits = ''.join(random.choice(string.digits) for _ in range(num_digits))

    password_special = ''.join(random.choice(string.punctuation) for _ in range(num_special))

    remaining_length = length - num_letters - num_digits - num_special
    password_remaining = ''.join(random.choice(chars) for _ in range(remaining_length))

    password = password_letters + password_digits + password_special + password_remaining

    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


# User input
length = int(input("Enter the total length of your password: "))
num_letters = int(input("Enter the number of letters in your password: "))
num_digits = int(input("Enter the number of digits in your password: "))
num_special = int(input("Enter the number of special characters in your password: "))

generated_password = generate_password(length, num_letters, num_digits, num_special)

if generated_password:
    print("Your random password is:", generated_password)
