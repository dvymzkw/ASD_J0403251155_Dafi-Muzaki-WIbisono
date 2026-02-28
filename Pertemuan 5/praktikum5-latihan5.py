#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 4: Generator PIN

#==============================

def buat_pin(panjang, hasil=""): # panjang (target digit pin), hasil (string penampung sementara)
    #Base case
    if len(hasil) == panjang: # Jika panjang string sudah sama dengan target digit, cetak pin
        print("PIN:", hasil)
        return
    
    #Recursive case
    for angka in ["0", "9", "6"]: # Memanggil fungsi dan menambahkan angka ke hasil
        buat_pin(panjang, hasil + angka)

buat_pin(4)