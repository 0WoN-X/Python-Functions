
import numpy as np
from math import gcd

# Key matrix
key = np.array([[3, 3],
                [2, 5]])

# Calculate inverse of key matrix modulo 26
def inverse_key(key):
    det = int(round(np.linalg.det(key))) % 26

    if gcd(det, 26) != 1:
        raise ValueError("Invalid key matrix!")

    det_inv = pow(det, -1, 26)

    adj = np.array([
        [key[1, 1], -key[0, 1]],
        [-key[1, 0], key[0, 0]]
    ])

    return (det_inv * adj) % 26


# Encryption function
def encrypt(text, key):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        pair = text[i:i+2]

        vector = np.array([
            ord(pair[0]) - 65,
            ord(pair[1]) - 65
        ])

        encrypted = key @ vector % 26

        result += chr(int(encrypted[0]) + 65)
        result += chr(int(encrypted[1]) + 65)

    return result


# Decryption function
def decrypt(text, key):
    inv_key = inverse_key(key)
    result = ""

    for i in range(0, len(text), 2):
        pair = text[i:i+2]

        vector = np.array([
            ord(pair[0]) - 65,
            ord(pair[1]) - 65
        ])

        decrypted = inv_key @ vector % 26

        result += chr(int(decrypted[0]) + 65)
        result += chr(int(decrypted[1]) + 65)

    return result


# Main program
message = input("Enter your message: ")

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted message:", decrypted)
