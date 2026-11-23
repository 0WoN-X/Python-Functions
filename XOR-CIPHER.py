
def xor_cipher(text, key):
    result = ""

    for char in text:
        result += chr(ord(char) ^ ord(key))

    return result


# Main program
message = input("Enter your message: ")
key = input("Enter XOR key: ")

if len(key) != 1:
    print("Key must be exactly one character!")
else:
    encrypted = xor_cipher(message, key)
    print("Encrypted:", encrypted)

    decrypted = xor_cipher(encrypted, key)
    print("Decrypted:", decrypted)
