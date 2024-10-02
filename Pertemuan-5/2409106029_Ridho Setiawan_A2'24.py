# element list bisa menggunakan tipe data apapun
kardus = ["mainan", True, 61, 1.5, [5, 3,["a", "z"]]]

name = ["umar", "kobi", "steven"]
print(type(name))

name[0] = "lame"
print(name)

print("sebelum append")
name.append("himel")
print("sesudah append")
print(name)

print("sebelum insert")
name.insert(0, "reiner")
print("setelah insert")
print(name)

# hapus isi list
del name[0]
print(name)

# pop, mengambil dan memindahkan isi dari list
pindah = name.pop(1)
print(pindah)

# slicing list
makanan = ["bakso", "mie ayam", "pentol", "cilok", "martabak", "sosis"]
# variabel[start:stop:step]
print(makanan[0:5:2])

# operasi list
print(name+makanan)
print(name*2)

# nested list
print(kardus[4][2][1])

benda = [["kursi", "meja", "piring"],["sandal", "sepatu", "kaus kaki"],["bakso", "mie ayam", "pentol"]]
for i in benda:
    for j in i:
        print(j, end=", ")

print("\n")

# nested tuple
tuple1 = ('a', 'b', 'c')
tuple2 = ('d', 'e', 'f')

gabung_tuple = tuple1, tuple2
print(gabung_tuple)

# unpacking tuple
identitas = (24, 4, 2006, "Ridho Setiawan")
tgl, bln, thn, nama = identitas
print(tgl)

# CRUD
print(
"""
== DATA MAHASISWA ==
--------------------
1. TAMBAH DATA
2. TAMPILKAN DATA
3. UBAH DATA
4. HAPUS DATA
5. KELUAR
--------------------
====================
"""
)

data_mhs = []
while True:
    pilih = int(input("\nPILIH : "))
    if pilih == 1:
        print("== TAMBAH DATA ==")
        nama = input("Nama : ")
        nim = input("NIM : ")
        kelas = input("Kelas : ")
        data_mhs.append([nama, nim, kelas])

    elif pilih == 2:
        print("== DATABASE ==")
        for data in data_mhs:
            print(data)
            for mhs in range(len(data)):
                print(mhs)
                print(f"Data Mahasiswa {mhs+1}\nNama : {nama} \nNIM : {nim} \nKelas : {kelas}")

    # elif pilih == 3:

    # elif pilih == 4:
        
    # elif pilih == 5: