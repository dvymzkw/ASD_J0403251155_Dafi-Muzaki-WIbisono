#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 3: Mencari Nilai Maksimum

#==============================

def cari_maks(data, index=0): # Index dimulai dari 0
    # Base case
    if index == len(data) - 1: # Jika index sudah mencapai elemen terakhir dalam list, kembalikan nilai
        return data[index]
    
    # Recursive case
    maks_sisa = cari_maks(data, index + 1) # Mengecek elemen selanjutnya dalam list sampai menemukan nilai yang paling besar
    
    if data[index] > maks_sisa: # Membandingkan elemen saat ini dengan nilai terbesar dari sisa (nilai terbesar yang akan dikembalikan)
        return data[index]
    else:
        return maks_sisa

angka = [6, 9, 4, 2, 7]
print("Nilai maksimum:", cari_maks(angka))