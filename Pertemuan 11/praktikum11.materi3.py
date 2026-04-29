#===============================
# Dafi Muzaki Wibisono
# J0403251155
# Implementasi DFS
#===============================

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

def dfs(graph, node, visited):
    # Fungsi: Untuk melakukan penelusuran dengan DFS
    # Graph: dictionary yang menyimpan graph
    # Node: menyimpan node yang sedang dikunjungi
    # Visited: menyimpan node yang sudah dikunjungi

    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    # Tampilkan node yang dikunjungi
    print(node, end=' ')

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dibaca
        if neighbor not in visited:
            # Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# Menjalankan dfs dari A
visited = set()
dfs(graph, 'A', visited)