# ==========================================================
# Nama : Dafi Muzaki Wibisono
# NIM : J0403251155
# Kelas : TPL B2
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif.
# Bellman-Ford dapat digunakan selama tidak ada siklus negatif.
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}


def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga karena belum diketahui.
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0.
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1.
    for _ in range(len(graph) - 1):

        # Periksa semua edge pada graph.
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak.
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

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Bobot langsung dari A ke B adalah 5.
#
# 2. Berapa total bobot jalur A -> C -> B?
#    Total bobot jalur A -> C -> B adalah 2,
#    karena bobot A -> C = 4 dan C -> B = -2.
#
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B.
#
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Karena Bellman-Ford memeriksa dan memperbarui semua edge berulang kali,
#    sehingga masih dapat menemukan jarak terpendek walaupun ada bobot negatif.
#
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Relaksasi edge adalah proses memeriksa apakah suatu edge dapat menghasilkan
#    jarak yang lebih pendek ke node tujuan, lalu memperbarui jaraknya jika bisa.
#
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Bellman-Ford dapat menangani bobot negatif, tetapi lebih lambat.
#    Dijkstra lebih cepat, tetapi hanya cocok untuk graph tanpa bobot negatif.
