# ============================================================
#  BAB XII - SORTING (SELECTION SORT)
#  JAWABAN LATIHAN 1, 2, DAN 3
# ============================================================


# ════════════════════════════════════════════════════════════
#  SOAL 1
#  Berikan langkah-langkah detail untuk mengurutkan
#  [80, 10, 50, 70, 60, 20] secara Ascending.
# ════════════════════════════════════════════════════════════

def selection_sort_ascending_verbose(arr):
    """
    Selection Sort Ascending dengan penjelasan langkah detail.
    """
    n = len(arr)
    print("=" * 60)
    print("SOAL 1 — Selection Sort Ascending: Langkah Detail")
    print("=" * 60)
    print(f"Data Awal : {arr}\n")

    for i in range(n - 1):
        min_idx = i
        print(f"┌─ Iterasi ke-{i+1} {'─'*40}")
        print(f"│  Bagian sudah terurut : {arr[:i] if arr[:i] else '(kosong)'}")
        print(f"│  Bagian belum terurut : {arr[i:]}")
        print(f"│  Asumsikan terkecil   : {arr[min_idx]} (indeks {min_idx})")

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                print(f"│    {arr[j]} < {arr[min_idx]} → terkecil baru: {arr[j]} (indeks {j})")
                min_idx = j
            else:
                print(f"│    {arr[j]} >= {arr[min_idx]} → lewati")

        if min_idx != i:
            print(f"│  ✔ Tukar {arr[i]} (indeks {i}) ↔ {arr[min_idx]} (indeks {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"│  ✔ {arr[i]} sudah di posisi benar, tidak perlu tukar")

        print(f"└─ Hasil iterasi ke-{i+1} : {arr}\n")

    print(f"✅ Array Terurut Akhir (Ascending): {arr}")
    return arr


print()
data_soal1 = [80, 10, 50, 70, 60, 20]
selection_sort_ascending_verbose(data_soal1.copy())


# ════════════════════════════════════════════════════════════
#  SOAL 2
#  list data = [7, 3, 9, 1, 5]
#  Bagaimana isi list setelah DUA iterasi pertama selesai?
#  Jelaskan setiap langkah pertukaran.
# ════════════════════════════════════════════════════════════

print("\n")
print("=" * 60)
print("SOAL 2 — Isi List Setelah 2 Iterasi Pertama")
print("=" * 60)

data_soal2 = [7, 3, 9, 1, 5]
print(f"Data Awal : {data_soal2}\n")

# ── Simulasi manual 2 iterasi pertama ──

arr = data_soal2.copy()
n   = len(arr)

for i in range(2):          # hanya 2 iterasi pertama
    min_idx = i
    print(f"┌─ Iterasi ke-{i+1} {'─'*40}")
    print(f"│  Bagian sudah terurut : {arr[:i] if arr[:i] else '(kosong)'}")
    print(f"│  Bagian belum terurut : {arr[i:]}")
    print(f"│  Asumsikan terkecil   : {arr[min_idx]} (indeks {min_idx})")

    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            print(f"│    {arr[j]} < {arr[min_idx]} → terkecil baru: {arr[j]} (indeks {j})")
            min_idx = j
        else:
            print(f"│    {arr[j]} >= {arr[min_idx]} → lewati")

    if min_idx != i:
        print(f"│  ✔ Tukar {arr[i]} (indeks {i}) ↔ {arr[min_idx]} (indeks {min_idx})")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    else:
        print(f"│  ✔ {arr[i]} sudah di posisi benar, tidak perlu tukar")

    print(f"└─ Hasil iterasi ke-{i+1} : {arr}\n")

print(f"📌 Isi list setelah 2 iterasi pertama: {arr}")
print("""
Penjelasan:
  Iterasi 1 → Cari terkecil dari [7,3,9,1,5] = 1 (indeks 3)
              Tukar 7 (indeks 0) ↔ 1 (indeks 3)
              Hasil: [1, 3, 9, 7, 5]

  Iterasi 2 → Cari terkecil dari [3,9,7,5] = 3 (indeks 1)
              3 sudah di posisi benar, tidak perlu tukar
              Hasil: [1, 3, 9, 7, 5]

  ∴ Setelah 2 iterasi: [1, 3, 9, 7, 5]
""")


# ════════════════════════════════════════════════════════════
#  SOAL 3
#  Modifikasi fungsi agar bisa mengurutkan STRING (nama buah)
#  secara alfabetis.
# ════════════════════════════════════════════════════════════

def selection_sort_universal(arr, ascending=True):
    """
    Selection Sort yang bisa mengurutkan angka MAUPUN string.

    Parameter:
        arr       : list berisi angka atau string
        ascending : True  → A–Z / kecil ke besar
                    False → Z–A / besar ke kecil

    Cara kerja:
        Python mendukung perbandingan string secara leksikografis
        (alfabetis) menggunakan operator < dan >, sehingga fungsi
        yang sama bekerja untuk angka maupun string tanpa perubahan
        logika inti — cukup tambahkan parameter 'ascending' untuk
        memilih arah urutan.
    """
    n     = len(arr)
    arah  = "Ascending (A→Z / kecil→besar)" if ascending else "Descending (Z→A / besar→kecil)"

    print("=" * 60)
    print(f"SOAL 3 — Selection Sort Universal ({arah})")
    print("=" * 60)
    print(f"Data Awal : {arr}\n")

    for i in range(n - 1):
        target_idx = i
        print(f"┌─ Iterasi ke-{i+1} {'─'*40}")
        print(f"│  Bagian sudah terurut : {arr[:i] if arr[:i] else '(kosong)'}")
        print(f"│  Bagian belum terurut : {arr[i:]}")

        for j in range(i + 1, n):
            # ascending → cari terkecil/terdepan alfabetis
            # descending → cari terbesar/terakhir alfabetis
            if (ascending and arr[j] < arr[target_idx]) or \
               (not ascending and arr[j] > arr[target_idx]):
                target_idx = j

        if target_idx != i:
            print(f"│  ✔ Tukar '{arr[i]}' (indeks {i}) ↔ '{arr[target_idx]}' (indeks {target_idx})")
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
        else:
            print(f"│  ✔ '{arr[i]}' sudah di posisi benar, tidak perlu tukar")

        print(f"└─ Hasil iterasi ke-{i+1} : {arr}\n")

    label = "Ascending Alfabetis" if ascending else "Descending Alfabetis"
    print(f"✅ Array Terurut Akhir ({label}): {arr}\n")
    return arr


# — Contoh 1: list string nama buah (ascending) —
print()
buah = ["mangga", "apel", "durian", "pisang", "jeruk", "anggur"]
selection_sort_universal(buah.copy(), ascending=True)

# — Contoh 2: list string nama buah (descending) —
buah2 = ["mangga", "apel", "durian", "pisang", "jeruk", "anggur"]
selection_sort_universal(buah2.copy(), ascending=False)

# — Contoh 3: list angka (ascending) — membuktikan fungsi universal —
angka = [42, 7, 19, 3, 55]
selection_sort_universal(angka.copy(), ascending=True)
