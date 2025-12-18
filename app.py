import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from feature_extraction import (
    extract_features,
    shannon_entropy,
    index_of_coincidence
)
from attack_engine import attack

#Configuration
DATASET_PATH = "crypto_dataset.csv"
CONFIDENCE_THRESHOLD = 0.75

#Plaintext detection parameters
ENTROPY_THRESHOLD = 2.5
IC_THRESHOLD = 0.07
MIN_LENGTH_FOR_PLAINTEXT_CHECK = 8



#Model Training
def train_model():
    print("[*] Training ML model...")

    df = pd.read_csv(DATASET_PATH)

    X, y = [], []
    for _, row in df.iterrows():
        X.append(extract_features(row["ciphertext"]))
        y.append(row["cipher_type"])

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)

    print("[✓] Model trained successfully\n")
    return model

#Plaintext Detection
def is_likely_plaintext(text: str) -> bool:
    """
    Detect plaintext only for very short inputs.
    This avoids false positives for monoalphabetic ciphers (e.g., Caesar).
    """
    if len(text) < MIN_LENGTH_FOR_PLAINTEXT_CHECK:
        entropy = shannon_entropy(text)
        ic = index_of_coincidence(text)

        if entropy < ENTROPY_THRESHOLD and ic > IC_THRESHOLD:
            return True

    return False

#Main Application
def main():
    print("=" * 70)
    print(" AI-Enhanced Automatic Crypto-Analysis System (Final Demo) ")
    print("=" * 70)

    model = train_model()

    while True:
        print("\nEnter ciphertext (or type 'exit'):")
        ciphertext = input("> ").strip()

        if ciphertext.lower() == "exit":
            print("Exiting application.")
            break

        #Plaintext detection
        if is_likely_plaintext(ciphertext):
            print("[!] Input is likely PLAINTEXT. Please provide encrypted text.")
            continue

        #Feature extraction
        features = extract_features(ciphertext)

        #Prediction with confidence
        probabilities = model.predict_proba([features])[0]
        max_confidence = float(np.max(probabilities))
        predicted_cipher = model.classes_[int(np.argmax(probabilities))]

        print(f"[+] Predicted Cipher Type: {predicted_cipher}")
        print(f"[+] Prediction Confidence: {max_confidence:.2f}")

        #Confidence threshold check
        if max_confidence < CONFIDENCE_THRESHOLD:
            print("[!] Low confidence prediction. Attack aborted.")
            continue

        #Automatic cryptanalytic attack
        plaintext, key = attack(predicted_cipher, ciphertext)

        print("[+] Recovered Plaintext:", plaintext)
        print("[+] Recovered Key:", key)


if __name__ == "__main__":
    main()

