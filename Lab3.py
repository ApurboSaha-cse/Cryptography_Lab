import math

def encrypt_transposition(plaintext, width):
    plaintext = plaintext.replace(" ", "").upper()
    length = len(plaintext)
    height = math.ceil(length / width)
    padded_length = height * width
    padded_text = plaintext.ljust(padded_length, 'X')  # Padding with X

    # Create the grid row-wise
    grid = [padded_text[i:i+width] for i in range(0, padded_length, width)]

    # Read column-wise
    ciphertext = ""
    for col in range(width):
        for row in range(height):
            ciphertext += grid[row][col]
    
    return ciphertext

def decrypt_transposition(ciphertext, width):
    length = len(ciphertext)
    height = math.ceil(length / width)

    # Build columns
    cols = [''] * width
    k = 0
    for col in range(width):
        for row in range(height):
            if k < len(ciphertext):
                cols[col] += ciphertext[k]
                k += 1

    # Read row-wise from columns
    plaintext = ""
    for row in range(height):
        for col in range(width):
            if row < len(cols[col]):
                plaintext += cols[col][row]

    return plaintext

# --- Example Usage ---
if __name__ == "__main__":
    text = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH"
    width = int(input("Enter width (number of columns): "))

    cipher = encrypt_transposition(text, width)
    print("\nEncrypted Text:")
    print(cipher)

    plain = decrypt_transposition(cipher, width)
    print("\nDecrypted Text:")
    print(plain)
