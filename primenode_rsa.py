# =========================================================
# TUGAS KRIPTOGRAFI: IMPLEMENTASI RSA FROM SCRATCH
# Nama : Kirana Shofa Dzakiyyah
# NIM  : 25051204358
# Deskripsi: Implementasi murni tanpa library kriptografi
# =========================================================

def gcd(a, b):
    """Mencari Faktor Persekutuan Terbesar (FPB)"""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm:
    Digunakan untuk mencari Modular Multiplicative Inverse.
    Mencari d sehingga (e * d) % phi == 1.
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(e, phi):
    """Menentukan kunci privat (d) secara matematis"""
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Invers modular tidak ditemukan!')
    else:
        # x mungkin negatif, maka kita ambil modulo phi
        return x % phi

def generate_keys(p, q):
    """Proses Pembangkitan Kunci (Key Generation)"""
    # 1. Menghitung n (Modulus)
    n = p * q
    
    # 2. Menghitung Totient Euler (phi)
    phi = (p - 1) * (q - 1)
    
    # 3. Memilih e (Kunci Publik)
    # Standar industri adalah 65537, jika tidak memungkinkan pakai 3
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        
    # 4. Menghitung d (Kunci Privat) menggunakan Extended GCD
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt(message, public_key):
    """
    Proses Enkripsi: C = M^e mod n
    """
    e, n = public_key
    # ord(char) mengubah karakter ke angka ASCII
    # pow(base, exp, mod) adalah cara paling efisien untuk (M^e % n)
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(cipher, private_key):
    """
    Proses Dekripsi: M = C^d mod n
    """
    d, n = private_key
    # pow(char, d, n) mengembalikan angka ke kode ASCII asal
    # chr() mengubah angka ASCII kembali ke karakter teks
    plain = [chr(pow(char, d, n)) for char in cipher]
    return "".join(plain)

# --- DEMO PROGRAM ---
if __name__ == "__main__":
    print("="*45)
    print("SISTEM ENKRIPSI RSA - IMPLEMENTASI MANDIRI")
    print("="*45)

    # Langkah 1: Tentukan bilangan prima p dan q
    # (Dalam praktiknya menggunakan prima yang sangat besar)
    p = 61
    q = 53
    
    # Langkah 2: Bangkitkan Kunci
    pub_key, priv_key = generate_keys(p, q)
    
    print(f"[+] Bilangan Prima : p={p}, q={q}")
    print(f"[+] Kunci Publik (e, n): {pub_key}")
    print(f"[+] Kunci Privat (d, n): {priv_key}")
    print("-" * 45)

    # Langkah 3: Input Pesan
    plaintext = "ALGO"
    print(f"Plaintext Asli     : {plaintext}")

    # Langkah 4: Enkripsi
    ciphertext = encrypt(plaintext, pub_key)
    print(f"Ciphertext (List)  : {ciphertext}")

    # Langkah 5: Dekripsi
    hasil_dekripsi = decrypt(ciphertext, priv_key)
    print(f"Hasil Dekripsi     : {hasil_dekripsi}")
    print("="*45)