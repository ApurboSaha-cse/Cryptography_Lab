def caesar_encrypt(plaintext, shift=3):
    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char  # keep punctuation, spaces
    return encrypted

def caesar_decrypt(ciphertext, shift=3):
    return caesar_encrypt(ciphertext, -shift)

# --- Example Usage ---
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    
    encrypted = caesar_encrypt(plaintext, 3)
    print("\nEncrypted (Caesar Cipher):")
    print(encrypted)

    decrypted = caesar_decrypt(encrypted, 3)
    print("\nDecrypted (Original Plaintext):")
    print(decrypted)
