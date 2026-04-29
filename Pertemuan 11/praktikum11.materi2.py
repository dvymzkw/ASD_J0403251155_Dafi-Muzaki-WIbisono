#===============================
# Dafi Muzaki Wibisono
# J0403251155
# Implementasi BFS
#===============================

# Struktur data untuk membuat antrian, gunakan library collections dari Python
from collections import deque


# Representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # Graph: Dictionary yang menyimpan struktur dari graph
    # Start: Node awal penelusuran

    # Queue digunakan untuk menyimpan node yang akan dibaca
    queue = deque()

    # Variabel yang digunakan untuk menyimpan node yang sudah dibaca
    visited = set()

    queue.append(start)

    # Tandai node awal sebagai node yang sudah dibaca
    visited.add(start)

    while queue:

        # Mengambil node paling depan dari queue
        node = queue.popleft()
        
        # Tampilkan node yang sedang dikunjungi
        print(node, end=' ')

        # Periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
           # Jika tetangga belum dikunjungi
           if neighbor not in visited:
                # Tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

# Menjalankan BFS dari node A
bfs(graph, 'A')
