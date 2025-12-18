import string
import random

ALPHABET = string.ascii_uppercase

def normalize_text(text: str) -> str:
    """
    Keep only letters A-Z and convert to uppercase.
    This simplifies classical cipher analysis.
    """
    return "".join(ch for ch in text.upper() if ch.isalpha())

#Caesar Cipher
def caesar_encrypt(plaintext: str, shift: int) -> str:
    plaintext = normalize_text(plaintext)
    result = []

    for ch in plaintext:
        idx = ALPHABET.index(ch)
        new_idx = (idx + shift) % 26
        result.append(ALPHABET[new_idx])

    return "".join(result)


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)

#Vigenere Cipher
def generate_vigenere_key(length: int) -> str:
    return "".join(random.choice(ALPHABET) for _ in range(length))

def vigenere_encrypt(plaintext: str, key: str) -> str:
    plaintext = normalize_text(plaintext)
    key = normalize_text(key)
    result = []

    for i, ch in enumerate(plaintext):
        p_idx = ALPHABET.index(ch)
        k_idx = ALPHABET.index(key[i % len(key)])
        c_idx = (p_idx + k_idx) % 26
        result.append(ALPHABET[c_idx])

    return "".join(result)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    ciphertext = normalize_text(ciphertext)
    key = normalize_text(key)
    result = []

    for i, ch in enumerate(ciphertext):
        c_idx = ALPHABET.index(ch)
        k_idx = ALPHABET.index(key[i % len(key)])
        p_idx = (c_idx - k_idx) % 26
        result.append(ALPHABET[p_idx])

    return "".join(result)

#XOR Cipher
def xor_encrypt(plaintext: str, key: int) -> str:
    """
    XOR encryption with single-byte key.
    Output is hex string for safe storage.
    """
    data = plaintext.encode("utf-8")
    encrypted = bytes([b ^ key for b in data])
    return encrypted.hex().upper()

def xor_decrypt(ciphertext_hex: str, key: int) -> str:
    data = bytes.fromhex(ciphertext_hex)
    decrypted = bytes([b ^ key for b in data])
    return decrypted.decode("utf-8", errors="replace")

#Manual test

if __name__ == "__main__":
    text = "Hello World this is a crypto test"

    print("Original:", text)

    #Caesar
    shift = 3
    c_enc = caesar_encrypt(text, shift)
    c_dec = caesar_decrypt(c_enc, shift)
    print("\n[Caesar]")
    print("Encrypted:", c_enc)
    print("Decrypted:", c_dec)

    #Vigenere
    key = "KEY"
    v_enc = vigenere_encrypt(text, key)
    v_dec = vigenere_decrypt(v_enc, key)
    print("\n[Vigenere]")
    print("Encrypted:", v_enc)
    print("Decrypted:", v_dec)

    #XOR
    xor_key = 42
    x_enc = xor_encrypt(text, xor_key)
    x_dec = xor_decrypt(x_enc, xor_key)
    print("\n[XOR]")
    print("Encrypted:", x_enc)
    print("Decrypted:", x_dec)

