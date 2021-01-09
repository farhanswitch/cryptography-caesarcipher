huruf = 'abcdefghijklmnopqrstuvwxyz'


def Encrypt(pesan, kunci):
    pesanHurufKecil = pesan.lower()
    ciphertext = ''
    indeksKapital = []
    for kapital in pesan:
        if kapital in pesan.upper():
            indeksKapital.append(pesan.find(kapital))

    for simbol in pesanHurufKecil:
        if simbol in huruf:
            nomor = huruf.find(simbol)
            nomor = (nomor + kunci) % 26
            ciphertext += huruf[nomor]
        else:
            ciphertext += simbol
    chpr = []
    for a in ciphertext:
        chpr.append(a)
    for isi in indeksKapital:
        chpr[isi] = chpr[isi].upper()
    hasil = ''
    for anggota in chpr:
        hasil += anggota

    return hasil
