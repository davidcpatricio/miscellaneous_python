# Taken from Python Essentials 2 - 2.5.1.6

text = input("Enter your message: ")
shift = input("Enter a number: ")

if not shift.isdigit():
    print("Range should be an integer number.")
# The shifted value should be in range 1-25 inclusive
elif int(shift) not in range(1, 26):
    print("Range should be higher than 0 and lower than 26.")
else:
    cipher = ''
    for char in text:
        # Non-alphabetic characters remain unchanged
        if not char.isalpha():
            cipher += char
            continue

        code = ord(char) + int(shift)
        if char.isupper():
            # Restarting the alphabet
            if code > ord('Z'):
                code -= 26
        else:
            # Restarting the alphabet
            if code > ord('z'):
                code -= 26

        cipher += chr(code)

    print(cipher)
