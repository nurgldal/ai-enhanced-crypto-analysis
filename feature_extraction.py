import math
import string
import numpy as np

ALPHABET = string.ascii_uppercase

def shannon_entropy(text: str) -> float:
    if not text:
        return 0.0

    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    entropy = 0.0
    length = len(text)

    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy

def index_of_coincidence(text: str) -> float:
    text = [ch for ch in text if ch in ALPHABET]
    N = len(text)

    if N <= 1:
        return 0.0

    freqs = {ch: 0 for ch in ALPHABET}
    for ch in text:
        freqs[ch] += 1

    numerator = sum(f * (f - 1) for f in freqs.values())
    denominator = N * (N - 1)

    return numerator / denominator

def letter_frequency_vector(text: str):
    text = [ch for ch in text if ch in ALPHABET]
    length = len(text)

    if length == 0:
        return [0.0] * 26

    freqs = {ch: 0 for ch in ALPHABET}
    for ch in text:
        freqs[ch] += 1

    return [freqs[ch] / length for ch in ALPHABET]

def extract_features(ciphertext: str):
    ciphertext = ciphertext.upper()

    features = []

    #Shannon Entropy
    features.append(shannon_entropy(ciphertext))

    #Index of Coincidence
    features.append(index_of_coincidence(ciphertext))

    #Ciphertext length
    features.append(len(ciphertext))

    #Letter frequency (26 features)
    features.extend(letter_frequency_vector(ciphertext))

    return np.array(features)

