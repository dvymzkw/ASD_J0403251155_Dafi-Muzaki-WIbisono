#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Latihan 2: Tracing Rekursi

#==============================

def countdown(n):
    #Base case
    if n == 0: # Jika n = 0, maka fungsi selesai.
        print("Selesai")
        return
    
    #Recursive case
    print("Masuk:", n) # Mencetak angka (n) yang masuk (besar sampai kecil)
    
    countdown(n - 1) # Mengurangi n sampai hasilnya 0
    
    print("Keluar:", n) # Mencetak angka (n) yang keluar (kecil sampai besar)

countdown(4) # Hitung mundur