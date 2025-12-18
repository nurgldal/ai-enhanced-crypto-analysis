import string
from encryptions import (
    caesar_decrypt,
    vigenere_decrypt,
    xor_decrypt
)

ALPHABET = string.ascii_uppercase

#Utility
def score_english(text: str) -> int:
    """
    Simple English scoring function.
    Counts common English letters.
    """
    common = "ETAOIN SHRDLU"
    score = 0
    for ch in text.upper():
        if ch in common:
            score += 1
    return score

#Caesar Attack
def caesar_attack(ciphertext: str):
    best_score = -1
    best_plaintext = ""
    best_shift = None

    for shift in range(1, 26):
        plaintext = caesar_decrypt(ciphertext, shift)
        score = score_english(plaintext)

        if score > best_score:
            best_score = score
            best_plaintext = plaintext
            best_shift = shift

    return best_plaintext, best_shift

#Vigenere Attack (simple, fixed key length) 
def vigenere_attack(ciphertext: str, key_length=3):
    best_score = -1
    best_plaintext = ""
    best_key = None

    for key in ["KEY", "TEST", "DATA", "CODE"]:
        plaintext = vigenere_decrypt(ciphertext, key)
        score = score_english(plaintext)

        if score > best_score:
            best_score = score
            best_plaintext = plaintext
            best_key = key

    return best_plaintext, best_key

#XOR Attack (brute-force)
def xor_attack(ciphertext_hex: str):
    best_score = -1
    best_plaintext = ""
    best_key = None

    for key in range(1, 256):
        try:
            plaintext = xor_decrypt(ciphertext_hex, key)
            score = score_english(plaintext)

            if score > best_score:
                best_score = score
                best_plaintext = plaintext
                best_key = key
        except:
            continue

    return best_plaintext, best_key

#Main dispatcher 
def attack(cipher_type: str, ciphertext: str):
    if cipher_type == "CAESAR":
        return caesar_attack(ciphertext)

    elif cipher_type == "VIGENERE":
        return vigenere_attack(ciphertext)

    elif cipher_type == "XOR":
        return xor_attack(ciphertext)

    else:
        raise ValueError("Unknown cipher type")

