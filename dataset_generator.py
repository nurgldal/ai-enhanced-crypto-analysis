import random
import csv

from encryptions import (
    caesar_encrypt,
    vigenere_encrypt,
    xor_encrypt,
    generate_vigenere_key
)


SENTENCES = [
    "cryptography is fun",
    "machine learning enhances cryptanalysis",
    "artificial intelligence changes security",
    "this project uses python",
    "classical ciphers are educational",
    "data preprocessing is important",
    "random forest is a strong classifier",
    "side channel attacks are dangerous",
    "ciphertext only attack scenario",
    "security depends on implementation"
]

def generate_plaintext():
    sentence = random.choice(SENTENCES)

    variations = [
        sentence,
        sentence.upper(),
        sentence.capitalize(),
        sentence + "!",
        ">> " + sentence
    ]

    return random.choice(variations)

def generate_sample():
    plaintext = generate_plaintext()
    cipher_type = random.choice(["CAESAR", "VIGENERE", "XOR"])

    if cipher_type == "CAESAR":
        shift = random.randint(1, 25)
        ciphertext = caesar_encrypt(plaintext, shift)
        key = str(shift)

    elif cipher_type == "VIGENERE":
        key_length = random.randint(3, 6)
        key = generate_vigenere_key(key_length)
        ciphertext = vigenere_encrypt(plaintext, key)

    else:  
        key_int = random.randint(1, 255)
        ciphertext = xor_encrypt(plaintext, key_int)
        key = str(key_int)

    return {
        "plaintext": plaintext,
        "ciphertext": ciphertext,
        "cipher_type": cipher_type,
        "key": key
    }

def generate_dataset(n_samples, output_file):
    random.seed(42)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["plaintext", "ciphertext", "cipher_type", "key"]
        )
        writer.writeheader()

        for _ in range(n_samples):
            sample = generate_sample()
            writer.writerow(sample)

if __name__ == "__main__":
    output = "crypto_dataset.csv"
    generate_dataset(1000, output)
    print(f"[✓] Dataset generated: {output}")

