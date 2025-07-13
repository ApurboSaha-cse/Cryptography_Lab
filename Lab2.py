import random

def preprocess(text):
    return ''.join(filter(str.isalpha, text.upper()))

def pad_text(text, block_size=3):
    pad_len = block_size - len(text) % block_size if len(text) % block_size != 0 else 0
    return text + 'X' * pad_len

def generate_polygram_key():
    # Example: generate fixed key for all 3-letter blocks made from A–Z
    # For demonstration, map 100 most frequent trigrams (use shorter mapping)
    from itertools import product
    blocks = [''.join(p) for p in product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=3)]
    selected_blocks = blocks[:100]
    shuffled_blocks = selected_blocks[:]
    random.shuffle(shuffled_blocks)
    key = dict(zip(selected_blocks, shuffled_blocks))
    return key

def encrypt_polygram(plaintext, key, block_size=3):
    plaintext = pad_text(preprocess(plaintext), block_size)
    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)]
    ciphertext = ''
    for block in blocks:
        ciphertext += key.get(block, block)  # default to original if block not found
    return ciphertext

def decrypt_polygram(ciphertext, key, block_size=3):
    reverse_key = {v: k for k, v in key.items()}
    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    plaintext = ''
    for block in blocks:
        plaintext += reverse_key.get(block, block)  # default to original if not found
    return plaintext

# --- Example Usage ---
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    
    key = generate_polygram_key()  # You can also define your own mapping for consistency
    cipher = encrypt_polygram(plaintext, key)
    print("\nEncrypted (Polygram Substitution Cipher):")
    print(cipher)

    decrypted = decrypt_polygram(cipher, key)
    print("\nDecrypted (Original Plaintext):")
    print(decrypted)

    # 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
