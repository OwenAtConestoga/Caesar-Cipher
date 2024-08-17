def encrypt_text(plaintext, n):
    ans = ""
    # Iterate over the given text
    for ch in plaintext:
        # Check if space is there then simply add space
        if ch == " ":
            ans += " "
        # Check if a character is uppercase then encrypt it accordingly
        elif ch.isupper():
            ans += chr((ord(ch) - 65 + n) % 26 + 65)
        # Check if a character is lowercase then encrypt it accordingly
        elif ch.islower():
            ans += chr((ord(ch) - 97 + n) % 26 + 97)
        else:
            # If it's not a letter, add it unchanged
            ans += ch

    return ans

# Take user input for plaintext and shift value
plaintext = input("Enter the text to encrypt: ")
n = int(input("Enter the shift value (n): "))

print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))
