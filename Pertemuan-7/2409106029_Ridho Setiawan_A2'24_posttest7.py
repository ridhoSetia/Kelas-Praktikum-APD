# # prosedur

# def menu():
#     print("Menu Pilihan")
#     print("1. Tambah")
#     print("2. Kurang")
#     print("3. Kali")
#     print("4. Bagi")

# menu()

# def pesan():
#     print("Selamat pagi calon ahli IT")
# def tambah():
#     x = 4+5
#     print(x)

# pesan()
# tambah()

# # prosedur dengan parameter
# def pesan(nama):
#     print(f"Selamat sore {nama}")

# pesan("Ridho")

# a = int(input("angka 1:"))
# b = int(input("angka 2:"))

# def kali(a, b):
#     hasil = a*b
#     print(hasil)

# kali(3, 4)
# kali(a, b)

# # fungsi
# a = int(input("angka 1:"))
# b = int(input("angka 2:"))

# def bagi(a, b):
#     hasil = a/b
#     return hasil

# print(bagi(a, b))

# # rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print("Volume Persegi = ", volume)

# volume_persegi(4)

# Contoh CRUD menggunakan fungsi dan prosedur

buku =[]
def show_data():
    if len(buku) <= 0:
        print ("Belum Ada data")
    else:
        print("ID", "Nama Buku")
    for indeks in range(len(buku)):
        print (indeks+1, buku[indeks])

# fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
        print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")

while True:
    show_menu()
    menu = input("PILIH MENU> ")
    print ("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print ("Salah pilih!")