def Biodata(tahun_lahir, nama, asal):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahun_lahir
    tahun_angkatan = tahun_sekarang

    print(f"Perkenalkan Nama Saya : {nama}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : {tahun_angkatan}")
    print(f"Asal Saya dari : {asal}")

tahun_lahir = int(input())
nama = input()
asal = input()
Biodata(tahun_lahir, nama, asal)
