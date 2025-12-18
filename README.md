# 🔐 AI-Enhanced Crypto-Analysis  
### *Artificial Intelligence for Automatic Cryptanalysis*

---

## 🇬🇧 English

### 📌 Project Description
This project presents an **AI-enhanced automatic cryptanalysis system** designed to identify and analyze classical ciphers under a **ciphertext-only attack model**.  
By integrating **machine learning techniques** with **traditional cryptanalysis**, the system automatically predicts the cipher type and applies the appropriate cryptanalytic attack when sufficient confidence is achieved.

---

### 🚀 System Overview
The proposed pipeline consists of the following stages:

1. Synthetic dataset generation using classical ciphers  
2. Cryptographic feature extraction (entropy, index of coincidence, letter frequencies)  
3. Cipher type classification using a Random Forest model  
4. Confidence-based decision mechanism to suppress unreliable attacks  
5. Automatic cipher-specific cryptanalysis  
6. End-to-end command-line demonstration  

---

### 🧠 Supported Cipher Types
- Caesar Cipher  
- Vigenere Cipher  
- XOR Cipher  

---

### 🛠 Technologies Used
- Python  
- Scikit-learn  
- NumPy  
- Pandas  
- WSL (Ubuntu)  

---

### ▶️ How to Run
```bash
# Generate the dataset
python dataset_generator.py

# Train the machine learning model
python model_training.py

# Run the demo application
python app.py
