#===============================
# Dafi Muzaki Wibisono
# J0403251155
# Latihan 2: Studi Kasus DFS
#===============================

graph = { 'A': ['B', 'C'], 
         'B': ['D', 'E'], 
         'C': ['F'], 
         'D': [], 
         'E': [], 
         'F': [] 
} 

def dfs(graph, node, visited): 
    visited.add(node) 
    print(node, end=" ") 
    for neighbor in graph[node]: 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)

visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited)

# Pertanyaan Analisis 
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu? 
#    Jawaban:
#    Karena DFS memakai prinsip rekursi atau stack, 
#    jadi dia bakal selesaikan satu jalur sampai mentok 
#    sebelum balik lagi ke atas untuk cek jalur lain.

# 2. Apa yang terjadi jika urutan neighbor diubah?  
#    Jawaban:
#    Urutan kunjungannya pasti berubah total. 
#    Kalau 'C' ditaruh di depan 'B', maka jalur 'C' 
#    akan dikunjungi habis duluan sebelum mulai menyentuh 
#    jalur 'B'.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama. 
#    Jawaban:
#    DFS itu sifatnya vertikal (ke bawah dulu), sedangkan 
#    BFS itu horizontal (melebar). Pada graph yang sama,
#    BFS akan mengunjungi A-B-C dulu, baru ke D-E-F.