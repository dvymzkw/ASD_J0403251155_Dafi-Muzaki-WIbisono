#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 4: Kombinasi Huruf

#==============================

def kombinasi(n, hasil=""): # 'n' adalah panjang target string, 'hasil' adalah string yang sedang dibangun (kosong di awal).
    #Base case
    if len(hasil) == n: # Jika string 'hasil' sudah sama dengan 'n', satu kombinasi berhasil dibuat.
        print(hasil)
        return

    #Recursive case
    kombinasi(n, hasil + "D") # Tambahkan karakter D ke dalam string
    kombinasi(n, hasil + "C") # Tambahkan karakter C ke dalam string

kombinasi(6)
