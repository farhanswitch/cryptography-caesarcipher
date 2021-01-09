import encrypt
import decrypt
teks = 'Aku'
encrypted = encrypt.Encrypt(teks, 5)

decrypted = decrypt.Decrypt(encrypted, 5)


print(f"Teks awal adalah {teks}")
print(f"Teks terenkripsi adalah {encrypted}")
print(f"Hasil dekripsi dari Ciphertext adalah {decrypted}")
