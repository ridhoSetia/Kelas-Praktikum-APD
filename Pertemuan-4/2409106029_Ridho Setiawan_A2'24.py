# # Perulangan For
# for i in range(2, 10, 2):
#     print(f"perulangan {i}")

# print("Menu minuman botol")
# save = ["coca cola", "sprite", "fanta", "pocari sweat"]
# for i in save:
#     print(i)

# print("Menu minuman botol")
# minuman = ["coca cola", "sprite", "fanta", "pocari sweat"]
# # for i, menu in enumerate(minuman, start=1):
# #     print(f"{i}. {menu}")
# for i in range(len(minuman)):
#     print(f"{i+1}. {minuman[i]}")

# # Nested For Loop
# makanan = ["bakso", "indomie", "cilok", "ayam"]
# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")

# # While Loop
# jawab = 'y'
# hitung = 0
# while (jawab == 'y' == jawab == 'Y'):
#     hitung += 1
#     jawab = input("ulang gak?")
# print(f"total perulangan {hitung}")

# i = 0
# while i < 5:
#     print(i)
#     i+=1

# # Break
# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("mau ulang? ").lower()
#     if ulang == 'tidak':
#         print("oke udahan")
#         break
# print(f"Total perulangan : {hitung}")

# # Continue
# print("bilangan ganjil")
# for i in range(10):
#     if i % 2 == 0:
#         # bila kondisi benar maka langsung melakukan perulangan
#         # dengan melewati kode setelah continue
#         continue
#     print(i)

# Studi Kasus 1

# Meminta input dari pengguna untuk range maksimal
range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
for angka in range(1, range_maksimal):
    angka += 1
    apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
    for i in range(2, angka):
        if angka % i == 0:
            apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
            # print(f"{angka} bukan prima")
            break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
    if apakah_prima == True:
        print(f"{angka} prima")
        hitung_prima += 1

# output
print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")

# Studi Kasus 2
total = 0

while True:
    angka = int(input("Masukkan angka positif (input negatif untuk berhenti): "))
    if angka < 0:
        break
    total += angka