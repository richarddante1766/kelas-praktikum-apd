# nama=['Shandy', 106, True, ["yuyun", 123], 3.96, [123, "alvito", False, 3.66], "rehan"]

# # print (nama [4])
# print (nama [4] [-2])
# print (nama [5] [0])

# matkul = ["Apd", 
#           "Apl", 
#           "Web", 
#           "Jarkom", 
#           "BASDAT", 
#           "STRUKDAT", 
#           "PTI", 
#           "KALKULUS", 
#           "PROBAS"
#           ]
# print (nama)
# print (matkul)
# print (nama [1])
# print (matkul [6])
# print (matkul [-1])

# makanan = ["bakso", "sate", "soto", "nasigoreng", "mie ayam", "ayam bakar", "cumi goreng"]
# print ("sebelum: ")
# print (makanan)
# # print (makanan [1:6])
# # makanan.append ("nasi goreng")
# print ("sesudah:")
# makanan.clear ()
# print (makanan)
# # data  = makanan.pop (5)
# # print (makanan)
# # print (data)
# # del makanan [:2]
# # print (makanan)
# # makanan.insert(1, "nasigoreng")
# # makanan[1] = ["ayam", "bebek"]
# # print (makanan)

# minuman = ["susu", "jus mangga", "jus sirsak", "es teler", "es teh", "es buah"]
# print ("sebelum :")
# print (minuman)
# print ( )
# print ("sesudah:")
# print ( )
# print ("ditambah")
# minuman.insert (0, "jus tomat")
# print (minuman)
# print ( )
# print ("diganti")
# minuman [4] = "air putih"
# print (minuman)
# print ( )
# print ("dihapus")
# del minuman [2]
# print (minuman)

# makanan = ["ayam", "ikan", ["bakso", "soto", "sate", "ikan", "bebek"], ["teh", "kopi", "air"]]
# for i in makanan:
#     if isinstance (i, list):
#         for j in i :
#             print (j)
#     else:
#         print (i)


akuns =[]

while True:
    print ("Halo! Selamat datang di aplikasi Catatan")
    print ("Silahkan pilih 'Daftar Akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'login'")
    print ('1. Daftar Akun')
    print ('2. Login')
    print ("3. Exit")
    print ("-------------------")
    opsi = input("pilih opsi: ")
    print (" ")

    if opsi == "1":
        print ("Halo Pengguna baru ! Ayp buat akun dulu")
        Username = input ("username :")
        akuna = False
        for akun in akuna:
            if akun [0] == 'username': 
                akuna = True
                break
        if akuna:
            print ("Nama Sudah Terpakai untuk Registrasi Silahkan dicoba lagi")
        else:
            Password = input ("password:")
            akuna.append (('username', 'password', []))
            print (f"Akun anda berhasil terdaftar dengan ID: [Username]")