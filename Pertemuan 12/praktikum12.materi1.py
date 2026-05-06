# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Materi 1: Algoritma Dijkstra
# ==========================================================

import heapq


# Graf berbobot yang direpresentasikan dengan dictionary bersarang.
# Formatnya: 'node_asal': {'node_tujuan': bobot_jarak}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    """
    Menghitung jarak terpendek dari node awal ke semua node lain
    menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tidak terhingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak_sementara, node).
    # Node dengan jarak paling kecil akan diproses lebih dulu.
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak yang diambil lebih besar dari jarak terbaik saat ini,
        # lewati karena data tersebut sudah tidak relevan.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node yang sedang diproses.
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            # Jika ditemukan jarak yang lebih pendek,
            # simpan jarak baru tersebut dan masukkan ke priority queue.
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari node A.
hasil = dijkstra(graph, 'A')
print(hasil)
