# 🛡️ PrimeNode RSA: A Pure Logic Implementation

**PrimeNode RSA** is a custom implementation of the **RSA (Rivest–Shamir–Adleman)** asymmetric algorithm. This project was developed as an academic assignment to demonstrate the step-by-step process of converting plaintext into ciphertext using pure mathematical logic without relying on high-level cryptographic libraries.

---

## 🎯 Project Objectives
Based on the assignment requirements, this project aims to:
* **Analyze** the theoretical concepts of asymmetric encryption.
* **Implement** the RSA algorithm from scratch (Key Generation, Encryption, and Decryption).
* **Visualize** the mathematical flow of data security.

---

## 🛠️ Core Components

### 1. Introduction (History & Usage)
The RSA algorithm, named after Ron Rivest, Adi Shamir, and Leonard Adleman, was first published in 1977. It is the backbone of modern internet security, widely used for:
* **Digital Signatures:** Verifying the authenticity of documents.
* **Key Exchange:** Securely sharing symmetric keys over insecure channels (SSL/TLS).

### 2. Key Generation Process
This implementation uses the **Extended Euclidean Algorithm** to ensure mathematical accuracy in finding the private key.
* **Select Primes:** Choose two distinct prime numbers, $p$ and $q$.
* **Compute Modulus ($n$):** $n = p \times q$.
* **Compute Totient ($\phi$):** $\phi(n) = (p-1) \times (q-1)$.
* **Public Key ($e$):** An integer such that $1 < e < \phi(n)$ and $gcd(e, \phi(n)) = 1$.
* **Private Key ($d$):** Calculated as the modular multiplicative inverse of $e$ modulo $\phi(n)$.



### 3. Encryption Mechanism
The encryption process converts plaintext characters into numerical values (ASCII) and applies the formula:
$$C = M^e \pmod{n}$$
* $M$: Plaintext message (numeric)
* $e$: Public exponent
* $n$: Modulus
* $C$: Resulting ciphertext

### 4. Decryption Mechanism
The decryption process restores the original message using the private key ($d$) with the formula:
$$M = C^d \pmod{n}$$
The resulting numeric values are then converted back into human-readable characters.

---

## 📊 Security Analysis

| Aspect | Description |
| :--- | :--- |
| **Strengths** | Extremely difficult to break due to the "Integer Factorization Problem." High reliability for secure key distribution. |
| **Weaknesses** | Computationally expensive and slower than symmetric algorithms (like DES/RC4). Requires very large prime numbers (e.g., 2048-bit) to remain secure against modern hardware. |

---

## 🚀 How to Run
1.  Ensure you have **Python 3.x** installed.
2.  Clone this repository:
    ```bash
    git clone [https://github.com/KirshX07/PrimeNode_RSA.git](https://github.com/KirshX07/PrimeNode_RSA.git)
    ```
3.  Run the main script:
    ```bash
    python primenode_rsa.py
    ```

---

## 👤 Author Information
* **Name:** Kirana Shofa Dzakiyyah
* **NIM:** 25051204358
* **Course:** Cryptography (Individual Assignment)
