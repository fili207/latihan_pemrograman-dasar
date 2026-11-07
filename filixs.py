while True:
    nama = input("basyir: ")

    print("Halo,", nama)

    ulang = input("Mau memasukkan nama lagi? (y/n): ")

    if ulang.lower() != "y":
        print("Program selesai. Terima kasih!")
        break