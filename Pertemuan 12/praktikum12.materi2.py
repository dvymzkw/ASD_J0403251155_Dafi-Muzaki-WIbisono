# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Materi 2: Algoritma Bellman-Ford
# ==========================================================

# Graph berbobot yang memiliki edge dengan bobot negatif.
# Bellman-Ford tetap dapat digunakan selama graph tidak memiliki siklus negatif.
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}


def bellman_ford(graph, start):
    """
    Menghitung jarak terpendek dari node awal ke semua node lain
    menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0.
    distances[start] = 0

    # Relaksasi dilakukan sebanyak jumlah node - 1.
    # Tujuannya adalah memberi kesempatan setiap edge memperbarui jarak.
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika node asal sudah memiliki jarak yang valid,
                # periksa apakah edge ini menghasilkan jarak lebih pendek.
                if (
                    distances[node] != float('inf')
                    and distances[node] + weight < distances[neighbor]
                ):
                    distances[neighbor] = distances[node] + weight

    return distances


# Menjalankan algoritma Bellman-Ford dari node A.
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
