# 🔐 AI-Enhanced Crypto-Analysis  
### *Artificial Intelligence for Automatic Cryptanalysis*

---

## 🇬🇧 English | 🇹🇷 Türkçe

### 📌 Project Description | Proje Açıklaması

**EN:**  
This project presents an **AI-enhanced automatic cryptanalysis system** designed to identify and analyze classical ciphers under a **ciphertext-only attack model**.  
By integrating **machine learning techniques** with **traditional cryptanalysis**, the system automatically predicts the cipher type and applies the appropriate cryptanalytic attack when sufficient confidence is achieved.

**TR:**  
Bu proje, **yalnızca şifreli metin (ciphertext-only)** varsayımı altında çalışan, **yapay zeka destekli otomatik bir kripto-analiz sistemi** sunmaktadır.  
Sistem, **makine öğrenmesi tekniklerini** **klasik kriptoloji yöntemleri** ile birleştirerek, şifreli metnin hangi şifreleme türüne ait olduğunu otomatik olarak tahmin eder ve yeterli güven seviyesi sağlandığında uygun kripto-analiz saldırısını uygular.

---

### 🚀 System Overview | Sistem Genel Bakışı

**EN:**  
The proposed pipeline consists of the following stages:

1. Synthetic dataset generation using classical ciphers  
2. Cryptographic feature extraction (entropy, index of coincidence, letter frequencies)  
3. Cipher type classification using a Random Forest model  
4. Confidence-based decision mechanism to suppress unreliable attacks  
5. Automatic cipher-specific cryptanalysis  
6. End-to-end command-line demonstration  

**TR:**  
Önerilen sistem aşağıdaki aşamalardan oluşmaktadır:

1. Klasik şifreleme algoritmaları kullanılarak sentetik veri seti oluşturma  
2. Şifreli metinden kriptografik özellik çıkarımı (entropi, çakışma indeksi, harf frekansları)  
3. Random Forest modeli ile şifre türü sınıflandırma  
4. Güven seviyesi düşük tahminleri bastırmak için güven tabanlı karar mekanizması  
5. Şifre türüne özgü otomatik kripto-analiz  
6. Komut satırı üzerinden uçtan uca demo uygulaması  

---

### 🧠 Supported Cipher Types | Desteklenen Şifre Türleri

- Caesar Cipher  
- Vigenere Cipher  
- XOR Cipher  

---

### 🛠 Technologies Used | Kullanılan Teknolojiler

- Python  
- Scikit-learn  
- NumPy  
- Pandas  
- WSL (Ubuntu)  

---

### ▶️ How to Run | Çalıştırma Adımları

```bash
# Generate the dataset | Veri seti oluşturma
python dataset_generator.py

# Train the machine learning model | Modeli eğitme
python model_training.py

# Run the demo application | Demo uygulamasını çalıştırma
python app.py

