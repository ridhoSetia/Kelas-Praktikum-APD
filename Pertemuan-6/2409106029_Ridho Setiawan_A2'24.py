# deklarasi dictionary
daftar_laptop = {
    "laptop1": "Acer",
    "laptop2": "Asus",
    "laptop3": "Lenovo"
}

# akses dictionary
print(daftar_laptop["laptop1"])

daftar_film = {}

daftar_film["film1"] = "Spiderman"
daftar_film["film2"] = "Bat Man"
daftar_film["film3"] = "Superman"

print(daftar_film)

# sifat dictionary
# 1. unordered
# 2. changeable
# 3. unique

biodata = {
    "nama": "Ridho Setiawan",
    "umur": 18,
    "prodi": "Informatika",
    "minat": ["Web Dev", "AI"], # dictionary of list
    "social media": {
        "instagram": "@ridho.setia_wan_",
        "linkedin": "Ridho Setiawan"
    }
}

print(biodata["minat"][0])
print(biodata["social media"]["instagram"])

# get()
print(biodata.get('social media')) # pake petik satu ''

# loop dictionary

# tanpa items
for i in daftar_laptop:
    print(f"Nilai {i} adalah {daftar_laptop[i]}")

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}

# pake items
for mapel, nilai in Nilai.items():
    print(f"Nilai {mapel} adalah {nilai}")

# tambah/timpa
Nilai['Prakarya'] = 89
Nilai.update({'Geografi': 82})
print(Nilai)

# # delete
# del Nilai["Fisika"]
# print(Nilai)

# # pop()
# cache = Nilai.pop("Kimia")
# print(Nilai)
# print(cache)

# # hapus isi
# Nilai.clear()
# print(Nilai)

# len()
print(f"jumlah key = {len(daftar_laptop)}")

# copy()
bajak = daftar_film.copy()
print(f"film yang dipinjam {bajak}")

# fromkeys
key = "manggis", "jeruk"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

# keys() and values(
# mengambil keynya saja
for i in Nilai.keys():
    print(i)

print("")

# mengambil valuenya saja
for i in Nilai.values():
    print(i)

# setdefault

#sebelum Setdefault
print(Nilai)
print("")

#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Biologi", 70))
print("")

#setelah menggunakan setdefault
print(Nilai)

# Dictionary of List
Musik = {
    "The Chainsmoker" : ["All we Know", "The Paris"],
    "Alan Walker" : ["Alone", "Lily"],
    "Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")

# Nested Dictionary
mahasiswa = {
    101 : {"Nama" : "Mamat", "Umur" : 20},
    111 : {"Nama" : "Asep", "Umur" : 22}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa :", key)
    for key_a, value_a in value.items():
        print (key_a, ":", value_a)
    print("")

#Menambahkan Item pada Nested Dictionary
mahasiswa[101]["Angkatan"] = 2023
print(mahasiswa)

#Mengubah Item pada Nested Dictionary
mahasiswa[101]["Nama"] = "Rizal"
print(mahasiswa)

#Menghapus Item pada Nested Dictionary
del mahasiswa[101]["Umur"]
print(mahasiswa)

mhs = {
    "Nama": "Ridho",
    "Umur": 18,
    "NIM": 2409106029,
    "Jurusan": "Informatika",
    "Angkatan": "2024"
}

print("""
1. Tambah item baru
2. Ubah satu key
3. Hapus satu key
""")

pilih = int(input("Pilih 1-3 : "))
if pilih == 1:
    print(mhs)
    
    tambahItemKey = input("Nama key : ")
    tambahItemValue = input("Nama value :")
    mhs[tambahItemKey] = tambahItemValue
    
    print(mhs)

elif pilih == 2:
    print(mhs)

    ubahItemKey = input("Nama key : ")
    ubahItemValue = input("Nama value :")
    Nilai[ubahItemKey] = ubahItemValue

    print(mhs)

elif pilih == 3:
    print(mhs)

    hapusItem = input("Key yang ingin dihapus :")
    del mhs[hapusItem]

Nilai = {
    "Matematika" : 90,
    "Fisika" : 80,
    "Biologi" : 80,
    "Kimia" : 70
}

totalNilai = sum(Nilai.values())
print(f"Total nilai {totalNilai}")
rata_rata = (totalNilai/len(Nilai))
print(f"Rata-rata nilai {rata_rata}")