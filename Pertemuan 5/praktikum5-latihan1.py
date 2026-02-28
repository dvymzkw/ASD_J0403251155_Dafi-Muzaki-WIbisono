#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 1: Rekursi Pangkat

#==============================

def pangkat(a, n): # Mendefinisikan fungsi bernama 'pangkat' dengan 'a' sebagai basis & 'n' sebagai eksponen.
    # Base case
    if n == 0: # Jika pangkat nya 0, maka hasilnya selalu 1.
        return 1
    
    # Recursive case
    return a * pangkat(a, n - 1) # Mengalikan 'a' dengan fungsi, lalu n dikurangi 1 (proses akan terus mengulang sampai n = 0)

print(pangkat(6, 4)) # Output: 1296