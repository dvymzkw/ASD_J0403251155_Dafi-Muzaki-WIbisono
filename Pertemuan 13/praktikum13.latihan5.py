# ========================================================== 
# Dafi Muzaki Wibisono
# J0403251155
# B2
# Latihan 5
# ========================================================== 

# Representasi weighted graph dalam bentuk list of tuples (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Implementasi Algoritma Kruskal
# Urutkan berdasarkan bobot (indeks ke-0 dari tuple)
edges.sort()

parent = {}

def find(node):
    if parent[node] == node:
        return node
    return find(parent[node])

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        parent[root1] = root2
        return True
    return False

# Inisialisasi setiap node sebagai parent dirinya sendiri
nodes = ['RouterA', 'RouterB', 'RouterC', 'RouterD']
for node in nodes:
    parent[node] = node

mst = []
total_weight = 0

# Proses seleksi edge
for weight, u, v in edges:
    if union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

# Output MST dan Total Bobot
print("--- Hasil Minimum Spanning Tree (Jaringan Komputer) ---")
print("Edge yang dipilih untuk MST:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (Bobot: {edge[2]})")

print(f"\nTotal bobot minimum: {total_weight}")

"""
PENJELASAN PROGRAM:
- Representasi: Menggunakan list of tuples agar mudah diurutkan (sorting).
- Algoritma Kruskal: Memilih edge dengan biaya terkecil secara global.
- Disjoint Set (find/union): Digunakan untuk mendeteksi siklus. 
  Jika dua router sudah terhubung di komponen yang sama, edge dilewati.
"""

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    (RouterC, RouterD, 1), (RouterA, RouterC, 2), (RouterA, RouterB, 3).
#
# 4. Berapa total bobot MST?
#    Total bobot = 1 + 2 + 3 = 6.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Edge (RouterB, RouterC, 4) dan (RouterB, RouterD, 5) tidak dipilih 
#    karena akan menciptakan siklus (jalur tertutup yang redundan) 
#    dalam jaringan, yang justru menambah biaya tanpa menambah konektivitas.