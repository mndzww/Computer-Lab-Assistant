matriks = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

# Bilangan skalar
skalar = 3

# kali matriks dengan skalar
hasil = []
for baris in matriks:
    hasil_baris = []
    for elemen in baris:
        hasil_baris.append(elemen * skalar)
    hasil.append(hasil_baris)

# hasil
print("Hasil perkalian matriks dengan skalar:")
for baris in hasil:
    print(baris)

print("="*40)
matriks1 = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

matriks2 = [[9, 8, 7], 
            [6, 5, 4], 
            [3, 2, 1]]

hasil = []

# jml matriks
for i in range(len(matriks1)):  # Loop baris
    baris = []
    for j in range(len(matriks1[0])):  # Loop kolom
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)

print("Hasil penjumlahan dua matriks:")
for baris in hasil:
    print(baris)
