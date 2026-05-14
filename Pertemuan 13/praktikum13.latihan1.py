# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Latihan 1
# ========================================================== 

import heapq

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Perbedaan graph awal dan spanning tree:
#    Graph awal adalah struktur yang bisa memiliki jalur redundan (siklus) 
#    dan menghubungkan seluruh vertex dengan semua edge yang tersedia. 
#    Sedangkan spanning tree adalah subset dari graph awal yang menghubungkan 
#    seluruh vertex tanpa membentuk siklus (minimal connection).
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena definisi dasar sebuah 'tree' dalam teori graf adalah 
#    graf terhubung yang asiklik (tidak memiliki siklus). Jika sebuah graf 
#    memiliki cycle, maka ia mengandung redundansi jalur, yang berarti 
#    bukan lagi struktur tree yang efisien.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya mempertahankan jumlah edge minimum yang 
#    diperlukan untuk menjaga agar semua vertex tetap terhubung (terkoneksi). 
#    Edge tambahan pada graph awal biasanya berfungsi sebagai jalur alternatif 
#    (siklus), yang harus dihapus untuk mencapai properti tree (n vertex 
#    memerlukan tepat n-1 edge).