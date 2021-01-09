import encrypt
import decrypt

__name__ = 'Enkripsi dan Dekripsi dengan Algoritma Kriptografi Caesar\'s Cipher'
while True:
    print('-'*15)
    print(f'Program {__name__}')
    print('''Menu :
            1. Enkripsi
            2. Dekripsi
            3. Keluar
    ''')
    print('Silahkan masukkan nomor menu')
    try:
        menu = int(input('>'))
    except:
        print('Anda harus memasukkan angka')
        continue

    if menu == 1:
        text = input('Silahkan masukkan pesan yang akan di enkripsi = ')
        kunci = int(input('Masukkan kunci untuk enkripsi (dalam angka) = '))
        encrypted = encrypt.Encrypt(text, kunci)

        print(f'Plaintext = {text}')
        print(f'Kunci = {kunci}')
        print(f'Pesan ter-enkripsi (Ciphertext) = {encrypted}')

        print('Apakah anda ingin kembali ke menu? Pilih (Y)a atau (T)idak ')
        pilihan = input('>')

        if pilihan.lower().startswith('y'):
            print('//Kembali ke Menu Utama')
        else:
            break
    elif menu == 2:
        ciphertext = input('Silahkan masukkan pesan yang akan di dekripsi = ')
        kunciDe = int(input('Masukkan kunci untuk dekripsi (dalam angka) = '))
        decrypted = decrypt.Decrypt(ciphertext, kunciDe)

        print(f'Ciphertext = {ciphertext}')
        print(f'Kunci = {kunciDe}')
        print(f'Pesan ter-dekripsi (Plaintext) = {decrypted}')

        print('Apakah anda ingin kembali ke menu? Pilih (Y)a atau (T)idak ')
        pilihan = input('>')

        if pilihan.lower().startswith('y'):
            print('//Kembali ke Menu Utama')
        else:
            break
    elif menu == 3:
        print('Sampai Jumpa Lagi')
        break
    else:
        print('Menu yang anda pilih tidak tersedia,pastikan anda sudah mengetik nomor menu dengan benar')
