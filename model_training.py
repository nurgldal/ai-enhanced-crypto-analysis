import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from feature_extraction import extract_features

DATASET_PATH = "crypto_dataset.csv"

def load_dataset(path):
    df = pd.read_csv(path)

    X = []
    y = []

    for _, row in df.iterrows():
        ciphertext = row["ciphertext"]
        cipher_type = row["cipher_type"]

        features = extract_features(ciphertext)
        X.append(features)
        y.append(cipher_type)

    return X, y

def main():
    print("[*] Loading dataset...")
    X, y = load_dataset(DATASET_PATH)
    print(f"[*] Total samples: {len(X)}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("[*] Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )
    model.fit(X_train, y_train)

    print("[*] Evaluating model...")
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print("\nAccuracy:", round(acc, 4), "\n")

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()

