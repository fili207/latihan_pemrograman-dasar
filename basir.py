# Mencari angka maksimal dari 2 angka

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 > angka2:
    print("Angka maksimal adalah:", angka1)
elif angka2 > angka1:
    print("Angka maksimal adalah:", angka2)
else:
    print("Kedua angka sama")