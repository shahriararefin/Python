# Define the shift value
shift = 515

# Input plaintext from the user
plaintext = input("Enter the plaintext: ")

# Initialize an empty string for the ciphertext
ciphertext = ""

# Iterate over each character in the plaintext
for char in plaintext:
    # Check if the character is an uppercase letter
    if 'A' <= char <= 'Z':
        # Shift character and wrap around the alphabet
        shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        ciphertext += shifted_char
    # Check if the character is a lowercase letter
    elif 'a' <= char <= 'z':
        # Shift character and wrap around the alphabet
        shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        ciphertext += shifted_char
    else:
        # If it's not a letter, just add it to the ciphertext unchanged
        ciphertext += char

# Print the ciphertext
print("Ciphertext:", ciphertext)