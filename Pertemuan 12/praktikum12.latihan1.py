# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang.
# Formatnya: 'node_asal': {'node_tujuan': bobot}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D.
# Jalur 1 melewati node B, yaitu A -> B -> D.
jalur_1 = graph['A']['B'] + graph['B']['D']

# Jalur 2 melewati node C, yaitu A -> C -> D.
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Membandingkan total bobot kedua jalur untuk menentukan jalur terpendek.
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
#    Total bobot jalur A -> B -> D adalah 9,
#    karena bobot A -> B = 4 dan B -> D = 5.
#
# 2. Berapa total bobot jalur A -> C -> D?
#    Total bobot jalur A -> C -> D adalah 3,
#    karena bobot A -> C = 2 dan C -> D = 1.
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Karena jalur terpendek ditentukan oleh total bobot, bukan hanya jumlah edge.
#    Meskipun dua jalur memiliki jumlah edge yang sama, total bobotnya bisa berbeda.
