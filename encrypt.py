huruf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def Encrypt(pesan,kunci):
    pesan = pesan.upper()
    ciphertext = ''
    for simbol in pesan:
        if simbol in huruf:
            nomor = huruf.find(simbol)
            nomor = (nomor + kunci) % 26
            ciphertext += huruf[nomor]
        else:
            ciphertext += simbol
    return ciphertext