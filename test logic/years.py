print("tahun awal")
tahun1 = int(input())
print("tahun akhir")
tahun2 = int(input())

print("hasil:")
for tahun in range(tahun1, tahun2):
    if (0 == tahun % 4) and (0 != tahun % 100) or (0 == tahun % 400):
        print(tahun)