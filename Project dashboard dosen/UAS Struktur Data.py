def binary_search(data, target):
    data.sort()  # Urutkan data terlebih dahulu
    low = 0
    high = len(data) - 1
    langkah = 0  # Hitung jumlah langkah

    while low <= high:
        langkah += 1
        mid = (low + high) // 2  # Tentukan elemen tengah
        if data[mid] == target:
            return data[mid], langkah  # Kembalikan nilai dan jumlah langkah
        elif target < data[mid]:
            high = mid - 1  # Cari di bagian kiri
        else:
            low = mid + 1  # Cari di bagian kanan
    return None, langkah  # Jika target tidak ditemukan

target = 15  # Nilai yang akan dicari
hasil_binary, langkah = binary_search(urutan, target)
if hasil_binary is not None:
    print(f"Binary Search: Nilai {target} ditemukan dalam {langkah} langkah.")
else:
    print(f"Binary Search: Nilai {target} tidak ditemukan setelah {langkah} langkah.")
