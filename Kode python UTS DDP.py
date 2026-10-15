import math
import time
from prettytable import PrettyTable
import os

os.system("cls") if os.name == "nt" else "clear"

while True:
    print("=======================================================================================================")
    print("                              SISTEM PENILAIAN BERAT BADAN IDEAL                                       ")
    print("=======================================================================================================")
    print("                             Pilih salah satu:                                                         ")
    print("                                   1. Hitung Berat Badan Ideal                                         ")
    print("                                   2. Lihat Kategori IMT                                               ")
    print("                                   3. Keluar                                                           ")
    print("=======================================================================================================")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("===================================================================================================")
        print("Pilih jenis kelamin")
        print("1. Laki-laki")
        print("2. Perempuan")
        print("===================================================================================================")
        jenis_kelamin = input("Pilih jenis kelamin: ")


        if jenis_kelamin == "1":
                berat_badan = float(input("Masukkan berat badan anda (kg)!: "))
                tinggi_cm = float(input("Masukkan tinggi badan anda! (cm): "))

                berat_ideal = (tinggi_cm - 100) * 0.90
        
        elif jenis_kelamin == "2":
                berat_badan = float(input("Masukkan berat badan anda (kg)!: "))
                tinggi_cm = float(input("Masukkan tinggi badan anda! (cm): "))

                berat_ideal = (tinggi_cm - 100) * 0.85

        else:
            print("Jenis kelamin tidak valid!")
            continue

        
        if berat_badan <= 0 or tinggi_cm <= 0:
            print("Berat dan tinggi badan harus lebih dari 0!")
            continue

    elif pilihan == "2":
        tabel = PrettyTable()
        tabel.field_names = ["Kategori", "IMT (kg/m2)"]
        tabel.add_row(["Underweight", "<18,5"])
        tabel.add_row(["Normal", "18.5-22.9"])
        tabel.add_row(["Overweight", "23-24.9"])
        tabel.add_row(["Obesitas tingkat 1", "25-29.9"])
        tabel.add_row(["Obesitas tingkat 2", ">30"])

        print(tabel)
        time.sleep(5)
        continue

    elif pilihan == "3":
        print("Terimakasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan anda tidak valid!")

        ulang = input("Apakah anda ingin menghitung kembali (y/n)? ")

    tinggi_badan = tinggi_cm / 100
    imt = berat_badan / math.pow(tinggi_badan, 2)

    if imt < 18.5:
        kategori = "Berat badan kurang ideal"
    elif imt < 25:
        kategori = "Berat badan ideal"
    elif imt < 30:
        kategori ="Berat badan berlebih"
    else:
        kategori = "Obesitas"
        
    konfirmasi = input("Apakah anda yakin ingin melihat hasil perhitungan? (y/n) ")
    if konfirmasi == "y":
        print("\n===================================== HASIL PERHITUNGAN =============================================")
        print(f"Berat badan anda: {berat_badan:.2f} kg")
        print(f"Tinggi badan anda: {tinggi_badan:.2f} m")
        print(f"Nilai IMT: {imt:.2f}")
        print(f"Kategori berat badan anda: {kategori}")
    else:
        ("Hasil perhitungan tidak jadi ditampilkan")
    time.sleep (5)