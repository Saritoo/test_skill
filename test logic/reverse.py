masukan_kata = input('')
kata = masukan_kata.split()
balikan = []
for i in kata:
    balikan.append(i[::-1])
hasil = " ".join(balikan)
print("kebalikan katanya adalah:",hasil)