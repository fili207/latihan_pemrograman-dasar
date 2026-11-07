print("Halo, ini aplikasi pertamaku!")
print("Selamat datang di Program Saya")
nama = input("Masukkan nama kamu: ")
print("Halo", nama, "! Semangat belajarnya ya!")
angka = int(input("Masukkan angka: "))
if angka % 2 == 0:
    print(angka, "adalah angka GENAP")
else:
    print(angka, "adalah angka GANJIL")
    jam = int(input("Sekarang jam berapa? (0-23): "))
if jam < 12:
    print("Selamat Pagi! 😊")
elif jam < 18:
    print("Selamat Siang/Sore! 🌤️")
else:
    print("Selamat Malam! 🌙")
    print("===== KALKULATOR SEDERHANA =====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilih = input("Pilih operasi (1-4): ")
a = float(input("Angka pertama: "))
b = float(input("Angka kedua: "))

if pilih == "1":
    print("Hasil =", a + b)
elif pilih == "2":
    print("Hasil =", a - b)
elif pilih == "3":
    print("Hasil =", a * b)
elif pilih == "4":
    print("Hasil =", a / b)
else:
    print("Pilihan tidak tersedia!")
    jam = int(input("Sekarang jam berapa? (0-23): "))