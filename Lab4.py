import math
import random

def auto_generate_key(length):
    key = list(range(length))
    random.shuffle(key)
    return key

def double_transposition_encrypt_dynamic(plaintext):
    plaintext = plaintext.replace(" ", "").upper()
    length = len(plaintext)

    # Choose a grid that's roughly square
    cols = math.ceil(math.sqrt(length))
    rows = math.ceil(length / cols)
    padded_text = plaintext.ljust(rows * cols, 'X')

    col_key = auto_generate_key(cols)
    row_key = auto_generate_key(rows)

    # Build grid
    grid = [padded_text[i:i+cols] for i in range(0, len(padded_text), cols)]
    # Transpose rows
    grid = [grid[i] for i in row_key]
    # Transpose columns
    grid = [''.join([row[i] for i in col_key]) for row in grid]

    cipher = ''.join(grid)
    return cipher, row_key, col_key, rows, cols

def double_transposition_decrypt_dynamic(cipher, row_key, col_key, rows, cols):
    inverse_col = [0]*len(col_key)
    for i, k in enumerate(col_key):
        inverse_col[k] = i

    inverse_row = [0]*len(row_key)
    for i, k in enumerate(row_key):
        inverse_row[k] = i

    # Break into grid
    grid = [cipher[i:i+cols] for i in range(0, len(cipher), cols)]
    # Reverse column transposition
    grid = [''.join([row[i] for i in inverse_col]) for row in grid]
    # Reverse row transposition
    grid = [grid[i] for i in inverse_row]

    plaintext = ''.join(grid)
    return plaintext.rstrip('X')  # remove padding

# --- Example Usage ---
if __name__ == "__main__":
    text = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH"
    cipher, row_key, col_key, rows, cols = double_transposition_encrypt_dynamic(text)
    print(f"Encrypted:\n{cipher}\n")

    decrypted = double_transposition_decrypt_dynamic(cipher, row_key, col_key, rows, cols)
    print(f"Decrypted:\n{decrypted}")
