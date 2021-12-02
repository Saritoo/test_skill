cek = input('')
idx = len(cek)
if idx % 2 == 1:
    for i in range(idx):
        if i != (idx//2):
            if cek[i] == cek[idx-i-1]:
                polindrom = True
            else:
                polindrom = False
else:
    for i in range(idx):
        if cek[i] == cek[idx-i-1]:
            polindrom = True
        else:
            polindrom = False
if polindrom == True:
    print("Polindrom.")
else:
    print("Bukan Polindrom.")