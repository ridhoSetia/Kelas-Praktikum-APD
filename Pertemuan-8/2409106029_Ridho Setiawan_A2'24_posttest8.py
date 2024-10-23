# try:
#     angka = int(input('angka : '))
# except ValueError:
#     print('wajib angka!')
#     angka = int(input('angka : '))
# else:
#     print(f'kamu menginput angka : {angka}')
# finally:
#     print('program selesai')

# def tambah():
#     a = int(input("nilai 1 : "))
#     b = int(input("nilai 2 : "))
#     print(f"{a} + {b} = {a+b}")

# def menu():
#     while True:
#         print('''
# 1. tambah
# 2. exit
# ''')
#         try:
#             pilih = int(input("pilih menu : "))

#             if pilih == 1:
#                 tambah()
#             elif pilih == 2:
#                 exit(0)
#             else:
#                 print("pilihan tidak ada")


#         except ValueError:
#             print("wajib angka")

# menu()

import csv
import pandas as pd

# # Membaca seluruh isi file sekaligus
# with open('./Pertemuan-8/data.csv', 'r') as file:
#     konten = file.read()
#     print(konten)

# # Membaca baris per baris
# with open('./Pertemuan-8/data.csv', mode='r') as file:
#     for baris in file:
#       print(baris, end='')
#       print()

# # Menulis teks ke file
# with open('./Pertemuan-8/data.csv', 'w') as file:
#     file.write('Ini adalah w.\n')

df=pd.read_csv('./Pertemuan-8/data.csv')
print(df.head())

# nama = input('nama : ')
# umur = input('umur : ')
# profesi = input('profesi : ')

# def tambahData(index, nama, umur, profesi):
#     with open('./Pertemuan-8/data.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([index,nama,umur,profesi])

# # index = len(csv.reader(open('./Pertemuan-8/data.csv', 'r')))
# tambahData(1, nama, umur, profesi)

# try:
#     with open("./Pertemuan-8/data.csv") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File tidak ditemukan")