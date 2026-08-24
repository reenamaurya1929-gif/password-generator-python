import string
import secrets

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    # Define character pools
    letters = string.ascii_letters      # a-z, A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # !@#$%^&* etc.

    all_characters = letters + digits + symbols

    # Ensure the password has at least one of each type
    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the rest of the password length randomly from all characters
    for _ in range(length - 3):
        password_chars.append(secrets.choice(all_characters))

    # Shuffle so the guaranteed characters aren't always at the start
    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def main():
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    if password:
        print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()