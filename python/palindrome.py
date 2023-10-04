# Python Essentials 2 - 2.5.1.7

palindrome = True

text = input("Enter a text: ")

if text == '':
    palindrome = False  # An empty string isn't a palindrome
else:
    filtered_text = ''
    for char in text:
        if char.isalpha():  # Only letters and considered for checking
            filtered_text += char.upper()  # Case insensitive

    position = -1
    for letter in filtered_text:
        if letter != filtered_text[position]:
            palindrome = False
            break
        else:
            position -= 1

if palindrome:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
