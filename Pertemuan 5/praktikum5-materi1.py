#==============================
# Dafi Muzaki Wibisono
# J0403251155
# TPL B2
#==============================

# Materi Rekursif: Faktorial
# Recursive case => 3! = 3 x 2 x 1
# Base case => 0 berhenti

#==============================

def faktorial(n):
    #Base case
    if n == 0:
        return 1

    #Reucrsive case
    return n*faktorial(n-1) #n-1*n-2*n-3......n-?
print('=== Program Faktorial ===')
print('Hasil faktorial: ', faktorial(10))
