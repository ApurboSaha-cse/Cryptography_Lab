def char_to_index(char):
    return ord(char.upper()) - ord('A')

def index_to_char(index):
    return chr((index % 26) + ord('A'))

def one_time_pad_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")  # sanitize
    key = key.upper()

    if len(key) < len(plaintext):
        raise ValueError("Key is shorter than plaintext!")

    cipher_text = ""
    for p, k in zip(plaintext, key):
        pi = char_to_index(p)
        ki = char_to_index(k)
        ci = (pi + ki) % 26
        cipher_text += index_to_char(ci)
    
    return cipher_text

def one_time_pad_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()

    if len(key) < len(cipher_text):
        raise ValueError("Key is shorter than ciphertext!")

    plain_text = ""
    for c, k in zip(cipher_text, key):
        ci = char_to_index(c)
        ki = char_to_index(k)
        pi = (ci - ki + 26) % 26
        plain_text += index_to_char(pi)
    
    return plain_text

# --- Load key from file ---
def load_key_from_file(filepath):
    with open(filepath, 'r') as f:
        return f.read().strip()

# --- Example usage ---
if __name__ == "__main__":
    plaintext = "HELLOCRYPTOGRAPHY"
    key = load_key_from_file("key.txt")  # this file must contain long random letters A–Z

    encrypted = one_time_pad_encrypt(plaintext, key)
    decrypted = one_time_pad_decrypt(encrypted, key)

    print("Plaintext :", plaintext)
    print("Key       :", key[:len(plaintext)])
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
