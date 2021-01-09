import encrypt


def Decrypt(cipherText, kunci):
    cipherHurufKecil = cipherText.lower()
    plainText = ''
    indeksKapital = []
    for kapital in cipherText:
        if kapital in encrypt.huruf.upper():
            indeksKapital.append(cipherText.find(kapital))

    for simbol in cipherHurufKecil:
        if simbol in encrypt.huruf:
            nomor = encrypt.huruf.find(simbol)
            nomor = (nomor - kunci) % 26
            plainText += encrypt.huruf[nomor]
        else:
            plainText += simbol

    plain = []
    for isi in plainText:
        plain.append(isi)
    for angka in indeksKapital:
        plain[angka] = plain[angka].upper()
    hasil = ''
    for anggota in plain:
        hasil += anggota

    return hasil
